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

Copy a sequence of frames to a new location or pattern:

```bash
seqcp render.%04d.exr comped.%04d.exr 1001-1050
```

- Copies frames from `render.1001.exr` to `comped.1001.exr`, etc.

## Do a Command

Run a shell command for each frame in a sequence, substituting `{}` with the frame number:

```bash
seqdo 'echo Processing frame {}' 1001-1005
```

- Prints a message for each frame from 1001 to 1005.

You can use `{src}` and `{dst}` if you specify input/output patterns:

```bash
seqdo 'convert {src} -resize 50% {dst}' input.%04d.jpg output.%04d.jpg 1001-1020
```

## Expand a Sequence

Show all frame numbers represented by a sequence expression:

```bash
seqexp 1001-1010x2
```

- Expands to: `1001 1003 1005 1007 1009`

## Generate a Sequence

Create empty files for a sequence of frames (useful for testing):

```bash
seqgen test.%04d.exr 1001-1005
```

- Creates files: `test.1001.exr` to `test.1005.exr`.

## List Sequences

List all frame sequences in the current directory, grouping files by pattern:

```bash
seqls
```

- Output example:
  ```
  render.%04d.exr: 1001-1050
  comped.%04d.exr: 1001-1050
  ```

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
