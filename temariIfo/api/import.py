import csv

from flask import Flask
from temariIfo import *
from temariIfo.api.models import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/TemariInfo2'
db.init_app(app)

def main():
    f = open('../resources/univ.csv')
    reader = csv.reader(f)

    for univ_id, univ_name, location, description in reader:

        University = Universities(univ_id=univ_id,univ_name=univ_name,location=location,
                        description=description)
        db.session.add(University)
    
    db.session.commit()

    f = open('../resources/inst_descrip.csv')
    reader = csv.reader(f)

    for inst_id, university_id, institute_name, phone_no, email, description in reader:

        Institute = Institutes(inst_id=inst_id,university_id=university_id,institute_name=institute_name,
                        phone_no=phone_no,email=email,description=description)
        db.session.add(Institute)
    
    db.session.commit()

    f = open('../resources/dept.csv')
    reader = csv.reader(f)

    for info_id, institute_id, department, years, objective in reader:

        Department = Information(info_id=info_id,institute_id=institute_id,department=department,
                        years=years,objective=objective)
        db.session.add(Department)
    
    db.session.commit()

    f = open('../resources/dept.csv')
    reader = csv.reader(f)

    for image_id, image_name, university_id, description in reader:

        Image = Images(image_id=image_id,image_name=image_name,university_id=university_id)
        db.session.add(Image)
    
    db.session.commit()

    if __name__ == '__main__':
        with app.app_context():
            main()