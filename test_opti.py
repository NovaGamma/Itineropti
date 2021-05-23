import requests

base_url = "https://itineroptiapp.herokuapp.com/address/"
#base_url = "http://127.0.0.1:5000/address/"
url = base_url + "13 rue général Pershing Versailles|181 rue Alésia Paris"
with requests.get(url) as r:
    print(r.text)
