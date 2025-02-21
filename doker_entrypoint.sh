#!/bin/bash
set -e

if [ "$1" = 'start' ]; then
    # Start the application
    exec bash /app/start.sh
else
    exec "$@"
fi