# seqchk

`seqchk` checks image files for validity. This is useful for verifying that all files present are not corrupt or zero-length.

It doesn't identify missing frames - use [`seqls -m`](./seqls.md) to identify missing frames.

## Usage

```bash
seqchk [PATTERN] [OPTIONS]
```

- `PATTERN`: Optional filename pattern using shell wildcards (for example, `render.*.exr` or `filename.????.tif`).

## Options

- `--verbose`, `-v`: Show detailed output for each file.
- `--only-sequences`, `-o`: Only consider sequences, ignore other files.
- `--strict`: Stop on the first error.
- `--dry-run`, `-n`: Show what would be checked, but do not actually check files.
- `--version`: Show version and exit.

## Examples

Check all files in the current directory:

```bash
seqchk
```

Check only sequence files in the current directory:

```bash
seqchk -o
```

Check a JPEG sequence using a shell wildcard:

```bash
seqchk "shotA.*.jpg"
```

Show line-by-line check output for each file:

```bash
seqchk --verbose "render.*.exr"
```

## Output

- Reports unreadable/corrupt files per sequence checked.
- Returns a nonzero exit code if any problems are found.

## Typical Use Cases

- Automated QC in render farms.
- Pre-delivery checks for VFX shots.
- Spot-checking sequences after file transfers.
