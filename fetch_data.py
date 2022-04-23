import requests
import json

poke_list = []
req = requests.get('http://pokeapi.co/api/v2/pokemon?offset=0&limit=493')
print("HTTP Status Code: " + str(req.status_code))
json_response = json.loads(req.content)
for pokemon in json_response["results"]:
    name = pokemon["name"].capitalize()
    req2 = requests.get('http://pokeapi.co/api/v2/pokemon/' + pokemon["name"])
    json_pokemon = json.loads(req2.content)
    height = json_pokemon['height']
    weight = json_pokemon['weight']
    types= []
    for type in json_pokemon['types']:
        types.append(type['type']['name'])
    if(len(types) < 2 ):
        types.append("single-type")
    species_url =  json_pokemon['species']['url']
    req3 = requests.get(species_url)
    json_species = json.loads(req3.content)
    gen = json_species["generation"]["url"][-2]
    fr_name = json_species["names"][0]["name"]
    for lang in json_species["names"]:
        if(lang["language"]["name"] == "fr"):
            fr_name = lang["name"]
    print(f"{fr_name}")
    output = {
        "name": fr_name,
        "gen": gen,
        "type1" : types[0],
        "type2" : types[1],
        "height" : height,
        "weight" : weight
    }
    poke_list.append(output)

text_file = open("data.json", "w")
 
#write string to file
text_file.write(json.dumps(poke_list))
 
#close file
text_file.close()


poke_list = []
req = requests.get('http://pokeapi.co/api/v2/pokemon?offset=493&limit=405')
print("HTTP Status Code: " + str(req.status_code))
json_response = json.loads(req.content)
for pokemon in json_response["results"]:
    name = pokemon["name"].capitalize()
    req2 = requests.get('http://pokeapi.co/api/v2/pokemon/' + pokemon["name"])
    json_pokemon = json.loads(req2.content)
    height = json_pokemon['height']
    weight = json_pokemon['weight']
    types= []
    for type in json_pokemon['types']:
        types.append(type['type']['name'])
    if(len(types) < 2 ):
        types.append("single-type")
    species_url =  json_pokemon['species']['url']
    req3 = requests.get(species_url)
    json_species = json.loads(req3.content)
    gen = json_species["generation"]["url"][-2]
    fr_name = json_species["names"][0]["name"]
    for lang in json_species["names"]:
        if(lang["language"]["name"] == "fr"):
            fr_name = lang["name"]
    print(f"{fr_name}")
    output = {
        "name": fr_name,
        "gen": gen,
        "type1" : types[0],
        "type2" : types[1],
        "height" : height,
        "weight" : weight
    }
    poke_list.append(output)

text_file = open("data2.json", "w")
 
#write string to file
text_file.write(json.dumps(poke_list))
 
#close file
text_file.close()


poke_list = []
req = requests.get('http://pokeapi.co/api/v2/pokemon?offset=898&limit=194')
print("HTTP Status Code: " + str(req.status_code))
json_response = json.loads(req.content)
for pokemon in json_response["results"]:
    name = pokemon["name"].capitalize()
    req2 = requests.get(pokemon["url"])
    json_pokemon = json.loads(req2.content)
    height = json_pokemon['height']
    weight = json_pokemon['weight']
    types= []
    for type in json_pokemon['types']:
        types.append(type['type']['name'])
    if(len(types) < 2 ):
        types.append("single-type")
    species_url =  json_pokemon['species']['url']
    req3 = requests.get(species_url)
    json_species = json.loads(req3.content)
    gen = json_species["generation"]["url"][-2]
    form_url =  json_pokemon['forms'][0]['url']
    req4 = requests.get(form_url)
    json_form = json.loads(req4.content)
    fr_name = json_form["names"][0]["name"]
    for lang in json_form["names"]:
        if(lang["language"]["name"] == "fr"):
            fr_name = lang["name"]
    print(f"{fr_name}")
    output = {
        "name": fr_name,
        "gen": gen,
        "type1" : types[0],
        "type2" : types[1],
        "height" : height,
        "weight" : weight
    }
    poke_list.append(output)

text_file = open("data3.json", "w")
 
#write string to file
text_file.write(json.dumps(poke_list))
 
#close file
text_file.close()