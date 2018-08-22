#!/bin/bash
cd ..
cd ..
export FLICK_PATH=$(pwd)

cd $FLICK_PATH/Flick

source $FLICK_PATH/Flick/env/bin/activate
cd flick
celery -A flick worker --loglevel=info --concurrency=10
