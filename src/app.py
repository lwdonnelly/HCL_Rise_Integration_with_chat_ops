from flask import Flask
from flask_restful import  Api
from urllib.parse import quote

from resources.external_API import External_Data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:%s@mysql.cnc.hclets.com:61606' % quote('Intern@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPOGATE_EXCEPTIONS'] = True
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(External_Data, '/external_API')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000)
