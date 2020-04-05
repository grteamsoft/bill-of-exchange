#!/usr/bin/env bash
# The script is used to run the migrations in the application.

set -xeuo pipefail
IFS=$'\n\t'

docker push registry.heroku.com/${HEROKU_APP_NAME}/${HEROKU_DYNONAME}

heroku container:release -a ${HEROKU_APP_NAME} ${HEROKU_DYNONAME}
