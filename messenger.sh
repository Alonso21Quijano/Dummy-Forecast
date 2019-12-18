#! /bin/bash

FORECAST_DIR='./forecasts/'
if [ -n "$2" ]
then
	# If screen is off, turn it on and unlock it
	if adb shell dumpsys power | grep -q mWakefulness=Asleep; 
	then
		adb shell input keyevent 26
		sleep 1
	fi

	# Check if sms app is already running and close it if it does
	test=$(adb shell ps | grep com.android.mms | awk '{print "FAIL"}');
	if [ ! -z $test  ]; then
		adb shell am force-stop com.android.mms
	fi

	# Read text from file
	FOLDER='./forecasts/'
	TEXT=$(cat $FOLDER$2)

	# Launch an intent to send an sms with the number and text passed in parameters
	adb shell "NL=$'\n' ;am start -a android.intent.action.SENDTO -d sms:$1 --es sms_body \"$TEXT\" --ez exit_on_sent true"
	sleep 1

	# Press send
	adb shell input keyevent 22
	sleep 1
	adb shell input keyevent 66
	sleep 3
else
	echo "Not enough parameters"
	echo "USAGE: ./messenger.sh phone_number message_text"
fi
