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
    return render_template("/templates/questions/question11.html", id=id)