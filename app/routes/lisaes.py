import requests





for a in range(1,22):
    url ="https://rickandmortyapi.com/api/character?page="+str(a)
    datos = requests.get(url).json()

    for a in datos['results']:
        print(a)




