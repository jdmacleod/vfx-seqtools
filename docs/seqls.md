# seqls

`seqls` lists all frame sequences in the current directory, grouping files by pattern. This is useful for quickly seeing what sequences are present in a shot or render folder.

## Usage

```bash
seqls
```

## Options

- `--missing-frames`, `-m`: List missing frames from sequences.
- `--only-sequences`, `-o`: Only consider sequences, ignore other files.
- `--version`: Show version and exit.

## Examples

List all sequences in the current directory:

```bash
seqls
```

- Output example:
  ```
  render.%04d.exr: 1001-1050
  comped.%04d.exr: 1001-1050
  ```
