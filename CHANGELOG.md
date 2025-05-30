# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - May 29, 2025

### Changed

- Pin `click` to version 8.1.8, as version 8.2 and greater drops support for Python 3.9. Revisit when Python 3.9 reaches end-of-life (est. Oct 2025).
- Update documentation.

## [0.2.0] - May 14, 2025

### Added

- Add exr support using [OpenEXR](https://pypi.org/project/OpenEXR/).
- Add `seqgen` utility to make sequences from lists of framenumbers.

## [0.1.1] - unreleased

### Added

- Add unit tests.

## [0.1.0] - April 28, 2025

### Added

- Add initial version of CLI utilities. `seqchk`, `seqcp`, `seqdo`, `seqexp`, `seqls`, `seqmv`, and `seqrm`.
