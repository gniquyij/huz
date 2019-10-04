#!/bin/bash
set -e
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pip install -r requirements.txt
wait; echo 'requirements installed'

cd ${here}/prepost/
python pre.py

echo '* * * * * cd '"${here}"'/recorders && /Users/yuqing.ji/.pyenv/versions/3.7.1/envs/huz/bin/python recording.py' > crontmp
crontab crontmp
rm crontmp
