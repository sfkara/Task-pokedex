import json

url = "https://raw.githubusercontent.com/zaferelcik/O-T/master/data.json"
response = requests.get(url)

json_verisi = response.json()


# print(json_verisi.get("types").get("name")),"\n",json_verisi["pokemons"],"\n",json_verisi["moves"])

# print(json_verisi["types"])


def type():
    for index in json_verisi["types"]:
        if (a == json_verisi["types"][index]["name"]):
            print("Effective Againist :", json_verisi["types"][index]["effectiveAgainst"])
            print("Weak Againist :", json_verisi["types"][index]["weakAgainst"])


def pokemon_name():
    for index in json_verisi["pokemons"]:
        if (a == json_verisi["pokemons"][0]["name"]):
            print("weights :", json_verisi["pokemons"][0]["Weight"])
            print("heights :", json_verisi["pokemons"][0]["Height"])
            print("Base Attack:", json_verisi["pokemons"][0]["BaseAttack"])
            print("Base Stamina :", json_verisi["types"][0]["BaseStamina"])
            print("Next Evolution :", json_verisi["pokemons"][0]["Next evolution(s)"])


def pokemon_move():
    for index in json_verisi["moves"]:
        if (a == json_verisi["types"][index]["name"]):
            print("id :", json_verisi["moves"][index]["id"])
            print("name :", json_verisi["moves"][index]["name"])
            print("type :", json_verisi["moves"][index]["type"])
            print("damage :", json_verisi["moves"][index]["damage"])
            print("energy :", json_verisi["moves"][index]["energy"])
            print("dps :", json_verisi["moves"][index]["dps"])
            print("duration :", json_verisi["moves"][index]["duration"])
# for index in json_verisi["pokemons"]:
#     print(index)
# for index in json_verisi["moves"]:
