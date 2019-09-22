#!/bin/bash
set -e
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

exec $SHELL
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv activate huz
cd ${here}/utils/
python hzonitor.py
