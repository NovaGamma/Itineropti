from flask import Flask,jsonify
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
    answer = [{'longitude':point.longitude,'lattitude':point.lattitude} for point in opti]
    return jsonify(data = answer)

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
    app.run(threaded=True, port=5000)
