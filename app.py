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
    session = Session()
    planets_list = session.query(Planet).all()
    result = planets_schema.dump(planets_list)
    return jsonify(result), 200

@app.route('/planet', methods=['POST'])
def post_planet():
    try:
        json_data = request.get_json()
        print("Received JSON data:", json_data)
        
        new_planet_data = planet_schema.load(json_data)
        new_planet = Planet(**new_planet_data)

        print("New Planet instance:", new_planet)

        session = Session()
        session.add(new_planet)
        session.commit()

        return jsonify(new_planet_data), 201  # 201 Created status code
    except Exception as e:
        print("Error:", str(e))
        return jsonify(message='Failed to create a Planet'), 404