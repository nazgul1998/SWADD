from flask import Flask
from routes.pacientes import pacientes
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="templates")

#config db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/SWADD'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(pacientes)


