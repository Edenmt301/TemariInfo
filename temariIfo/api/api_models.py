from flask_restplus import  fields as rp_fields
from temariIfo.api.routes import api



univ = api.model("University", {
    'name': rp_fields.String('Name of the University'),
    'location': rp_fields.String,
    'description': rp_fields.String,
})
inst = api.model("Institute", {
    'name': rp_fields.String('Name of the Istitute'),
    'phone_no': rp_fields.String,
    'email': rp_fields.String,
    'description': rp_fields.String,
    'university_name': rp_fields.String,
})
dept = api.model("Information", {
    'department': rp_fields.String('Name of the Department'),
    'years': rp_fields.Integer,
    'objective': rp_fields.String,
    'institute_name': rp_fields.String,
})