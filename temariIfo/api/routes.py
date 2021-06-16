
from flask import Flask, jsonify,  request, Blueprint
from functools import wraps
from flask_restplus import Resource, Api, fields as rp_fields
from marshmallow import Schema,fields as ma_fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from temariIfo.api.models import *
from temariIfo.api.schemas import *

# authorization={'apikey' : {
#         'type' : 'apiKey',
#         'in' : 'header',
#         'name':'X-API-KEY',
#     }
# }

api_bp = Blueprint('api', __name__)
api = Api(api_bp)



from temariIfo.api.api_models import *
from temariIfo import db



@api.route('/api/University/<int:id>')
class Index(Resource):
    def get(self, id):
         one_uni=Universities.query.filter_by(univ_id=id).first()
         uni_schema=UniversitySchema()
         return uni_schema.dump(one_uni)
         
    @api.expect(univ)
    @api.response(204, 'University successfully updated.')
    def put(self, id):
        """
        Updates a University.
        """
        univ = Universities.query.filter_by(uiv_id=id).first()
        
        univ.univ_name = request.json['name']
        univ.location = request.json['location']
        univ.description = request.json['description']
        

        db.session.add(univ)
        db.session.commit()

        return UniversitySchema.dump(univ)
    @api.response(204, 'University successfully deleted.')
    def delete(self, id):
        """
        Deletes University.
        """
        univ = Universities.query.filter_by(univ_id=id).first()
        if univ is None:
            return None, 404
        db.session.delete(univ)
        db.session.commit()
        return None, 204



@api.route('/api/Universities')
class Index(Resource):
    def get(self):
         one_uni=Universities.query.all()
         uni_schema=UniversitySchema(many=True)
         return uni_schema.dump(one_uni)
    @api.expect(univ)
    def post(self):
        """
        Create a new University
        """
        new_univ = Universities()
        new_univ.univ_name = request.json['name']
        new_univ.location = request.json['location']
        new_univ.description = request.json['description']
        
        db.session.add(new_univ)
        db.session.commit()

        return UniversitySchema().dump(new_univ)



@api.route('/api/Institutes/<int:id>')
class Index(Resource):
     def get(self, id):
         one_uni=Institutes.query.filter_by(inst_id=id).first()
         uni_schema=InstituteSchema()
         return uni_schema.dump(one_uni)
         
@api.route('/api/Institute')
class Index(Resource):
    def get(self):
         one_uni=Institutes.query.all()
         uni_schema=InstituteSchema(many=True)
         return uni_schema.dump(one_uni)

    @api.expect(inst)
    def post(self):
        """
        Create a new Institute
        """
        new_inst = Institutes()
        uni_name =request.json['university_name']
        univ = Universities.query.filter_by(univ_name=uni_name).first_or_404()
        if univ:
            new_inst.university_id =univ.univ_id
        else:
            return None, 404
        new_inst.institute_name = request.json['name']
        new_inst.phone_no = request.json['phone_no']
        new_inst.email = request.json['email']
        new_inst.description = request.json['description']
        
        db.session.add(new_inst)
        db.session.commit()

        return InstituteSchema().dump(new_inst)

@api.route('/api/Department/<int:id>')
class Index(Resource):
     def get(self, id):
         one_uni=Information.query.filter_by(info_id=id).first()
         uni_schema=InformationSchema()
         return uni_schema.dump(one_uni)

@api.route('/api/Department')
class Index(Resource):
    def get(self):
         one_uni=Information.query.all()
         uni_schema=InformationSchema(many=True)
         return uni_schema.dump(one_uni)

    @api.expect(dept)
    def post(self):
        """
        Create a new Department
        """
        new_dept = Information()
        inst_name =request.json['institute_name']
        inst = Institutes.query.filter_by(institute_name=inst_name).first_or_404()
        if inst:
           new_dept.institute_id =inst.inst_id
        else:
            return None, 404
        new_dept.department = request.json['department']
        new_dept.objective = request.json['objective']
        new_dept.years = request.json['years']
        
        db.session.add(new_dept)
        db.session.commit()

        return InformationSchema().dump(new_dept)

