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
        
        
    def devolver(self):
        if self.__estado == "disponible":
            raise Exception(f"El libro '{self.__titulo}' ya está disponible")
        self.__estado = "disponible"
        
        
    def __str__(self):
        return f"Titulo: {self.__titulo}, Autor: {self.__autor}, Año: {self.__anio}, Estado: {self.__estado}"
    
    
    
    def to_file_format(self):
        return f"{self.__titulo}|{self.__autor}|{self.__anio}|{self.__estado}"
    
    
class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, estado="disponible"):
        super().__init__(titulo, autor, anio, estado)
        self.__formato = formato
        
        
    def get_formato(self):
        return self.__formato
    
    
    def __str__(self):
        return f"{super().__str__()}, Formato: {self.__formato}"
    
    
    def to_file_format(self):
        return f"DIGITAL{super().to_file_format()}|{self.__formato}"
    
    
