from flask import Flask , Blueprint
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restplus import Api


app = Flask(__name__)
app.config['SECRET_KEY'] = '9be2425c134644f512341d1c9678cafa'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://onjutkbosxshkp:0239028ad3492f69057fabf2d9c51bcc08a6e2e1edb865eaf14f3ae19678d80b@ec2-3-234-22-132.compute-1.amazonaws.com:5432/d4g589rc6v9j0g'


db = SQLAlchemy(app)
db.init_app(app)


from temariIfo.api import routes
from temariIfo.api import models


from temariIfo.api.routes import api_bp
app.register_blueprint(api_bp)



# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")
# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)


#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/TemariInfo2'
