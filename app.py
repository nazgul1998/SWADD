from flask import Flask
from routes.pacientes import pacientes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")


app.config.update(dict(
    RECAPTCHA_ENABLED = True,
    RECAPTCHA_SITE_KEY = "6Ld_MlYgAAAAALFIh30safrM4yyOw6JCVlnuS9oO" ,
    RECAPTCHA_SECRET_KEY = "6Ld_MlYgAAAAAINLuF1Z5nNwrqCvpwDv7hUqwDjn" ,
))
app.config['SECRET_KEY'] = "N@zgul1998!!"
#config db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/SWADD'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(pacientes)


