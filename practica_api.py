import json
import requests 
import csv 
BASE_URL = "https://swapi.dev/api/people/1/"


""" Función para obtener la información de Luke Skywalker desde la API de Star Wars. 
Pseudocódigo: 
1. Definir la URL base de la API 2.  Establecer el número de página donde se encuentra Luke 
3.  Hacer una solicitud GET a la URL con el número de página 
4. Convertir la respuesta a formato JSON 
5. Para cada personaje en los resultados: - Si el nombre del personaje es 'Luke Skywalker': - Devolver la información del personaje 
6. Si no se encuentra a Luke, devolver None """

def obtener_info_luke(personaje_minuscula):
    BASE_URL = "https://swapi.dev/api/people/1/"
    response = requests.get(BASE_URL)
    response_json = response.json()
    if personaje_minuscula == "luke skywalker":
        return response_json["name"],response_json["mass"],response_json["films"][0]
    else:
        print('Este no es un nombre valido, Ingrese nuevamente "Luke Skywalker"')
    
    
personaje_requerido = input("Cual es el nombre del personaje que estas buscando?")
personaje_minuscula = personaje_requerido.lower()

nombre_personaje, peso_personaje, pelicula1 = obtener_info_luke(personaje_minuscula)

print(f"El nombre del personaje es {nombre_personaje} y el peso del personaje es {peso_personaje} kg, estuvo en peliculas como {pelicula1}")








