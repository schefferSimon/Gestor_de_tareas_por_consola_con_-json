class Tarea:

    def __init__(self, nombre, fechaLimite, descripcion, estado="pendiente"):
        self.__nombre = nombre
        self.__estado = estado
        self.__fechaLimite = fechaLimite
        self.__descripcion = descripcion

    def getNombre(self):
        return self.__nombre
    
    def getEstado(self):
        return self.__estado
    
    def getFechaLimite(self):
        return self.__fechaLimite

    def getDescripcion(self):
        return self.__descripcion

    def marcarCompletada(self):
        self.__estado = "Completada"

    