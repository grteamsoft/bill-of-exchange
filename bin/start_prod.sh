#!/usr/bin/env bash
# The script is used to run the application on production environment.

set -xeuo pipefail
IFS=$'\n\t'

cd "$( dirname "${BASH_SOURCE[0]}" )"

python -- /app/app/server.py
