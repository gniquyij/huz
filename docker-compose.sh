#!/bin/bash

docker-compose up -d
wait; docker exec -it huz_main /bin/bash init.sh
