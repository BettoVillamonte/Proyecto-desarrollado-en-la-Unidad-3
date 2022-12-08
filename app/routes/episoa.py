import requests
'''
url = "https://rickandmortyapi.com/api/episode/2"

datos = requests.get(url).json()


for a in datos['characters']:

    nombres = a

    mirar = requests.get(nombres).json()
    print("Nombre",mirar['name'])
    print("TYPO ",mirar['type'])

    if mirar['location']["url"] == "":
        print("htts:sae")
    else:
        print(mirar['location']["url"])
        localidad = mirar['location']["url"]

    local_dato = requests.get(localidad).json()
    r = requests.get(localidad)

    print(local_dato)
    if r.status_code=="404":
        print("ERROR")
    else:
        print("Dimension : ", local_dato['dimension'])

    print("--------")

'''
from app.modelos.capitulo import Capitulo
from app.db import db



link = "https://rickandmortyapi.com/api/episode/"

for numerador in range(1,52):
    url=link+str(numerador)

    datos = requests.get(url).json()

    for a in datos['characters']:

        nombres = a

        mirar = requests.get(nombres).json()
        nommbre = mirar['name']
        tyypo = mirar['type']
        fotoss = mirar['image']

        if mirar['location']["url"] == "":
            print("htts:sae")
        else:
            mirar['location']["url"]
            localidad = mirar['location']["url"]

        local_dato = requests.get(localidad).json()
        r = requests.get(localidad)

        # print(local_dato)
        if r.status_code == "404":
            print("ERROR")
        else:

            llenado_capitulo = Capitulo(numerador, nommbre, tyypo, local_dato['dimension'], fotoss)

            db.Capitulo.insert_one(llenado_capitulo.to_json())

            # print("Nombre", nommbre, "Typo:", tyypo, "Dimension : ", local_dato['dimension'])

        print("--------")

