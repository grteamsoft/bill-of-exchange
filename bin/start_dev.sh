#!/usr/bin/env bash
# The script is used to run the application on dev environment.

set -xeuo pipefail
IFS=$'\n\t'

cd "$( dirname "${BASH_SOURCE[0]}" )"

# Waiting for all the dependent services running.
# @todo Change it to readiness probe to all the services it depends on.
sleep 3;

./migrate.sh

watchmedo auto-restart \
  --recursive \
  --pattern="*.py" \
  --directory="/app" \
  python -- /app/app/server.py