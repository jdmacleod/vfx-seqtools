# seqgen

`seqgen` generates a sequence expression from a list of framenumbers. Useful for visualizing or debugging frame ranges in VFX/animation workflows.

Complements [seqexp](./seqexp.md)

## Usage

```bash
seqgen [FRAMES]
```

- `FRAMES`: Frames to consider for a sequence expression (for example, `1,2,3,4,5`).

## Options

- `--version`: Show version and exit.

## Examples

Generate a sequence from a space-separated list of frames:

```bash
seqgen "1 2 3 4 5"
```

```bash
1-5
```

Generate a sequence from a comma-separated list of frames:

```bash
seqgen 5,10,15,20
```

```bash
5-20x5
```
