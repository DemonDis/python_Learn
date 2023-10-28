#! /bin/bash

# set -x

python3.11 -m venv .venv
# python3 -m venv .venv
. .venv/bin/activate

# pip3 install -U pup setuptools wheel

pip3 install -r requirements.txt

# pip install --upgrade pip