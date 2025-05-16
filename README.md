# VFX seqtools

Command-line utilities for working with frame sequences in Animation and VFX.

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vfx-seqtools)](https://pypi.org/project/vfx-seqtools/)
 [![Build Status](https://github.com/jdmacleod/vfx-seqtools/actions/workflows/python-package.yml/badge.svg)](https://github.com/jdmacleod/vfx-seqtools/actions/workflows/python-package.yml)
[![Documentation](https://img.shields.io/badge/doc-latest-blue.svg)](https://jdmacleod.github.io/vfx-seqtools/) [![PyPI - Version](https://img.shields.io/pypi/v/vfx-seqtools)](https://pypi.org/project/vfx-seqtools/)

[![GitHub License](https://img.shields.io/github/license/jdmacleod/vfx-seqtools)](https://github.com/jdmacleod/vfx-seqtools/blob/main/LICENSE)
[![Tests Status](https://jdmacleod.github.io/vfx-seqtools/reports/junit/tests-badge.svg)](https://jdmacleod.github.io/vfx-seqtools/reports/junit/report.html) [![Coverage Status](https://jdmacleod.github.io/vfx-seqtools/reports/coverage/coverage-badge.svg)](https://jdmacleod.github.io/vfx-seqtools/reports/coverage/index.html)
[![codecov](https://codecov.io/gh/jdmacleod/vfx-seqtools/branch/main/graph/badge.svg)](https://codecov.io/gh/jdmacleod/vfx-seqtools)

**This is the readme for developers.** The documentation for users is available here: [https://jdmacleod.github.io/vfx-seqtools/](https://jdmacleod.github.io/vfx-seqtools/)

## Prerequisites

You will need [Python](https://www.python.org/) installed. All [Supported versions of Python](https://devguide.python.org/versions/) have been tested to work.

## Quickstart

Install using [pip](https://pypi.org/project/pip/) or [pipx](https://pipx.pypa.io/stable/).

```bash
$ pip install vfx-seqtools
```

or

```bash
$ pipx install vfx-seqtools
```

This will provide the command-line utilities:

- `seqchk` - check frame sequences in the current directory for file consistency. Uses [pillow](https://pypi.org/project/pillow/).
- `seqcp` - copy frames according to provided name patterns and frame range.
- `seqdo` - do command(s), substituting in the provided frame range.
- `seqexp` - expand a frame sequence, to evaluate it visually.
- `seqgen` - given a list of framenumbers, make a frame sequence.
- `seqls` - list frame sequences in the current directory.
- `seqmv` - move (rename) frames according to provided name patterns and frame range.
- `seqrm` - remove (delete) frames according to provided name patterns and frame range.

See the [user documentation](https://jdmacleod.github.io/vfx-seqtools/) for examples.

## Developer Setup

Clone this repository (or fork on GitHub).

In the local repository directory, set up for Python development. The steps below show [Astral's uv](https://docs.astral.sh/uv/) in use - but using Python [venv](https://docs.python.org/3/library/venv.html) is also fine.

```bash
# Create and activate Python virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies with the project set as editable
uv pip install -e ".[dev]"

# Install Git pre-commit hooks
pre-commit install
```

Create a feature branch and make changes. See [TESTS.md](./TESTS.md) for details on running this product's tests.

## Contributing

Contributions to improve these utilities are welcome! Please submit [issues](https://github.com/jdmacleod/vfx-seqtools/issues) and [pull requests](https://github.com/jdmacleod/vfx-seqtools/pulls) on GitHub.

## License

This code is MIT licensed. See the [LICENSE](LICENSE) file for details.

## Reference

- [Ryan Galloway's PySeq library](https://github.com/rsgalloway/pyseq)
- [Geoff Harvey's seqparse library](https://github.com/hoafaloaf/seqparse)
- [Cyril Pichard's filesequence library](https://github.com/cpichard/filesequence)
- [Matt Chambers and Justin Israel's fileseq library](https://github.com/justinfx/fileseq)
- [Matthias Baas' Python Computer Graphics Kit](https://github.com/behnam/cgkit/blob/4b70aed7e0c436287ebcd71aa4362a82965edcb4/utilities/seqls.py)
