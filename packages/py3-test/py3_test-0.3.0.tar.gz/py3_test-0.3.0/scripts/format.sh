#!/bin/sh -e
set -x

ruff src tests --fix
black src tests
pyright src tests
find  src tests -name "*.py" -type f |xargs pyupgrade