from flask import Flask
from routes.pacientes import pacientes
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os 
from flask_wtf.csrf import CSRFProtect

load_dotenv()
app = Flask(__name__, template_folder="templates")
csrf = CSRFProtect(app)
csrf.init_app(app)
app.secret_key = os.getenv('SECRET_KEY').strip()

print(app.secret_key)

#config db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/SWADD'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(pacientes)


