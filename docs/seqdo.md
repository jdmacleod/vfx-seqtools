# seqdo

`seqdo` runs a shell command for each frame in a sequence, substituting frame numbers and file patterns. This is useful for batch processing or automating per-frame operations.

## Usage

```bash
seqdo COMMAND [SRC_PATTERN] [DST_PATTERN] [FRAMES]
```

- `COMMAND`: The shell command to run. Use `{}` for the frame number, `{src}` and `{dst}` for input/output filenames.
- `SRC_PATTERN`: (Optional) Source filename pattern.
- `DST_PATTERN`: (Optional) Destination filename pattern.
- `FRAMES`: Frame range or sequence expression.

## Options

- `--dry-run`, `-n`: Show what would be done, but do not actually run commands.
- `--thread-count N`: Run up to N commands in parallel.
- `--verbose`, `-v`: Show detailed output for each command.
- `--strict`: Stop on the first error.
- `--quiet`, `-q`: Only print errors.
- `--version`: Show version and exit.

## Examples

Print a message for each frame:

```bash
seqdo 'echo Processing frame {}' 1001-1005
```

Run an image conversion for each frame:

```bash
seqdo 'convert {src} -resize 50% {dst}' input.%04d.jpg output.%04d.jpg 1001-1020
```

Run up to 4 commands in parallel:

```bash
seqdo --thread-count 4 'echo Frame {}' 1-10
```

## Output

- Shows command output and errors for each frame.
- Returns a nonzero exit code if any problems are found.
