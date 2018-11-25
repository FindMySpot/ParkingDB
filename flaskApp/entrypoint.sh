#!/bin/sh

python querySensor.py &
python reservationChecker.py &
flask run --host=0.0.0.0
