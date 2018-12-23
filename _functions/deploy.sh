#!/usr/bin/env bash

# set global default deploy variables
RUNTIME="python37"
REGION="europe-west1"
ENV_FILE="env.yml"
TIMEOUT="30"

# gcloud deploy script function
deploy() {
  # set variables
  function_name="$1"
  function_source="$2"
  function_entry="$3"
  function_runtime="$4"
  function_region="$5"
  function_envfile="$6"
  function_timeout="$7"

  # run gcloud deploy command
  gcloud functions deploy $function_name \
    --source=$function_source \
    --entry-point=$function_entry \
    --runtime=$function_runtime \
    --region=$function_region \
    --env-vars-file=$function_envfile \
    --timeout=$function_timeout \
    --trigger-http

  # echo empty newline
  echo " "
}

# run deploy commands
if [[ "$1" == "all" || "$1" == "spotify-nowplaying" ]]; then
  deploy spotify-nowplaying _spotify  nowplaying $RUNTIME $REGION $ENV_FILE $TIMEOUT
fi
if [[ "$1" == "all" || "$1" == "spotify-topartists" ]]; then
  deploy spotify-topartists _spotify  topartists $RUNTIME $REGION $ENV_FILE $TIMEOUT
fi
if [[ "$1" == "all" || "$1" == "songkick-concerts" ]]; then
  deploy songkick-concerts  _songkick gigography $RUNTIME $REGION $ENV_FILE $TIMEOUT
fi

# show script helper
if [[ "$1" == "" || "$1" == "help" ]]; then
  echo "This script deploys one or more functions"
  echo ""
  echo "Deploy one function ex.   \"$0 function_name\""
  echo "Deploy all functions ex.  \"$0 all\""
fi
