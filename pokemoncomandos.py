import urllib.request, urllib.parse, urllib.error
import json
import ssl

api="https://pokeapi.co/api/v2/pokemon/"


while True:
    pokemon=input("Pokemon: ")
    if len(pokemon)<1: break
    url=api+pokemon
    print(url)
    request = urllib.request.Request(url)
    request.add_header('User-Agent',"cheese")
    datose=urllib.request.urlopen(request)
    data=datose.read().decode()
    print('Retrieved', len(data), 'characters')
    
