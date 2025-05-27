# seqrm

`seqrm` removes (deletes) a sequence of files for a specified frame range. This is useful for cleaning up intermediate or unwanted files in VFX/animation workflows.

## Usage

```bash
seqrm PATTERN [FRAMES]
```

- `PATTERN`: Filename pattern (e.g., `temp.%04d.exr`).
- `FRAMES`: Frame range or sequence expression (e.g., `1001-1020`).

## Options

- `--dry-run`, `-n`: Show what would be deleted, but do not actually remove files.
- `--interactive`, `-i`: Request confirmation before deleting each file.
- `--verbose`, `-v`: Show detailed output for each file.
- `--strict`: Stop on the first error.
- `--quiet`, `-q`: Only print errors.
- `--version`: Show version and exit.

## Examples

Remove a sequence of files:

```bash
seqrm temp.%04d.exr 1001-1020
```

Preview what would be deleted (dry run):

```bash
seqrm --dry-run temp.%04d.exr 1-3
```
