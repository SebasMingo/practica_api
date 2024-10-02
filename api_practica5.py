import requests
import json
import csv
import argparse

def buscar(input_personaje):
    url = "https://swapi.dev/api/people/"
    response = requests.get(url)
    data = response.json()
    personajes = data["results"]
    for personaje in personajes:
        if personaje["name"] == input_personaje:
            return personaje["name"]

input_personaje = input("A que personaje estas buscando?\n")
person = buscar(input_personaje)
print(f"El personaje es {person}")
    