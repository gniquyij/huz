#!/bin/bash
set -e
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pip install -r requirements.txt
wait; echo 'requirements installed'

cd ${here}/prepost/
python pre.py

crontab -l | { cat; echo '* * * * * '"${here}"'/hzonitor.sh'; } | crontab -
