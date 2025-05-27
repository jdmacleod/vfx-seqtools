# seqmv

`seqmv` renames (moves) a sequence of files from one pattern to another, for a specified frame range. This is useful for versioning, organizing, or retargeting image sequences in VFX/animation workflows.

## Usage

```bash
seqmv SRC_PATTERN DST_PATTERN [FRAMES]
```

- `SRC_PATTERN`: Source filename pattern (e.g., `oldname.%04d.exr`).
- `DST_PATTERN`: Destination filename pattern (e.g., `newname.%04d.exr`).
- `FRAMES`: Frame range or sequence expression (e.g., `1001-1020`).

## Options

- `--dry-run`, `-n`: Show what would be moved, but do not actually move files.
- `--interactive`, `-i`: Request confirmation before moving each file.
- `--verbose`, `-v`: Show detailed output for each file.
- `--strict`: Stop on the first error.
- `--quiet`, `-q`: Only print errors.
- `--version`: Show version and exit.

## Examples

Rename a sequence to a new pattern:

```bash
seqmv oldname.%04d.exr newname.%04d.exr 1001-1020
```

Preview what would be moved (dry run):

```bash
seqmv --dry-run a.%04d.png b.%04d.png 10-20
```
