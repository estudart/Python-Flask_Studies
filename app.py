from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flasgger import Swagger
from model import *
from schemas import *

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class HomeResource(Resource):
    def get(self):
        """
        Welcome to the home page!

        ---
        responses:
          200:
            description: A welcome message.
        """
        return {"message": "Welcome to the home page!"}

class PlanetsResource(Resource):
    def get(self):
        """
        Get a list of planets.

        ---
        responses:
          200:
            description: List of planets.
        """
        session = Session()
        planets_list = session.query(Planet).all()
        result = planets_schema.dump(planets_list)
        return result, 200

    def post(self):
        """
        Create a new planet.

        ---
        parameters:
          - name: planet_name
            in: formData
            type: string
            required: true
            description: The name of the planet.
          - name: planet_type
            in: formData
            type: string
            description: The type of the planet.
          - name: home_star
            in: formData
            type: string
            description: The home star of the planet.
          - name: mass
            in: formData
            type: float
            description: The mass of the planet.
          - name: radius
            in: formData
            type: float
            description: The radius of the planet.
          - name: distance
            in: formData
            type: float
            description: The distance from home star of the planet.
        responses:
          201:
            description: Created.
        """
        try:
            json_data = request.form
            new_planet_data = planet_schema.load(json_data)
            new_planet = Planet(**new_planet_data)

            session = Session()
            session.add(new_planet)
            session.commit()

            return jsonify(new_planet_data), 201
        except Exception as e:
            return jsonify(message='Failed to create a Planet'), 404

class PlanetResource(Resource):
    def delete(self, id):
        """
        Delete a planet by ID.

        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: The ID of the planet to delete.
        responses:
          200:
            description: Planet deleted.
          422:
            description: Planet not found.
        """
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

    def put(self, id):
        """
        Update a planet by ID.

        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: The ID of the planet to update.
          - name: planet_name
            in: formData
            type: string
            description: The name of the planet.
          - name: planet_type
            in: formData
            type: string
            description: The type of the planet.
          - name: home_star
            in: formData
            type: string
            description: The home star of the planet.
          - name: mass
            in: formData
            type: float
            description: The mass of the planet.
          - name: radius
            in: formData
            type: float
            description: The radius of the planet.
          - name: distance
            in: formData
            type: float
            description: The distance from home star of the planet.
        responses:
          200:
            description: Planet updated.
          404:
            description: Failed to update planet.
        """
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
            return jsonify(message='Failed to create a Planet'), 404

api.add_resource(HomeResource, '/')
api.add_resource(PlanetsResource, '/planets')
api.add_resource(PlanetResource, '/planet/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
