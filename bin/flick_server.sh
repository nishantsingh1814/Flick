#!/bin/bash

echo $FLICK_PATH
cd $FLICK_PATH/Flick

npm run dev
source $FLICK_PATH/Flick/env/bin/activate
python3 $FLICK_PATH/Flick/flick/manage.py runserver 127.0.0.1:8000
