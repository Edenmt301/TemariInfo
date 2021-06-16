from flask_marshmallow import Marshmallow
from temariIfo.api.models import *
from temariIfo import app
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema,fields as ma_fields


ma = Marshmallow(app)

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        #include_fk = True

class ImageSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Images
        load_instance = True
        include_fk = True

class InformationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Information
        load_instance = True
        include_fk = True

class InstituteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Institutes
        load_instance = True
        include_fk = True
        include_relationships = True
    
    information= ma_fields.Nested(InformationSchema, many=True, only=['info_id', 'department','years','objective'])

   
class UniversitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Universities
        load_instance = True
        include_relationships = True
    
    institutes = ma_fields.Nested(InstituteSchema, many=True)
    Images = ma_fields.Nested(ImageSchema, many=True, only=['image_id', 'image_name'])
