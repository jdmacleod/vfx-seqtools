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

List all files in the current directory, with sequence grouping:

```bash
seqls
```

- Output example:

```bash
./COS_002_0045_comp_NFX_v001.1001-1054#.exr
./meridian.21000-21006,21008@@@@@.tif
./testcp.11-19x2#.tif
./notsequence.tif
```

List only sequences in the current directory:

```bash
seqls -o
```

- Output example:

```bash
./COS_002_0045_comp_NFX_v001.1001-1054#.exr
./meridian.21000-21006,21008@@@@@.tif
./testcp.11-19x2#.tif
```

List only sequences in the current directory, and identify missing frames:

```bash
seqls -o -m
```

- Output example:

```bash
./COS_002_0045_comp_NFX_v001.1001-1054#.exr
./meridian.21000-21006,21008@@@@@.tif
Missing frames: 21007
./testcp.11-19x2#.tif
Missing frames: 0012-0018x2
```

List only files matching "COS*":

```bash
seqls -o -m "COS*"
```

- Output example:

```bash
COS_002_0045_comp_NFX_v001.1001-1054#.exr
```
