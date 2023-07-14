#!/bin/bash
# Controls the system. Examples:
#
# ./run.sh
# ./run.sh stop
# ./run.sh restart

MYDIR=$(dirname $(realpath "$0"))
cd $MYDIR

if [ ! -e uploads ]; then
    mkdir uploads
    # 1500 es el UID del usuario hackmd dentro del docker
    chown 1500.root uploads
    chmod 700 uploads
fi

if [ -z "$1" ]; then
    docker-compose up -d
else
    docker-compose "$@"
fi
