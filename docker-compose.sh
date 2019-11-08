#!/bin/bash

while getopts 's:i:' opt
do
    case ${opt} in
    s) scope=${OPTARG};;
    i) input=${OPTARG};;
    *) echo ${opt}' is not an option';;
    esac
done

docker-compose up -d; sleep 30;
if [[ ${scope} == 'src' ]];
then
    export src=${input}
    docker exec -it huz_main /bin/bash bin/update.sh
else
    docker exec -it huz_main /bin/bash bin/init.sh
fi
