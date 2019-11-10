#!/bin/bash
set -e
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pip install -r ${here}/../requirements.txt
wait; echo 'requirements installed'

cd ${here}
python init.py main all

echo '''
*/10 * * * * cd '${here}'/../recorders && '$(which python)' recording.py
*/10 * * * * cd '${here}'/../recorders && '$(which python)' playback.py
''' > crontmp
crontab crontmp
rm crontmp
