# Tests

Tests for this product are set up with `pytest`.

## Run Tests With `pytest`

```bash
$ pytest
..................................                                                                                                [100%]
34 passed in 0.18s
```

## Run Tests and Display Code Coverage

```bash
$ pytest --cov=vfx_seqtools
...............                                                                                                                                                                                                        [100%]
============================================================ tests coverage =============================================================
___________________________________________ coverage: platform darwin, python 3.11.12-final-0 ___________________________________________

Name                                   Stmts   Miss  Cover
----------------------------------------------------------
src/vfx_seqtools/__init__.py               2      0   100%
src/vfx_seqtools/actions/__init__.py       0      0   100%
src/vfx_seqtools/actions/seqchk.py        57     57     0%
src/vfx_seqtools/actions/seqcp.py         56     56     0%
src/vfx_seqtools/actions/seqdo.py         49     49     0%
src/vfx_seqtools/actions/seqexp.py        18      0   100%
src/vfx_seqtools/actions/seqls.py         19     19     0%
src/vfx_seqtools/actions/seqmv.py         56     56     0%
src/vfx_seqtools/actions/seqrm.py         54     54     0%
src/vfx_seqtools/common_options.py        43     13    70%
src/vfx_seqtools/decorators.py            32      2    94%
src/vfx_seqtools/parser.py                25      0   100%
src/vfx_seqtools/seqchk_cli.py             6      6     0%
src/vfx_seqtools/seqcp_cli.py              6      6     0%
src/vfx_seqtools/seqdo_cli.py              6      6     0%
src/vfx_seqtools/seqexp_cli.py             6      1    83%
src/vfx_seqtools/seqls_cli.py              6      6     0%
src/vfx_seqtools/seqmv_cli.py              6      6     0%
src/vfx_seqtools/seqrm_cli.py              6      6     0%
----------------------------------------------------------
TOTAL                                    453    343    24%
```

## Run Tests and Generate Code Coverage HTML Report

```bash
$ pytest --cov=vfx_seqtools --cov-report=html
..................................                                                                                                [100%]
============================================================ tests coverage =============================================================
___________________________________________ coverage: platform darwin, python 3.11.12-final-0 ___________________________________________

Coverage HTML written to dir htmlcov
34 passed in 0.47s
```

Open ./htmlcov/index.html in a web browser to inspect details of the test results.
