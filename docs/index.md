# vfx-seqtools

Command-line utilities for working with frame sequences in Animation and VFX.

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vfx-seqtools)](https://pypi.org/project/vfx-seqtools/)
 [![Build Status](https://github.com/jdmacleod/vfx-seqtools/actions/workflows/python-package.yml/badge.svg)](https://github.com/jdmacleod/vfx-seqtools/actions/workflows/python-package.yml)
[![Documentation](https://img.shields.io/badge/doc-latest-blue.svg)](https://jdmacleod.github.io/vfx-seqtools/) [![PyPI - Version](https://img.shields.io/pypi/v/vfx-seqtools)](https://pypi.org/project/vfx-seqtools/)

[![GitHub License](https://img.shields.io/github/license/jdmacleod/vfx-seqtools)](https://github.com/jdmacleod/vfx-seqtools/blob/main/LICENSE)
[![Tests Status](./reports/junit/tests-badge.svg?dummy=8484744)](./reports/junit/report.html)
[![Coverage Status](./reports/coverage/coverage-badge.svg?dummy=8484744)](./reports/coverage/index.html)
[![codecov](https://codecov.io/gh/jdmacleod/vfx-seqtools/branch/main/graph/badge.svg)](https://codecov.io/gh/jdmacleod/vfx-seqtools)

## Prerequisites

You will need [Python](https://www.python.org/) installed - all [supported versions of Python](https://devguide.python.org/versions/) should work.

## Quickstart

Install using [pip](https://pypi.org/project/pip/) or [pipx](https://pipx.pypa.io/stable/).

```bash
$ pip install vfx-seqtools
```

or

```bash
$ pipx install vfx-seqtools
```

This will provide the command-line utilities:

- `seqchk` - check frame sequences in the current directory for file consistency.
- `seqcp` - copy frames according to provided name patterns and frame range.
- `seqdo` - do command(s), substituting in the provided frame range.
- `seqexp` - expand a frame sequence, to evaluate it visually.
- `seqgen` - make a frame sequence from a list of framenumbers.
- `seqls` - list frame sequences in the current directory.
- `seqmv` - move (rename) frames according to provided name patterns and frame range.
- `seqrm` - remove (delete) frames according to provided name patterns and frame range.

## Examples

See [examples.md](./examples.md) for more examples.

## Changes

See the product [Change Log](https://github.com/jdmacleod/vfx-seqtools/blob/main/CHANGELOG.md) on GitHub for a history of changes.

## Problems?

Please submit [issues](https://github.com/jdmacleod/vfx-seqtools/issues) on GitHub.

## Want to contribute?

Details on the GitHub page: [https://github.com/jdmacleod/vfx-seqtools](https://github.com/jdmacleod/vfx-seqtools).
