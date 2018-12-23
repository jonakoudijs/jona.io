#!/usr/bin/env bash

# set required variables
ENV_FILE="env.yml"

# export all environment variables for testing
while read line; do
  # set delimiter/seperator
  IFS=': '

  # skip empty lines
  if [ "$line" != "" ]; then
    # read line into array as seperated key/value
    read -ra ADDR <<< "$line"
    # export environment variable
    export ${ADDR[0]}=${ADDR[1]}
  fi
done <$ENV_FILE

# execute functions
