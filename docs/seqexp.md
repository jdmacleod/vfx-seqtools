# seqexp

`seqexp` expands a sequence expression into a list of frame numbers. Useful for visualizing or debugging frame ranges in VFX/animation workflows.

## Usage

```bash
seqexp SEQUENCE
```

- `SEQUENCE`: Frame range or sequence expression (e.g., `1001-1050`, `1-10x2`).

## Options

- `--version`: Show version and exit.

## Examples

Expand a simple range:

```bash
seqexp 1001-1005
```

- Output: `1001 1002 1003 1004 1005`

Expand a range with step:

```bash
seqexp 1001-1010x2
```

- Output: `1001 1003 1005 1007 1009`

Expand a complex sequence:

```bash
seqexp 1-5,10-12
```

- Output: `1 2 3 4 5 10 11 12`
