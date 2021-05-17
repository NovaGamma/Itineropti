from flask import Flask
import json
import Point
from get_coord import get_coords

app = Flask(__name__)

@app.route('/point/<int:nPoint>')
def hello_world(nPoint):
    array = [i for i in range(nPoint)]
    with open("test.json",'w') as file:
        json.dump(array,file)
    return f'The number of point is {nPoint}'

@app.route('/address/<string:addresses>')
def itineropty(addresses):
    adresses = addresses.split('|')
    coords = get_coords(points = adresses)
    opti = Point.main(coords)
    text = ""
    for point in opti:
        text += str(point) + "|"
    return text[:-1]

@app.route('/open')
def open_file():
    with open("test.json",'r') as file:
        data = json.load(file)
    return json.dumps(data)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000,ssl_context='adhoc')
