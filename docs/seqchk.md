# seqchk

`seqchk` checks image files in a sequence for existence, completeness, and (optionally) validity. This is useful for verifying that all expected frames are present and not corrupt in a VFX or animation pipeline.

## Usage

```bash
seqchk PATTERN [FRAMES]
```

- `PATTERN`: Filename pattern using printf-style formatting (e.g., `render.%04d.exr`).
- `FRAMES`: Frame range or sequence expression (e.g., `1001-1050`, `1-10x2`).

## Options

- `--verbose`, `-v`: Show detailed output for each file.
- `--strict`: Stop on the first error.
- `--quiet`, `-q`: Only print errors.
- `--dry-run`, `-n`: Show what would be checked, but do not actually check files.
- `--version`: Show version and exit.

## Examples

Check for missing or corrupt frames in a typical EXR sequence:

```bash
seqchk render.%04d.exr 1001-1050
```

Check a JPEG sequence with a custom frame range:

```bash
seqchk shotA.%03d.jpg 1-100
```

Check only even frames:

```bash
seqchk comp.%04d.exr 1001-1050x2
```

Show detailed output for each file:

```bash
seqchk --verbose render.%04d.exr 1001-1010
```

## Output

- Reports missing files, unreadable/corrupt files, and a summary of the check.
- Returns a nonzero exit code if any problems are found.

## Typical Use Cases

- Automated QC in render farms.
- Pre-delivery checks for VFX shots.
- Spot-checking sequences after file transfers.
