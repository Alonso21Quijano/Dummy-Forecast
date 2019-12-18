import requests
import json
import os
import subprocess

key = ''
SEP_SYMB = '/'
with open('config') as config:
    lines = SEP_SYMB.join([string.strip() for string in config.readlines()]) + SEP_SYMB
    key_start = str.find(lines, 'API_KEY')
    key_start = str.find(lines, ':', key_start) + 1
    key_end = str.find(lines, SEP_SYMB, key_start) 
    key = lines[key_start:key_end].strip()

if len(key):

    DAYS = 3

    db_update_flag = False
    query = []
    with open('client_database.json') as json_file:
        db = json.load(json_file)
        indexes = set()
        for client in db['Clients']:
            indexes.update(client['Cities_ID'])
            query.append({'phone' : client['phone'], 'cities': client['Cities_ID']})

        for city in db['Cities']:
            if city['ID'] in indexes:
                indexes.remove(city['ID'])
                city_name = city['name']
                data = {}
                if 'country_code' in city:
                    country_code = city['country_code']
                    res = requests.get("https://api.weatherbit.io/v2.0/forecast/daily",
                                    params={'key': key, 'city':city_name, 'country':country_code, 'lang': 'ru', 'units': 'metric',
                                    'days': DAYS})
                    data = res.json()
                else:
                    res = requests.get("https://api.weatherbit.io/v2.0/forecast/daily",
                                    params={'key': key, 'city':city_name, 'lang': 'ru', 'units': 'metric',
                                    'days': DAYS})
                    data = res.json()

                    db_update_flag = True
                    try:
                        city['country_code'] = data['country_code']
                    except Exception as e:
                        print('Failed to extract data from weatherbit.io')
                        exit()
                try:
                    if city_name != data['city_name']:
                        city['name'] = data['city_name']
                except Exception as e:
                        print('Failed to extract data from weatherbit.io')
                        exit()

                try:
                    message_file = os.path.join('.', 'forecasts', data['city_name'] + '.' + data['country_code'] + '.msg')
                except Exception as e:
                    print('Failed to extract data from weatherbit.io')
                    exit()
                with open(message_file, 'w') as outfile:
                    try:
                        outfile.write('Прогноз погоды на три дня в ' + data['city_name'] + ', ' + data['country_code'] + ':${NL}')
                        for day_fc in data['data']:
                            outfile.write('${NL}' + day_fc['valid_date'] + ':$NL')
                            outfile.write('Температура: ' + '{:+.1f}'.format(day_fc['min_temp']) + ' -- ' + '{:+.1f}'.format(day_fc['max_temp']) + ' C${NL}')
                            outfile.write('Ветер: ' + '{:.1f}'.format(day_fc['wind_spd']) + ' м/с ' + day_fc['wind_cdir']+ '${NL}')
                            outfile.write('Вероятность осадков: ' + str(day_fc['pop']) + '%${NL}')
                    except Exception as e:
                        outfile.write('Failed to create message  :(')
            if not len(indexes):
                break            
    if db_update_flag:
        with open('client_database.json', 'w') as db_json_file:
            json.dump(db, db_json_file, ensure_ascii = False, indent=4)

