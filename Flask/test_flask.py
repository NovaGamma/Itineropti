from flask import Flask
import json

app = Flask(__name__)

@app.route('/point/<int:nPoint>')
def hello_world(nPoint):
    array = [i for i in range(nPoint)]
    with open("test.json",'w') as file:
        json.dump(array,file)
    return f'The number of point is {nPoint}'

@app.route('/open')
def open_file():
    with open("test.json",'r') as file:
        data = json.load(file)
    return json.dumps(data)
