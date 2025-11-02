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
        
        
    def marcar_prestado(self, titulo):
        libro = self.buscar_libro(titulo)
        libro.prestar()
        print(f"Libro '{titulo}' marcado como prestado")
        
        
    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        libro.devolver()
        print(f"Libro '{titulo}' devuelto exitosamente")
        
        
    def cargar_desde_archivo(self):
        try:
            with open(self.__archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    
                    partes = linea.split('|')
                    
                    if partes[0] == "DIGITAL":
                        libro = LibroDigital(partes[1], partes[2], int(partes[3]), partes[5], partes[4])
                    else:
                        libro = Libro(partes[0], partes[1], int(partes[2]), partes[3])
                        
                    self.__libros.append(libro)
                    
            print(f"Se cargaron {len(self.__libros)} libro(s) desde {self.__archivo}")
        except FileNotFoundError:
            print(f"Archivo '{self.__archivo}' no encontrado. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar archivo: {e}")
            
     
    def guardar_en_archivo(self):
        try:
            with open(self.__archivo, 'w', enconding='utf-8') as f:
                for libro in self.__libros:
                    f.write(libro.to_file_format() + '\n')
            print(f"Se guardaron {len(self.__libros)} libro(s) en {self.__archivo}")
        except Exception as e:
            print(f"Error al guardar archivo: {e}")
            
            
def menu_principal():
    biblioteca = Biblioteca()
    
    while True:
        print("\n" + "="*50)
        print("GESTOR DE BIBLIOTECA")
        print("="*50)
        print("1. Agregar libro físico")
        print("2. Agregar libro digital")
        print("3. Eliminar libro")
        print("4. Ver todos los libros")
        print("5. Ver libros disponibles")
        print("6. Buscar libro")
        print("7. Marcar libro como prestado")
        print("8. Devolver libro")
        print("9. Salir")
        print("="*50)
        
        try:
            opcion = input("Elige una opción: ").strip()
            
            if opcion == "1":
                print("\n--- AGREGAR LIBRO FÍSICO ---")
                titulo = input("Título: ").strip()
                autor = input("Autor: ").strip()
                anio = int(input("Año de publicación: ").strip())
                biblioteca.agregar_libro(Libro(titulo, autor, anio))
                
            elif opcion == "2":
                print("\n--- AGREGAR LIBRO DIGITAL ---")
                titulo = input("Titulo: ").strip()
                autor = input("Autor: ").strip()
                anio = int(input("Año de publicación: ").strip())
                formato = input("Formato (PDF, ePub, MOBI, etc.): ").strip()
                biblioteca.agregar_libro(LibroDigital(titulo, autor, anio, formato))
                
            elif opcion == "3":
                titulo = input("\nTítulo del libro a eliminar: ").strip()
                biblioteca.eliminar_libro(titulo)
                
            elif opcion == "4":
                biblioteca.listar_libros()
                
            elif opcion == "5":
                biblioteca.listar_disponibles()
                
            elif opcion == "6":
                titulo = input("\nTítulo del libro a buscar: ").strip()
                libro = biblioteca.buscar_libro(titulo)
                tipo = "[DIGITAL]" if isinstance(libro, LibroDigital) else "[FÍSICO]"
                print(f"\n Libro encontrado:\n {tipo} {libro}")
                
            elif opcion == "7":
                titulo = input("\nTítulo del libro a prestar: ").strip()
                biblioteca.marcar_prestado(titulo)
                
            elif opcion == "8":
                titulo = input("\nTítulo del libro a devolver: ").strip()
                biblioteca.devolver_libro(titulo)
                
            elif opcion == "9":
                print("\n--- GUARDANDO CAMBIOS ---")
                biblioteca.guardar_en_archivo()
                print("\n¡Hasta pronto!")
                break
            
            else:
                print("\n Opción inválida. Por favor, elige una opción del 1 al 9.")
                
        except ValueError as e:
            print(f"\n Error de valor: {e}")
        except Exception as e:
            print(f"'n Error: {e}")
            
            
if __name__ == "__main__":
    menu_principal() 
            
                            