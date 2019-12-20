import json
from pathlib import Path

NAME = 'client_database.json'

def findmaxID(data, area):
    IDs = list(range(len(data[area]) + 1))
    for unit in data[area]:
        if unit['ID'] <  IDs[-1]:
            IDs.remove(unit['ID'])
    return IDs[0]

def add_city(name, city, *countrycode):
    path = Path(name)
    data = json.loads(path.read_text(encoding='utf-8'))
    ID = findmaxID(data, 'Cities')
    if len(countrycode) == 0:
        data['Cities'].append({'ID': ID, 'name': city})
    else:
        data['Cities'].append({'ID': ID, 'name': city,'country_code':countrycode[0]})
    path.write_text(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')), encoding='utf-8')

def remove_city(name, city_ID):
    path = Path(name)
    data = json.loads(path.read_text(encoding='utf-8'))
    for city in data['Cities']:
        if city['ID'] == city_ID:
            data['Cities'].remove(city)
    path.write_text(json.dumps(data, sort_keys=True, indent=4, ensure_ascii = False, separators=(',', ': ')), encoding='utf-8')

def add_client(name, phone, cities_id, *client_name):
    path = Path(name)
    data = json.loads(path.read_text(encoding='utf-8'))
    ID = findmaxID(data, 'Clients')
    if len(client_name) == 0:
        data['Clients'].append({'Cities_ID':cities_id, 'ID': ID, 'phone': phone})
    else:
        data['Clients'].append({'Cities_ID':cities_id, 'ID': ID, 'name': client_name[0], 'phone': phone})
    path.write_text(json.dumps(data, sort_keys=True, indent=4, ensure_ascii = False, separators=(',', ': ')), encoding='utf-8')

def remove_client(name, client_ID):
   path = Path(name)
   data = json.loads(path.read_text(encoding='utf-8'))
   for client in data['Clients']:
       if client['ID'] == client_ID:
           data['Clients'].remove(client)
   path.write_text(json.dumps(data, sort_keys=True, indent=4, ensure_ascii = False, separators=(',', ': ')), encoding='utf-8')

if __name__ == "__main__":
    print("Welcome to db_assistant")
    while True:
        print("What would you like to do now?")
        print("'a_ci' --  add city \t 'r_ci'-remove city")
        print("'a_cl' --  add client \t 'r_cl'-remove client")
        print("'s' -- show database\t 'x' -- exit")
        command = input().split()
        if len(command):
            if command[0] == 'a_ci':
                if len(command) == 1:
                    print("Add city: Please specify city name and country_code(optionaly)")
                    command = input().split()
                else:
                    command = command[1:]
                if len(command) > 1:
                    try:
                        add_city(NAME, command[0], command[1])
                    except Exception as e:
                        print("Something went wrong")
                elif len(command):
                    try:
                        add_city(NAME, command[0])
                    except Exception as e:
                        print("Something went wrong")
                else:
                    print('Canceled')
            elif command[0] == 'r_ci':
                if len(command) == 1:
                    print("Remove city: Please specify city ID")
                    command = input().split()
                else:
                    command = command[1:]
                if len(command):
                    try:
                        remove_city(NAME, int(command[0]))
                    except Exception as e:
                        print("Something went wrong")
                else:
                    print('Canceled')
            elif command[0] == 'a_cl':
                if len(command) == 1:
                    print("Add client: Please specify client phone, city IDs and name(optionaly)")
                    command = input().split()
                else:
                    command = command[1:]
                if len(command) > 1:
                    try:
                        int(command[-1])
                        add_client(NAME, command[0], command[1:])
                    except Exception as e:
                        add_client(NAME, command[0], command[1:-1], command[-1])
                else:
                    print('Canceled')
            elif command[0] == 'r_cl':
                if len(command) == 1:
                    print("Remove client: Please specify client ID")
                    command = input().split()
                else:
                    command = command[1:]
                if len(command):
                    try:
                        remove_client(NAME, int(command[0]))
                    except Exception as e:
                        print("Something went wrong")
                else:
                    print('Canceled')
            elif command[0] == 's':
                path = Path(NAME)
                data = json.loads(path.read_text(encoding='utf-8'))
                print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii = False))
            elif command[0] == 'x':
                print("EXIT")
                break
            else:
                print("Sorry. Don't understand")
