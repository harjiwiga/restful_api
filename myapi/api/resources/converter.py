
from geoalchemy2 import Geography,Geometry
from marshmallow_sqlalchemy import ModelConverter
from marshmallow import fields

class GeoConverter(ModelConverter):
    SQLA_TYPE_MAPPING = ModelConverter.SQLA_TYPE_MAPPING.copy()
    SQLA_TYPE_MAPPING.update({
        Geometry: fields.Str
    })

