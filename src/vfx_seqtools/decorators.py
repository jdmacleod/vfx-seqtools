"""Permit options to be shared between multiple Typer scripts."""

# type: ignore

# https://github.com/fastapi/typer/discussions/742
import functools
import inspect
import typing
from typing import Any, Callable, TypeVar

from typing_extensions import Concatenate, ParamSpec

RHook = TypeVar("RHook")
ParamsHook = ParamSpec("ParamsHook")
RSource = TypeVar("RSource")
ParamsSource = ParamSpec("ParamsSource")


class BadHookError(TypeError): ...


def attach_hook(
    hook_func: Callable[ParamsHook, RHook], hook_output_kwarg: str = ""
) -> Callable[..., Any]:
    """
    Decorates a source function to be executed with a pre-execution hook function. The hook function's
    output is passed to the source function as a specified keyword argument. This decorator
    filters keyword arguments for the hook function according to its signature, and the rest of the arguments
    are passed to the source function. It updates the wrapper function's signature to include the combined
    list of arguments, excluding the internally managed hook_output_kwarg.

    The motivation for this utility is to allow combining groups of shared options for Typer cli scripts.
    Typer infers the command line arguments from a functions type annotations, and to share common groups of arguments
    between multiple scripts, there is a necessity to merge parameter lists of function.

    Usage Examples:

    common.py
    ```
    def logging_options(
        log_level: Annotated[int, typer.Option(help="Log level. Must be between 0 and 9."),
        log_to_file: Annotated[Optional[pathlib.Path], typer.Option(help="A file to stream logs to.") = None
        ):
        if log_level < 0 or log_level > 9:
          raise ValueError("log_level must be between 0 and 9.")
        ...
        # create logger
        ...
        return logger
    ```

    main1.py
    ```
    @attach_hook(common.logging_options, hook_output_kwarg="logger")
    def foo(size: int, logger: Logger):
        ....

    if __name__=="__main__":
        typer.run(foo)
    ```

    main2.py
    ```
    @attach_hook(common.logging_options, hook_output_kwarg="logger")
    def bar(color: str, logger: Logger):
        ....

    if __name__=="__main__":
        typer.run(bar)
    ```

    in the example above both main1 and main2 cli's enable to specify shared logging arguments from the command line,
    in addition to the specific argument of each script.

    Args:
        hook_func: The hook function to execute before the source function. All required argumenets must
            be allowed to be passed as keyword arguments.
        hook_output_kwarg: The keyword argument name for the hook's output passed to the source function.
                           If None, defaults to the hook function's name.

    Raises:
        BadHookError: If the hook function has an argument with no default value that collides with source.

    Returns:
        A decorator that chains the hook function with the source function, excluding the hook_output_kwarg
        from the wrapper's external signature.
    """
    if hook_output_kwarg is None or hook_output_kwarg == "":
        hook_output_kwarg = hook_func.__name__

    def decorator(
        source_func: Callable[Concatenate[RHook, ParamsSource], RSource],  # type: ignore
    ) -> Callable[Concatenate[ParamsSource, ParamsHook], RSource]:  # type: ignore
        source_params = inspect.signature(source_func).parameters

        # Raise BadHookError if the hook has non-default argument that collides with the `source_func`.
        dup_params = [
            k
            for k, v in inspect.signature(hook_func).parameters.items()
            if k in source_params and v.default == inspect.Parameter.empty
        ]
        if dup_params:
            raise BadHookError(
                f"The following non-default arguments of the hook function (`{hook_func.__name__}`) collide with the source func (`{source_func.__name__}`): {dup_params}"
            )
        hook_params = {
            k: v.replace(kind=inspect.Parameter.KEYWORD_ONLY)
            for k, v in inspect.signature(hook_func).parameters.items()
            if k not in source_params
        }

        @functools.wraps(source_func)
        def wrapper(*args: list, **kwargs: dict) -> RSource:
            # Filter kwargs for those accepted by the hook function
            hook_kwargs = {k: v for k, v in kwargs.items() if k in hook_params}

            # Execute hook function with its specific kwargs
            hook_result = hook_func(**hook_kwargs)  # type: ignore

            # Filter in the remaining kwargs for the source function.
            source_kwargs = {k: v for k, v in kwargs.items() if k not in hook_kwargs}

            # Execute the source function with original args and pass the hook's output to the source function as
            # the specified keyword argument
            # mypy bug: https://github.com/python/mypy/issues/18481
            return source_func(  # type: ignore
                *args,  # type: ignore
                **source_kwargs,  # type: ignore
                **{hook_output_kwarg: hook_result},  # type: ignore
            )  # type: ignore

        # Combine signatures, but remove the hook_output_kwarg
        combined_params = [
            param for param in source_params.values() if param.name != hook_output_kwarg
        ] + list(hook_params.values())
        # mypy bug: https://github.com/python/mypy/issues/12472
        wrapper.__signature__ = inspect.signature(source_func).replace(  # type: ignore
            parameters=combined_params
        )

        # Combine annotations, but remove the hook_output_kwarg
        wrapper.__annotations__ = {
            **typing.get_type_hints(source_func),
            **typing.get_type_hints(hook_func),
        }
        if hook_output_kwarg:
            wrapper.__annotations__.pop(hook_output_kwarg, None)

        return wrapper  # type: ignore

    return decorator
