from utils.db import db

class Paciente(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre_completo = db.Column(db.String(300))
    estado_civil = db.Column(db.String(20))
    edad = db.Column(db.Integer)
    sexo = db.Column(db.String(10))
    ocupacion = db.Column(db.String(20))
    educacion = db.Column(db.String(20))
    fecha = db.Column(db.Date)

    item1 = db.Column(db.Integer)
    item2 = db.Column(db.Integer)
    item3 = db.Column(db.Integer)
    item4 = db.Column(db.Integer)
    item5 = db.Column(db.Integer)
    item6 = db.Column(db.Integer)
    item7 = db.Column(db.Integer)
    item8 = db.Column(db.Integer)
    item9 = db.Column(db.Integer)
    item10 = db.Column(db.Integer)
    item11 = db.Column(db.Integer)
    item12 = db.Column(db.Integer)
    item13 = db.Column(db.Integer)
    item14 = db.Column(db.Integer)
    item15 = db.Column(db.Integer)
    item16 = db.Column(db.Integer)
    item17 = db.Column(db.Integer)
    item18 = db.Column(db.Integer)
    item19 = db.Column(db.Integer)
    item20 = db.Column(db.Integer)
    item21 = db.Column(db.Integer)
    
    emocion1 =db.Column(db.String(20))
    emocion2 =db.Column(db.String(20))
    emocion3 =db.Column(db.String(20))
    emocion4 =db.Column(db.String(20))
    emocion5 =db.Column(db.String(20))
    emocion6 =db.Column(db.String(20))
    emocion7 =db.Column(db.String(20))
    emocion8 =db.Column(db.String(20))
    emocion9 =db.Column(db.String(20))
    emocion10 =db.Column(db.String(20))
    emocion11 =db.Column(db.String(20))
    emocion12 =db.Column(db.String(20))
    emocion13 =db.Column(db.String(20))
    emocion14 =db.Column(db.String(20))
    emocion15 =db.Column(db.String(20))
    emocion16 =db.Column(db.String(20))
    emocion17 =db.Column(db.String(20))
    emocion18 =db.Column(db.String(20))
    emocion19 =db.Column(db.String(20))
    emocion20 =db.Column(db.String(20))
    emocion21 =db.Column(db.String(20))

    total = db.Column(db.Integer)
    
    def __init__(self,nombre_completo,estado_civil,edad,sexo,ocupacion,educacion,fecha):
        self.nombre_completo = nombre_completo
        self.estado_civil = estado_civil
        self.edad = edad
        self.sexo = sexo
        self.ocupacion = ocupacion
        self.educacion = educacion
        self.fecha = fecha
        
        self.item1 = -1
        self.item2 = -1
        self.item3 = -1
        self.item4 = -1
        self.item5 = -1
        self.item6 = -1
        self.item7 = -1
        self.item8 = -1
        self.item9 = -1
        self.item10 = -1
        self.item11 = -1
        self.item12 = -1
        self.item13 = -1
        self.item14 = -1
        self.item15 = -1
        self.item16 = -1
        self.item17 = -1
        self.item18 = -1
        self.item19 = -1
        self.item20 = -1
        self.item21 = -1
        
        
        self.emocion1 = "a"
        self.emocion2 = "a"
        self.emocion3 = "a"
        self.emocion4 = "a"
        self.emocion5 = "a"
        self.emocion6 = "a"
        self.emocion7 = "a"
        self.emocion8 = "a"
        self.emocion9 = "a"
        self.emocion10 = "a"
        self.emocion11 = "a"
        self.emocion12 = "a"
        self.emocion13 = "a"
        self.emocion14 = "a"
        self.emocion15 = "a"
        self.emocion16= "a"
        self.emocion17 = "a"
        self.emocion18 = "a"
        self.emocion19 = "a"
        self.emocion20 = "a"
        self.emocion21 = "a"

        self.total = 0
        
        
    def __str__(self) -> str:
        cadena = self.nombre_completo + " " + self.estado_civil + " " + str(self.edad) + " " + self.sexo + " " + self.ocupacion + " " + self.educacion + " " + str(self.fecha)
        return cadena