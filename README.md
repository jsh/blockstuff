# blockstuff

Trends.

This repo implements [the presentation found here](https://docs.google.com/presentation/d/12iLQT3CsslLkVfdh6Wcb_uhrFeXjC8F2BCFND64iYmM/edit?usp=sharing)

## Installation

See [INSTALL](https://github.com/jsh/blockstuff/blob/master/INSTALL).

## Performance

The pypy3 interpreter will make these scripts run __much__ faster than the standard python3 interpreter.
Right now, all the shebang lines are `#!/usr/bin/env/pypy3`.
If you can, install `pypy3`.
If not, just all the shebang lines to `#!/usr/bin/env python3`.

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

