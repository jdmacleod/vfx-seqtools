# Examples

This page provides examples using the `vfx-seqtools` command-line utilities with frame sequences. Replace file patterns and frame ranges with those relevant to your project.

- [Examples](#examples)
  - [Check Frames](#check-frames)
  - [Copy Frames](#copy-frames)
  - [Do a Command](#do-a-command)
  - [Expand a Sequence](#expand-a-sequence)
  - [Generate a Sequence](#generate-a-sequence)
  - [List Sequences](#list-sequences)
  - [Rename a Sequence](#rename-a-sequence)
  - [Remove a Sequence](#remove-a-sequence)

## Check Frames

Check all files in the current directory:

```bash
seqchk
```

Check files in the current directory matching "COS*" as a sequence:

```bash
seqchk "COS*"
```

See [seqchk](./seqchk.md) for even more examples.

## Copy Frames

Copy frames 1001-1050 from `render.####.exr` to `comped.####.exr`:

```bash
seqcp render.####.exr comped.####.exr -f 1001-1050
```

Copy even frames in the range 1-10 from `animtexture.@.exr` to `animoffset.@.exr`, with a +10 frame offset:

```bash
seqcp animtexture.@.exr animoffset.@+10.exr -f 1-10x2
```

See [seqcp](./seqcp.md) for even more examples.

## Do a Command

Run a shell command for each frame in a sequence, substituting `@` with the frame number:

```bash
seqdo 'echo Processing frame @' -f 1001-1005
```

See [seqdo](./seqdo.md) for even more examples.

## Expand a Sequence

List all frame numbers represented by a sequence expression:

```bash
seqexp 1001-1010x2
```

- Expands to: `1001 1003 1005 1007 1009`

See [seqexp](./seqexp.md) for even more examples.

## Generate a Sequence

Create a sequence expression from a list of frames:

```bash
seqgen "1 2 3 4 5"
```

- Output: `1-5`

See [seqgen](./seqgen.md) for even more examples.

## List Sequences

List all files in the current directory, grouping files by sequence:

```bash
seqls
```

- Output example:

```bash
render.1001-1050#.exr
comped.1001-1050#.exr
```

See [seqls](./seqls.md) for even more examples.

## Rename a Sequence

Rename (move) a sequence of files to a new pattern:

```bash
seqmv oldname.%04d.exr newname.%04d.exr 1001-1020
```

- Moves `oldname.1001.exr` to `newname.1001.exr`, etc.

## Remove a Sequence

Delete a sequence of files from disk:

```bash
seqrm temp.%04d.exr 1001-1020
```

- Removes `temp.1001.exr` to `temp.1020.exr`.
