#!/bin/bash
export FLICK_PATH=$(pwd)

cd /home/vagrant/www/Flick
npm install
npm run dev
source $FLICK_PATH/Flick/env/bin/activate
python $FLICK_PATH/Flick/flick/manage.py runserver 127.0.0.1:8000
