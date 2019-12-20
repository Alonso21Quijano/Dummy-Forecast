import json
import subprocess

with open('client_database.json') as json_file:
    db = json.load(json_file)
    for client in db['Clients']:
        try:
            indexes = list(map(int, client['Cities_ID']))
            for db_city in db['Cities']:
                if int(db_city['ID']) in indexes:
                    indexes.remove(db_city['ID'])
                    msg_file = db_city['name'] + '.' + db_city['country_code'] + '.msg'
                    try:
                        subprocess.call(["./messenger.sh", client['phone'], msg_file])
                    except Exception as e:
                        print("failed to send sms to",  client['phone'])
                    
                if not len(indexes):
                    break
        except Exception as e:
                        print("problem with client",  client['phone'])
