from marshmallow import Schema, fields

class PlanetSchema(Schema):
    planet_id = fields.Int()
    planet_name = fields.Str()
    planet_type = fields.Str()
    home_star = fields.Str()
    mass = fields.Float()
    radius = fields.Float()
    distance = fields.Float()
    image = fields.String()

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)