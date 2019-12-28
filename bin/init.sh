#!/bin/bash
set -e
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pip install -r ${here}/../requirements.txt
wait; echo 'requirements installed'

apt install -y s3fs
echo ${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY} > /etc/passwd-s3fs
chmod 600 /etc/passwd-s3fs
s3fs huz ${here}/../src -o passwd_file=/etc/passwd-s3fs -o nonempty -o url=https://s3-ap-northeast-1.amazonaws.com

cd ${here}
python init.py main all

echo '''
*/10 * * * * cd '${here}'/../recorders && '$(which python)' recording.py
*/10 * * * * cd '${here}'/../recorders && '$(which python)' playback.py
''' > crontmp
crontab crontmp
rm crontmp
