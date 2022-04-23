import json
import random
from colorama import Back

data_json = open("data.json", "r")
data2_json = open("data2.json", "r")
data3_json = open("data3.json", "r")

data = json.loads(data_json.read())
data2 = json.loads(data2_json.read())
data3 = json.loads(data3_json.read())

total_data = data + data2 + data3

nom = input("Quel Pokémon ?\n")

def garder(x, attribut, qt, supinf = "sup"):
    if(attribut == "type1" or attribut == "type2"):
        return [i for i in x if i[attribut] == qt]
    elif(attribut == "gen" or attribut=="weight" or attribut=="height"):
        if(supinf == "sup"):
            return [i for i in x if i[attribut] > qt]
        elif(supinf == "inf"):
            return [i for i in x if i[attribut] < qt]
        else:
            return [i for i in x if i[attribut] == qt]
    else:
        return 0

def exclure(x, attribut, qt, supinf = "sup"):
    if(attribut == "type1" or attribut == "type2"):
        return [i for i in x if i[attribut] != qt]
    elif(attribut == "gen" or attribut=="weight" or attribut=="height"):
        if(supinf == "sup"):
            return [i for i in x if i[attribut] < qt]
        elif(supinf == "inf"):
            return [i for i in x if i[attribut] > qt]
        else:
            return [i for i in x if i[attribut] != qt]
    else:
        return 0

def exclure_pokemon(x, pokemon):
    return [i for i in x if i["name"] != pokemon]

results = [i for i in total_data if i["name"]==nom]
for poke in results:
    print(f"\nNom: {poke['name']}")
    print(f"Gen    : {poke['gen']}")
    print(f"Type 1 : {poke['type1']}")
    print(f"Type 2 : {poke['type2']}")
    print(f"Height : {poke['height']/10}m")
    print(f"Weight : {poke['weight']/10}kg")
print("\n")
guess = random.choice(total_data)
i = 0

while(guess['name'] != results[0]["name"]):
    gen_print = Back.GREEN + '✓' + Back.RESET
    type_1_print = Back.GREEN + '✓' + Back.RESET
    type_2_print = Back.GREEN + '✓' + Back.RESET
    height_print = Back.GREEN + '✓' + Back.RESET
    weight_print = Back.GREEN + '✓' + Back.RESET

    if(guess["gen"] > results[0]["gen"]):
        gen_print = Back.BLUE + '▼' + Back.RESET
        total_data = garder(total_data, "gen", guess["gen"], "inf")
    if(guess["gen"] < results[0]["gen"]):
        gen_print = Back.BLUE + '▲' + Back.RESET
        total_data = garder(total_data, "gen", guess["gen"], "sup")
    elif(guess["gen"] == results[0]["gen"]):
        total_data = garder(total_data, "gen", guess["gen"], "egal")
    print(f"Elements après nettoyage de gen    : \t{len(total_data)}")
    if(guess["type1"] != results[0]["type1"]):
        type_1_print = Back.RED + 'X' + Back.RESET
        total_data = exclure(total_data, "type1", guess["type1"])
    elif(guess["type1"] == results[0]["type1"]):
        total_data = garder(total_data, "type1", guess["type1"])
    if(guess["type1"] == results[0]["type2"]):
        type_1_print = Back.YELLOW + '⬌' + Back.RESET  
        total_data = garder(total_data, "type2", guess["type1"])
    print(f"Elements après nettoyage de type1  : \t{len(total_data)}")
    if(guess["type2"] != results[0]["type2"]):
        type_2_print = Back.RED + 'X' + Back.RESET
        total_data = exclure(total_data, "type2", guess["type2"])
    elif(guess["type2"] == results[0]["type2"]):
        total_data = garder(total_data, "type2", guess["type2"])
    if(guess["type2"] == results[0]["type1"]):
        type_1_print = Back.YELLOW + '⬌' + Back.RESET
        total_data = garder(total_data, "type1", guess["type2"])
    print(f"Elements après nettoyage de type2  : \t{len(total_data)}")
    if(guess["height"] > results[0]["height"]):
        height_print = Back.BLUE + '▼' + Back.RESET
        total_data = garder(total_data, "height", guess["height"], "inf")
    if(guess["height"] < results[0]["height"]):
        height_print = Back.BLUE + '▲' + Back.RESET
        total_data = garder(total_data, "height", guess["height"], "sup")
    elif(guess["height"] == results[0]["height"]):
        total_data = garder(total_data, "height", guess["height"], "egal")
    print(f"Elements après nettoyage de height : \t{len(total_data)}")
    if(guess["weight"] > results[0]["weight"]):
        weight_print = Back.BLUE + '▼' + Back.RESET
        total_data = garder(total_data, "weight", guess["weight"], "inf")
    if(guess["weight"] < results[0]["weight"]):
        weight_print = Back.BLUE + '▲' + Back.RESET
        total_data = garder(total_data, "weight", guess["weight"], "sup")
    elif(guess["weight"] == results[0]["weight"]):
        total_data = garder(total_data, "weight", guess["weight"], "egal")
    print(f"Elements après nettoyage de weight : \t{len(total_data)}")
    total_data = exclure_pokemon(total_data, guess["name"])
    print(f"{'{0: <20}'.format(guess['name'])}\t{gen_print} {type_1_print} {type_2_print} {height_print} {weight_print}")
    print(f"Elements restants : {len(total_data)}")
    guess = random.choice(total_data)
    i += 1

print(f"{'{0: <20}'.format(guess['name'])}\t{Back.GREEN + '✓' + Back.RESET} {Back.GREEN + '✓' + Back.RESET} {Back.GREEN + '✓' + Back.RESET} {Back.GREEN + '✓' + Back.RESET} {Back.GREEN + '✓' + Back.RESET}")
i += 1
print(f"Trouvé !")
print(f"\nEssais : {i}")

data2_json.close()
data_json.close()