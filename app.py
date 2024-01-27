from flask import Flask, jsonify, request

from flask_sqlalchemy import SQLAlchemy

import os

from model import *
from schemas import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route('/planets', methods=["GET"])
def planets():
    session = Session()
    planets_list = session.query(Planet).all()
    result = planets_schema.dump(planets_list)
    return jsonify(result), 200

@app.route('/planet', methods=['POST'])
def post_planet():
    try:
        json_data = request.form
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

@app.route('/planet/<int:id>', methods=['DELETE'])
def delete_planet(id):
    try:
        session = Session()
        delete_planet = session.query(Planet).filter(Planet.planet_id == id).first()
        if not delete_planet:
            error_msg = f'Planet not found in the database'
            return {"message": error_msg}, 200
        else:
            delete = session.query(Planet).filter(Planet.planet_id == id).delete()
            session.commit()
            msg = f'Planet with id: {id}, was deleted'
            return {"message": msg}, 200
    except:
        error_msg = f'Planet not found'
        return {"message": error_msg}, 422

@app.route('/planet/<int:id>', methods=['PUT'])
def edit_planet(id):
    try:
        session = Session()
        planet = session.query(Planet).filter(Planet.planet_id == id).first()

        if not planet:
            error_msg = f'Planet does not exist in database'
            return {"message": error_msg}, 200
        else:
            for field, value in request.form.items():
                setattr(planet, field, value)
        
        session.commit()

        error_msg = f'Planet with id: {id} updated with new values'
        return {"message": error_msg}, 200
    except Exception as e:
        print("Error:", str(e))
        return jsonify(message='Failed to create a Planet'), 404

           

