#!/bin/bash
set -e
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pip install -r requirements.txt
wait; echo 'requirements installed'

cd ${here}/prepost/
python pre.py

echo '''
* * * * * cd '${here}'/recorders && '$(which python)' recording.py
* * * * * cd '${here}'/recorders && '$(which python)' playback.py
''' > crontmp
crontab crontmp
rm crontmp
