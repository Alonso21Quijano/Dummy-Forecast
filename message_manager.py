import json
import subprocess

with open('client_database.json') as json_file:
    db = json.load(json_file)
    for client in db['Clients']:
        indexes = list(client['Cities_ID'])
        for db_city in db['Cities']:
            if db_city['ID'] in indexes:
                indexes.remove(db_city['ID'])
                msg_file = db_city['name'] + '.' + db_city['country_code'] + '.msg'
                subprocess.call(["./messenger.sh", client['phone'], msg_file])
                
            if not len(indexes):
                break
