from flask import Flask
import os
from db.database import db
from endpoints.department import department_bp
from endpoints.employee import employee_bp

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql5721270:IUpPqbqNBI@sql5.freesqldatabase.com/sql5721270'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(employee_bp, url_prefix='/employee/')
app.register_blueprint(department_bp, url_prefix='/department/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(host='0.0.0.0', port=8888)
