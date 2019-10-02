import json

def leer_json():
    with open('config.json') as contenido:
        poop = json.load(contenido)
        print poop

leer_json()

