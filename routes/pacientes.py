from multiprocessing.sharedctypes import Value
from flask import Blueprint, render_template, request, Response
from models.pacientes import Paciente
from utils.db import db
from utils.gordon import obtener_frame_camara, imagePaths
from dotenv import load_dotenv
load_dotenv()
import os 
import hashlib


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
    fecha = request.form['fecha']
    clave = ""
    if ("invitacion" in request.form):
        invitacion = request.form['invitacion']
        clave = hashlib.sha256()
        clave.update(bytes(invitacion,'utf-8'))
        print (clave.hexdigest())
        print (os.getenv('SECRET_VALUE').strip())
        
    if (clave.hexdigest() == os.getenv('SECRET_VALUE')):
        print("invitado")
        
        
    elif not (clave.hexdigest() == os.getenv('SECRET_VALUE')):
        return render_template("/templates/indicaciones.html")
    
    
    if(nombre_completo == "" or estado_civil == "" or edad == "" or sexo=="" or fecha==""):
        return render_template("/templates/indicaciones.html")
    
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
    
    if not ("item1" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question01.html", id=id)
    
    
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
    print("pregunta 1 guardada con exito")
    return render_template("/templates/questions/question02.html", id=id)



@pacientes.route("/quest2/<int:id>", methods=["GET"])
def question02(id):
    return render_template("/templates/questions/question02.html", id=id)
    
@pacientes.route("/emocion2", methods=["POST"])
def emocion02():
    
    if not ("item2" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question02.html", id=id)
    
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item2'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
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
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje 
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 3
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item2 = nuevo
    paciente.emocion2 = animo
    db.session.commit()
    print("pregunta 2 guardada con exito")
    return render_template("/templates/questions/question03.html", id=id)



@pacientes.route("/quest3/<int:id>", methods=["GET"])
def question03(id):
    return render_template("/templates/questions/question03.html", id=id)
    
@pacientes.route("/emocion3", methods=["POST"])
def emocion03():
    
    if not ("item3" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question03.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item3'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = 0
        elif(puntaje == 2):
            nuevo = 0
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
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje 
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
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
    paciente.item3 = nuevo
    paciente.emocion3 = animo
    db.session.commit()
    print("pregunta 3 guardada con exito")
    return render_template("/templates/questions/question04.html", id=id)


@pacientes.route("/quest4/<int:id>", methods=["GET"])
def question04(id):
    return render_template("/templates/questions/question04.html", id=id)
    
@pacientes.route("/emocion4", methods=["POST"])
def emocion04():
    
    if not ("item4" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question04.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item4'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 0
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = 1 
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
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
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item4 = nuevo
    paciente.emocion4 = animo
    db.session.commit()
    print("pregunta 4 guardada con exito")
    return render_template("/templates/questions/question05.html", id=id)



@pacientes.route("/quest5/<int:id>", methods=["GET"])
def question05(id):
    return render_template("/templates/questions/question05.html", id=id)
    
@pacientes.route("/emocion5", methods=["POST"])
def emocion05():
    
    if not ("item5" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question05.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item5'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 1
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item5 = nuevo
    paciente.emocion5 = animo
    db.session.commit()
    print("pregunta 5 guardada con exito")
    return render_template("/templates/questions/question06.html", id=id)





@pacientes.route("/quest6/<int:id>", methods=["GET"])
def question06(id):
    return render_template("/templates/questions/question06.html", id=id)
    
@pacientes.route("/emocion6", methods=["POST"])
def emocion06():
    
    if not ("item6" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question06.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item6'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 1
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item6 = nuevo
    paciente.emocion6 = animo
    db.session.commit()
    print("pregunta 6 guardada con exito")
    return render_template("/templates/questions/question07.html", id=id)



@pacientes.route("/quest7/<int:id>", methods=["GET"])
def question07(id):
    return render_template("/templates/questions/question07.html", id=id)
    
@pacientes.route("/emocion7", methods=["POST"])
def emocion07():
    
    if not ("item7" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question07.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item7'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = 0
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 0
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 1
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item7 = nuevo
    paciente.emocion7 = animo
    db.session.commit()
    print("pregunta 7 guardada con exito")
    return render_template("/templates/questions/question08.html", id=id)



@pacientes.route("/quest8/<int:id>", methods=["GET"])
def question08(id):
    return render_template("/templates/questions/question08.html", id=id)
    
@pacientes.route("/emocion8", methods=["POST"])
def emocion08():
    
    if not ("item8" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question08.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item8'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item8 = nuevo
    paciente.emocion8 = animo
    db.session.commit()
    print("pregunta 8 guardada con exito")
    return render_template("/templates/questions/question09.html", id=id)



@pacientes.route("/quest9/<int:id>", methods=["GET"])
def question09(id):
    return render_template("/templates/questions/question09.html", id=id)
    
@pacientes.route("/emocion9", methods=["POST"])
def emocion09():
    
    if not ("item9" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question09.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item9'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 0
        elif(puntaje == 3):
            nuevo = 0
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 2
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
            nuevo = 1
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 0
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item9 = nuevo
    paciente.emocion9 = animo
    db.session.commit()
    print("pregunta 9 guardada con exito")
    return render_template("/templates/questions/question10.html", id=id)


@pacientes.route("/quest10/<int:id>", methods=["GET"])
def question10(id):
    return render_template("/templates/questions/question10.html", id=id)
    
@pacientes.route("/emocion10", methods=["POST"])
def emocion10():
    
    if not ("item10" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question10.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item10'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
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
            nuevo = 1
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 3
        elif(puntaje == 1):
            nuevo = 3
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item10 = nuevo
    paciente.emocion10 = animo
    db.session.commit()
    print("pregunta 10 guardada con exito")
    return render_template("/templates/questions/question11.html", id=id)


@pacientes.route("/quest11/<int:id>", methods=["GET"])
def question11(id):
    return render_template("/templates/questions/question11.html", id=id)
    
@pacientes.route("/emocion11", methods=["POST"])
def emocion11():
    
    if not ("item11" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question11.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item11'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 1
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
            nuevo = 2
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item11 = nuevo
    paciente.emocion11 = animo
    db.session.commit()
    print("pregunta 11 guardada con exito")
    return render_template("/templates/questions/question12.html", id=id)



@pacientes.route("/quest12/<int:id>", methods=["GET"])
def question12(id):
    return render_template("/templates/questions/question12.html", id=id)
    
@pacientes.route("/emocion12", methods=["POST"])
def emocion12():
    
    if not ("item12" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question12.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item12'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 1
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo =puntaje
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item12 = nuevo
    paciente.emocion12 = animo
    db.session.commit()
    print("pregunta 12 guardada con exito")
    return render_template("/templates/questions/question13.html", id=id)



@pacientes.route("/quest13/<int:id>", methods=["GET"])
def question13(id):
    return render_template("/templates/questions/question13.html", id=id)
    
@pacientes.route("/emocion13", methods=["POST"])
def emocion13():
    
    if not ("item13" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question13.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item13'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo =puntaje
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item13 = nuevo
    paciente.emocion13 = animo
    db.session.commit()
    print("pregunta 13 guardada con exito")
    return render_template("/templates/questions/question14.html", id=id)


@pacientes.route("/quest14/<int:id>", methods=["GET"])
def question14(id):
    return render_template("/templates/questions/question14.html", id=id)
    
@pacientes.route("/emocion14", methods=["POST"])
def emocion14():
    if not ("item14" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question14.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item14'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 2
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item14 = nuevo
    paciente.emocion14 = animo
    db.session.commit()
    print("pregunta 14 guardada con exito")
    return render_template("/templates/questions/question15.html", id=id)




@pacientes.route("/quest15/<int:id>", methods=["GET"])
def question15(id):
    return render_template("/templates/questions/question15.html", id=id)
    
@pacientes.route("/emocion15", methods=["POST"])
def emocion15():
    if not ("item15" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question15.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item15'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
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
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = 3
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item15 = nuevo
    paciente.emocion15 = animo
    db.session.commit()
    print("pregunta 15 guardada con exito")
    return render_template("/templates/questions/question16.html", id=id)




@pacientes.route("/quest16/<int:id>", methods=["GET"])
def question16(id):
    return render_template("/templates/questions/question16.html", id=id)
    
@pacientes.route("/emocion16", methods=["POST"])
def emocion16():
    if not ("item16" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question16.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item16'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item16 = nuevo
    paciente.emocion16 = animo
    db.session.commit()
    print("pregunta 16 guardada con exito")
    return render_template("/templates/questions/question17.html", id=id)




@pacientes.route("/quest17/<int:id>", methods=["GET"])
def question17(id):
    return render_template("/templates/questions/question17.html", id=id)
    
@pacientes.route("/emocion17", methods=["POST"])
def emocion17():
    if not ("item17" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question17.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item17'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item17 = nuevo
    paciente.emocion17 = animo
    db.session.commit()
    print("pregunta 17 guardada con exito")
    return render_template("/templates/questions/question18.html", id=id)




@pacientes.route("/quest18/<int:id>", methods=["GET"])
def question18(id):
    return render_template("/templates/questions/question18.html", id=id)
    
@pacientes.route("/emocion18", methods=["POST"])
def emocion18():
    if not ("item18" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question18.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item18'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo =puntaje
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item18 = nuevo
    paciente.emocion18 = animo
    db.session.commit()
    print("pregunta 18 guardada con exito")
    return render_template("/templates/questions/question19.html", id=id)




@pacientes.route("/quest19/<int:id>", methods=["GET"])
def question19(id):
    return render_template("/templates/questions/question19.html", id=id)
    
@pacientes.route("/emocion19", methods=["POST"])
def emocion19():
    if not ("item19" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question19.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item19'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item19 = nuevo
    paciente.emocion19 = animo
    db.session.commit()
    print("pregunta 19 guardada con exito")
    return render_template("/templates/questions/question20.html", id=id)





@pacientes.route("/quest20/<int:id>", methods=["GET"])
def question20(id):
    return render_template("/templates/questions/question20.html", id=id)
    
@pacientes.route("/emocion20", methods=["POST"])
def emocion20():
    if not ("item20" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question20.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item20'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 0
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
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo =puntaje
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item20 = nuevo
    paciente.emocion20 = animo
    db.session.commit()
    print("pregunta 20 guardada con exito")
    return render_template("/templates/questions/question21.html", id=id)






@pacientes.route("/quest21/<int:id>", methods=["GET"])
def question21(id):
    return render_template("/templates/questions/question21.html", id=id)
    
@pacientes.route("/emocion21", methods=["POST"])
def emocion21():
    if not ("item21" in request.form):
        id = int(request.form['id'])
        return render_template("/templates/questions/question21.html", id=id)
    
    emocion = obtener_frame_camara()
    while emocion == "":
        emocion = obtener_frame_camara()
    puntaje = int(request.form['item21'])
    animo = imagePaths[emocion[0]]
    print(animo + " - " + str(puntaje))
    id = int(request.form['id'])
    nuevo = -1
    #['Disgustado', 'Enojado', 'Feliz', 'Serio', 'Sorprendido', 'Temerozo', 'Triste']
    if(animo == 'Feliz'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 1
    elif(animo == 'Enojado'):
        if(puntaje == 0):
            nuevo = 2
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Disgustado'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
    elif(animo == 'Serio'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Sorprendido'):
        if(puntaje == 0):
            nuevo = puntaje
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 1
        elif(puntaje == 3):
            nuevo = 2
            
    elif(animo == 'Temerozo'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = puntaje
        elif(puntaje == 2):
            nuevo = 3
        elif(puntaje == 3):
            nuevo = puntaje
            
    elif(animo == 'Triste'):
        if(puntaje == 0):
            nuevo = 1
        elif(puntaje == 1):
            nuevo = 2
        elif(puntaje == 2):
            nuevo = puntaje
        elif(puntaje == 3):
            nuevo = puntaje
            
            
    print(str(animo) + " - " + str(nuevo))      
    paciente = Paciente.query.get(id)
    paciente.item21 = nuevo
    paciente.emocion21 = animo
    db.session.commit()
    print("pregunta 21 guardada con exito")
    paciente.total = paciente.item1 + paciente.item2 + paciente.item3 +paciente.item4 +paciente.item5 + paciente.item6 + paciente.item7 +paciente.item8 + paciente.item9 +paciente.item10 +paciente.item11+paciente.item12 + paciente.item13 + paciente.item14+paciente.item15+paciente.item16+paciente.item17+paciente.item18+paciente.item19+paciente.item20+paciente.item21
    if paciente.total>=0 and paciente.total<=13:
        paciente.resultado_final = "Mínina depresión."
    elif paciente.total>=14 and paciente.total<=19:
        paciente.resultado_final = "Depresión leve."
    elif paciente.total>=20 and paciente.total<=28:
        paciente.resultado_final = "Depresión moderada."
    elif paciente.total>=29 and paciente.total<=63:
        paciente.resultado_final = "Depresión grave."
        
    db.session.commit()
    print("pregunta 21 guardada con exito")
    return render_template("/templates/agradecimiento.html", id=id)
    

