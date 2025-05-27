# seqgen

`seqgen` generates empty files for a sequence of frames, useful for testing or creating placeholder files in VFX/animation workflows.

## Usage

```bash
seqgen PATTERN [FRAMES]
```

- `PATTERN`: Filename pattern (e.g., `test.%04d.exr`).
- `FRAMES`: Frame range or sequence expression (e.g., `1001-1005`).

## Options

- `--dry-run`, `-n`: Show what would be created, but do not actually create files.
- `--verbose`, `-v`: Show detailed output for each file.
- `--strict`: Stop on the first error.
- `--quiet`, `-q`: Only print errors.
- `--version`: Show version and exit.

## Examples

Create empty EXR files for a range:

```bash
seqgen test.%04d.exr 1001-1005
```

Create only even frames:

```bash
seqgen test.%04d.exr 1002-1010x2
```

Preview what would be created (dry run):

```bash
seqgen --dry-run test.%04d.exr 1-3
```
