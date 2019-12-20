#! /bin/bash

cd ~/Dummy-Forecast

python3 parser.py

python3 message_manager.py

adb shell input keyevent 26
