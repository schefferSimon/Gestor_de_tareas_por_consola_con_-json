import json
import os
from models.tarea import Tarea

class ServicioTarea:
    def __init__(self):
        self.listaTareas = []
        self.rutaArchivo = "data/tareas.json"


    def cargarTareas(self):
        if not os.path.exists(self.rutaArchivo):
            self.listaTareas = []
            return 

        with open(self.rutaArchivo, "r") as archivo :
            datos = json.load(archivo)
        
        self.listaTareas= []
        
        for diccionario in datos:
            t = Tarea(**diccionario)
            self.listaTareas.append(t)

