import requests

url = "https://itineroptiapp.herokuapp.com/address/4 rue Isabeau de Bavières 94240 L'Haÿ-Les-Roses|40 rue Antoine de St Exupéry 94320 Thiais|290 rue de la cote st Jean Villainnes-Sur-Seine 78670|13 Rue Général Pershing Versailles 78000"

with requests.get(url) as r:
    print(r.text)
