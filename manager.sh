#! /bin/bash

cd ~/dummy_forecast

python3 parser.py

python3 message_manager.py

adb shell input keyevent 26
