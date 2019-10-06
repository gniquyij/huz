#!/bin/bash
set -e
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pip install -r requirements.txt
wait; echo 'requirements installed'

cd ${here}/prepost/
python pre.py

echo '''
* * * * * cd '"${here}"'/recorders && /usr/local/bin/python recording.py
@weekly cd '"${here}"'/recorders && /usr/local/bin/python playback.py weekly
@monthly cd '"${here}"'/recorders && /usr/local/bin/python playback.py monthly
@yearly cd '"${here}"'/recorders && /usr/local/bin/python playback.py yearly
''' > crontmp
crontab crontmp
rm crontmp
