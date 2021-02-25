from flask import Flask
from flask_restful import  Api
from urllib.parse import quote
import sqlalchemy

from resources.external_API import External_Data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy.engine.url.URL(drivername="mysql+pymysql",
    username="root",
    password="Intern@123",
    host="mysql.cnc.hclets.com",
    port=61606,
    database="nsds",
    )
'mysql+pymysql://root:%s@mysql.cnc.hclets.com:61606' % quote('Intern@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPOGATE_EXCEPTIONS'] = True
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


api.add_resource(External_Data, '/external_API')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000)
