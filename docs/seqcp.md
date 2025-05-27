# seqcp

`seqcp` copies a sequence of files from one pattern to another, for a specified frame range. This is useful for duplicating or versioning image sequences in VFX/animation workflows.

## Usage

```bash
seqcp SRC_PATTERN DST_PATTERN [FRAMES]
```

- `SRC_PATTERN`: Source filename pattern (e.g., `render.%04d.exr`).
- `DST_PATTERN`: Destination filename pattern (e.g., `comped.%04d.exr`).
- `FRAMES`: Frame range or sequence expression (e.g., `1001-1050`).

## Options

- `--dry-run`, `-n`: Show what would be copied, but do not actually copy files.
- `--interactive`, `-i`: Request confirmation before copying each file.
- `--verbose`, `-v`: Show detailed output for each file.
- `--strict`: Stop on the first error.
- `--quiet`, `-q`: Only print errors.
- `--version`: Show version and exit.

## Examples

Copy a sequence from one pattern to another:

```bash
seqcp render.%04d.exr comped.%04d.exr 1001-1050
```

Copy only odd frames:

```bash
seqcp input.%04d.jpg output.%04d.jpg 1-100x2
```

Preview what would be copied (dry run):

```bash
seqcp --dry-run a.%04d.png b.%04d.png 10-20
```

## Output

- Reports files copied, skipped, or failed.
- Returns a nonzero exit code if any problems are found.
