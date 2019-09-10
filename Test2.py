"""Pokedex"""
import os
import json
from requests import request


def main_menu():
    """Provide interface for finding and viewing pokemon details"""
    select_pokemon = ""
    pokemon_stats = ""


    # Read pokedex from JSON file and parse as list of dictionaries
    pokedex_json = open("pokedex.dat", encoding="utf-8").read()
    pokedex = json.loads(pokedex_json)["pokemon"]

    os.system("cls")
    print("\n                       \033[1mWelcome to the Pokédex!\x1b[0m")
    print("\n                     Generation I (Kanto Reigon)")
    print("                             #001 - #151")

    # Loop until user provides pokemon name that exists in pokedex
    while pokemon_stats == "":
        select_pokemon = input("\n\nWhich Pokémon would you like to see details for?: ").title()
        try:
            pokemon_stats = next(stats for stats in pokedex if stats["name"] == select_pokemon)
        except:
            print("\nNo Pokémon found with the name \"{}\"\n".format(select_pokemon))


# if __name__ == "__main__":
#     os.system("chcp 6501")
#     abspath = os.path.abspath(__file__)
#     dname = os.path.dirname(abspath)
#     os.chdir(dname)

    main_menu()
