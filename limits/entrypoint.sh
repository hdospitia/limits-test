#!/bin/bash

ulimit -n 512

if [ "$1" == 'start' ]; then
	exec python /code/hello-world.py
fi

exec "$@"
