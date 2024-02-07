from marshmallow import Schema, fields

class PlanetSchema(Schema):
    planet_id = fields.Integer()
    planet_name = fields.String()
    planet_type = fields.String()
    home_star = fields.String()
    mass = fields.Float()
    radius = fields.Float()
    distance = fields.Float()
    image = fields.String()
    description = fields.String()

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)