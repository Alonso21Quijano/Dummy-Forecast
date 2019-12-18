Dummy Forecast Messenger
========================

This program is designed to send sms containing 3 day's weatherforecast to clients from database.

REQUIREMENTS
------------

This program uses Android phone connected over USB to Your PC, so make sure that You have both =)
The program communicate with a phone via [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb). You need to turn on the Developer options and enable USB debugging to run this program.

Getting Started
---------------

1. Make sure you've [installed adb](https://developer.android.com/studio/releases/platform-tools.html#downloads)

2. [Enable USB debugging](https://developer.android.com/studio/command-line/adb#Enabling) on Your device

3. Sign up on https://www.weatherbit.io/ and get personal API key

4. Put "API_KEY: *your_key*" in the `config` file

5. Fill `client_database.json` file. It has the next structure:
```python
{
    "Cities": [
        {
            "ID": city ID,
            "name": City name,
            "country_code": weatherbit's country code(optional)
        },
	...
    ],
    "Clients": [
        {
            "ID": client ID,
            "name": client name(optional),
            "phone": client phone,
            "Cities_ID": [
                client cities ID,
		....
            ]
        },
	...
    ]
}
```

6. Launch manager.sh to run program

7. Optionally You may put manager.sh in chron or other task manager to send sms regularly and automatically!

