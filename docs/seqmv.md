# seqmv

`seqmv` renames (moves) a sequence of files from one pattern to another, for a specified frame range. This is useful for versioning, organizing, or retargeting image sequences in VFX/animation workflows.

## Usage

```bash
seqmv SRC_PATTERN DST_PATTERN [FRAMES]
```

- `SRC_PATTERN`: Source filename pattern (e.g., `oldname.####.exr`).
- `DST_PATTERN`: Destination filename pattern (e.g., `newname.####.exr`).
- `FRAMES`: Frame range or sequence expression (e.g., `-f 1001-1020`).

## Options

- `--dry-run`, `-n`: Show what would be moved, but do not actually move files.
- `--interactive`, `-i`: Request confirmation before moving each file.
- `--verbose`, `-v`: Show detailed output for each file.
- `--strict`: Stop on the first error.
- `--version`: Show version and exit.

## Examples

Rename a sequence to a new pattern:

```bash
seqmv oldname.####.exr newname.####.exr -f 1001-1020
```

Preview what would be moved (dry run):

```bash
seqmv -n oldname.####.png newname.####.pnf -f 10-20
```

Interactively copy files, prompting for each copy:

```bash
seqmv -i askfile.####.exr confirmfile.####.exr -f 10-20
```

Move frames 10-20 and offset the destination frame numbering by +10 frames:

```bash
seqmv file.####.exr offsetfile.####+10.exr -f 10-20
```
