#!/usr/bin/bash -eu

# git clone https://github.com/jsh/blockstuff
# cd blockstuff
# git checkout hybrid-oo

sudo apt update
sudo apt upgrade
sudo apt install black ipython3 pypy3 python3-pip
pip3 install --user pipenv
PATH+=:~/.local/bin
sed -i 's/3.9/3.8.5/' Pipfile
pipenv --rm
pipenv --python 3.8
pipenv update
# pipenv install pypy3
pipenv install black ||
  pipenv lock --pre
pipenv shell
