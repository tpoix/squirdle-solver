import json

data_json = open("data.json", "r")
data2_json = open("data2.json", "r")
data3_json = open("data3.json", "r")

data = json.loads(data_json.read())
data2 = json.loads(data2_json.read())
data3 = json.loads(data3_json.read())

if(len(data) == 493):
    print(f"#1 - #493 : OK")
elif(len(data) < 493):
    print(f"#1 - #493 : MISSING POKEMONS, PLEASE RUN fetch_data.py")
else:
    print(f"#1 - #493 : TOO MANY POKEMONS, PLEASE RUN fetch_data.py")
if(len(data2) == 405):
    print(f"#493 - #898 : OK")
elif(len(data2) < 405):
    print(f"#493 - #898 : MISSING POKEMONS, PLEASE RUN fetch_data.py")
else:
    print(f"#493 - #898 : TOO MANY POKEMONS, PLEASE RUN fetch_data.py")
if(len(data2) == 405):
    print(f"Forms : OK")
elif(len(data2) < 405):
    print(f"Forms : MISSING POKEMONS, PLEASE RUN fetch_data.py")
else:
    print(f"Forms : TOO MANY POKEMONS, PLEASE RUN fetch_data.py")

print(f"Total : {len(data) + len(data2) + len(data3)}")


data3_json.close()
data2_json.close()
data_json.close()