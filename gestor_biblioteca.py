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
    
    
class Biblioteca:
    def __init__(self, archivo="biblioteca.txt"):
        self.__libros = []
        self._archivo = archivo
        self.cargar_desde_archivo()
        
        
    def agregar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise TypeError("Solo se pueden agregar objetos de tipo Libro")
        
        for lib in self.__libros:
            if lib.get_titulo().lower() == libro.get_titulo.lower():
                raise Exception(f"Ya existe un libro con el título '{libro.get_titulo}'")
            
        self.__libros.append(libro)
        print(f"Libro '{libro.get_titulo()}' agregado exitosamente")
        
        
    def eliminar_libro(self, titulo):
        for i, libro in enumerate(self.__libros):
            if libro.get_titulo().lower() == titulo.lower():
                self.__libros.pop(i)
                print(f" Libro '{titulo}' eliminado exitosamente")
                return
        raise Exception(f"No se encontró el libro '{titulo}'")
    
    
    def buscar_libro(self, titulo):
        for libro in self.__libros:
            if libro.get_titulo().lower() == titulo.lower():
                return libro
        raise Exception(f"No se encontró el libro '{titulo}'")
    
    
    def listar_libros(self):
        if not self.__libros:
            print("La biblioteca está vacía")
            return
        
        print("\n" + "="*70)
        print("CATÁLOGO DE LIBROS")
        print("="*70)
        for i, libro in enumerate(self.__libros, 1):
            tipo = "[DIGITAL]" if isinstance(libro, LibroDigital) else "[FÍSICO]"
            print(f"{i}. {tipo} {libro}")
        print("="*70 + "\n")
        
        
    def listar_disponibles(self):
        disponibles = [lib for lib in self.__libros if lib.get_estado() == "disponible"]
        
        if not disponibles:
            print("No hay libros disponibles")
            return
        
        print("\n" + "="*70)
        print("LIBROS DISPONIBLES")
        print("="*70)
        for i, libro in enumerate(disponibles, 1):
            tipo = "[DIGITAL]" if isinstance(libro, LibroDigital) else "[FÍSICO]"
            print(f"{i}. {tipo} {libro}")
        print("="*70 + "\n")
        
        
    