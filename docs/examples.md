# Examples

Examples of using `noc` to interact with [Netflix Open Content](https://opencontent.netflix.com/) media.

- [Examples](#examples)
  - [Check Frames](#check-frames)
  - [Copy Frames](#copy-frames)
  - [Do a command](#do-a-command)
    - [Expand a sequence](#expand-a-sequence)
    - [List Sequences](#list-sequences)
    - [Rename a Sequence](#rename-a-sequence)
    - [Remove a Sequence](#remove-a-sequence)

## Check Frames

Check a sequence to see if the files are good.

```bash
seqchk
```

## Copy Frames

Copy frames from one name to another.

```bash
seqcp
```

## Do a command

Do a command, substituting in a frame number for every frame in a sequence.

```bash
seqdo
```

### Expand a sequence

Expand a sequence, to see the list of frames it represents.

```bash
seqexp
```

### List Sequences

List files, grouping them into sequences for readability.

```bash
seqls
```

### Rename a Sequence

Rename (move) files from one name to another, for every frame in a sequence.

```bash
seqmv
```

### Remove a Sequence

Remove (delete) files from disk, for every frame in a sequence.

```bash
seqrm
```
