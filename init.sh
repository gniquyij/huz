#!/bin/bash
set -e
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pip install -r requirements.txt
wait; echo 'requirements installed'

cd ${here}/prepost/
python pre.py

/etc/init.d/cron start   # docker entrypoint
echo '''
* * * * * cd '${here}'/recorders && '$(which python)' recording.py
@weekly cd '${here}'/recorders && '$(which python)' playback.py weekly
@monthly cd '${here}'/recorders && '$(which python)' playback.py monthly
@yearly cd '${here}'/recorders && '$(which python)' playback.py yearly
''' > crontmp
crontab crontmp
rm crontmp
