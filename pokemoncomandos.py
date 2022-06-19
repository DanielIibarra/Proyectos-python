import urllib.request, urllib.parse, urllib.error
import json

api="https://pokeapi.co/api/v2/pokemon/"

while True:
    pokemon=input("Pokemon: ")
    if len(pokemon)<1: 
        break
