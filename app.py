from flask import Flask, jsonify, request

from flask_sqlalchemy import SQLAlchemy

import os

from model import *
from schemas import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/super_simple")
def super_simple():
    return jsonify(message=f'Hello from the planetary API.'), 200

@app.route("/not_found")
def not_found():
    return jsonify(message='That resource was not found'), 404

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = request.args.get('age')
    if int(age) < 18:
        return jsonify(message=f'Sorry, {name}, you are not old enough !'), 401
    else:
        return jsonify(message=f'Welcome {name}, you are old enough !'), 200
    
@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if int(age) < 18:
        return jsonify(message=f'Sorry, {name}, you are not old enough !'), 401
    else:
        return jsonify(message=f'Welcome {name}, you are old enough !'), 200
    

@app.route('/planets', methods=["GET"])
def planets():
    planets_list = Planet.query.all()
    result = planets_schema.dump(planets_list)
    return jsonify(result), 200

# marshmallow schemas


    


if __name__ == '__main__':
    app.run(debug=True)