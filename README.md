# blockstuff

Trends.

This repo implements [the presentation found here](https://docs.google.com/presentation/d/12iLQT3CsslLkVfdh6Wcb_uhrFeXjC8F2BCFND64iYmM/edit?usp=sharing)

## Installation

See [INSTALL](https://github.com/jsh/blockstuff/blob/master/INSTALL).

## Performance

Right now, shebang lines may be `#!/usr/bin/env pypy3` or `#!/usr/bin/env python3`

The pypy3 interpreter will make these scripts run __much__ faster than the standard python3 interpreter.

If you can, install `pypy3` and make the lines `#!/usr/bin/env pypy3`.
If not, just set the shebang lines to `#!/usr/bin/env python3`.

N.B., At this writing, `pypy3` is back-rev to `python3`, so some functions may only be available with `python3`.
For example, `statistics.harmonic_mean()` is available for both,
but `statistics.fmean()` and `statistics.geometric_mean()` are only available with `python3`.
For some experiments, you may __have__ to use the slower interpreter.

## Overview

### Scripts

- `average_block_count.py`: average block count for random sequences of a given length over repeated trials

- `block_count_dist.py`: distribution of block counts for random sequences of a given length

- `decompose_into_trends.py`: decompose a random sequence into trends

#### Usage

Scripts should all understand `--help`

### Modules

- `blockstuff.py`: a module to manipulate trends/blocks

### Administrative files

- `INSTALL`: How to install this software

- `LICENSE`: An MIT License

- `Makefile`: How to build, lint, test, etc.

- `Pipfile*`: Config files for pipenv

- `README.md`: This file

