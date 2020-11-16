# blockstuff

Trends.

This repo implements [the presentation found here](https://docs.google.com/presentation/d/12iLQT3CsslLkVfdh6Wcb_uhrFeXjC8F2BCFND64iYmM/edit?usp=sharing)

## Installation

See [INSTALL](https://github.com/jsh/blockstuff/blob/master/INSTALL).

## Performance

To improve performance (substantially), install `pypy3` and change all shebang lines from `#!/usr/bin/env python` to `#!/usr/bin/env/pypy3`

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

