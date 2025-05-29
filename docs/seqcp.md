# seqcp

`seqcp` copies a sequence of files from one pattern to another, for a specified frame range. This is useful for duplicating or versioning image sequences in VFX/animation workflows.

## Usage

```bash
seqcp SRC_PATTERN DST_PATTERN [FRAMES]
```

- `SRC_PATTERN`: Source filename pattern (e.g., `render.#.exr`).
- `DST_PATTERN`: Destination filename pattern (e.g., `comped.#.exr`).
- `FRAMES`: Frame range or sequence expression (e.g., `-f 1001-1050`).

## Options

- `--dry-run`, `-n`: Show what would be copied, but do not actually copy files.
- `--interactive`, `-i`: Request confirmation before copying each file.
- `--verbose`, `-v`: Show detailed output for each file.
- `--strict`: Stop on the first error.
- `--version`: Show version and exit.

## Examples

Copy a sequence from one pattern to another:

```bash
seqcp render.####.exr comped.####.exr -f 1001-1050
```

Copy only odd frames in the range 1-100 (for example, 1, 3, 5, 7, ...):

```bash
seqcp input.####.jpg output.####.jpg -f 1-100x2
```

Preview what would be copied (dry run):

```bash
seqcp -n somefile.@.png anotherfile.@.png -f 10-20
```

Interactively copy files, prompting for each copy:

```bash
seqcp -i askfile.####.exr confirmfile.####.exr -f 10-20
```

Copy frames 10-20 and offset the destination frame numbering by +10 frames:

```bash
seqcp file.####.exr offsetfile.####+10.exr -f 10-20
```

## Output

- Reports files copied, skipped, or failed.
- Returns a nonzero exit code if any problems are found.
