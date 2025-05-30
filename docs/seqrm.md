# seqrm

`seqrm` removes (deletes) a sequence of files for a specified frame range. This is useful for cleaning up intermediate or unwanted files in VFX/animation workflows.

## Usage

```bash
seqrm PATTERN [FRAMES]
```

- `PATTERN`: Filename pattern (e.g., `temp.####.exr`).
- `FRAMES`: Frame range or sequence expression (e.g., `-f 1001-1020`).

## Options

- `--dry-run`, `-n`: Show what would be deleted, but do not actually remove files.
- `--interactive`, `-i`: Request confirmation before deleting each file.
- `--verbose`, `-v`: Show detailed output for each file.
- `--strict`: Stop on the first error.
- `--version`: Show version and exit.

## Examples

Remove a sequence of files:

```bash
seqrm temp.####.exr -f 1001-1020
```

Preview what would be deleted (dry run):

```bash
seqrm -n temp.####.exr -f 1-3
```

Interactively remove files, prompting for each copy:

```bash
seqrm -i askfile.####.exr confirmfile.####.exr -f 10-20
```
