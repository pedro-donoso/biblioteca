"""Sistema de Gestión de Biblioteca"""


class Libro:
    def __init__(self, titulo, autor, anio, estado="disponible"):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__estado = estado
        

    def  get_titulo(self):
        return self.__titulo
    
    
    def get_autor(self):
        return self.__autor
    
    
    def get_anio(self):
        return self.__anio
    
    
    def get_estado(self):
        return self.__estado
    
        
    def set_estado(self, estado):
        if estado in ["disponible", "prestado"]:
            self.__estado = estado
        else:
            raise ValueError("Estado debe ser 'disponible" o "prestado")
        
        
    def prestar(self):
        if self.__estado == "prestado":
            raise Exception(f"El libro '{self.__titulo}' ya está prestado")
        self.__estado = "prestado"
        
        
    