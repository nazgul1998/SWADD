from multiprocessing.sharedctypes import Value
from flask import Blueprint, render_template, request, Response
from models.pacientes import Paciente
from utils.db import db
from utils.gordon import obtener_frame_camara, imagePaths

pacientes = Blueprint('pacientes', __name__)

@pacientes.route("/")
def home():
    return render_template("/templates/home.html")

@pacientes.route("/indicaciones")
def indicaciones():
    return render_template("/templates/indicaciones.html")

@pacientes.route('/datos_basicos', methods=["POST"])
def datos_basicos():
    nombre_completo = request.form['nombre_completo']
    estado_civil = request.form['estado_civil']
    edad = request.form['edad']
    sexo = request.form['sexo']
    ocupacion = "Estudiante"
    educacion = "Secundaria"
    fecha = request.form['fecha']
    
    nuevo_paciente = Paciente(nombre_completo,estado_civil,edad,sexo,ocupacion,educacion,fecha)
    db.session.add(nuevo_paciente)
    db.session.commit()
    id = nuevo_paciente.id
    print(nuevo_paciente)
    return question01(nuevo_paciente.id)

@pacientes.route("/quest1/<int:id>", methods=["GET"])
def question01(id):
    return render_template("/templates/questions/question01.html", id=id)
    
@pacientes.route("/emocion1", methods=["POST"])
def emocion01():
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item1'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = 1
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 0
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje 
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = 0
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item1 = nuevo
    paciente.emocion1 = animo
    db.session.commit()
    print("pregunta 1 lista")
    return render_template("/templates/questions/question01.html", id=id)

