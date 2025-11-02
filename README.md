# 📚 Sistema de Gestión de Biblioteca

Sistema de gestión de biblioteca en Python con POO y persistencia de datos.

## 🎯 Características

- Gestión de libros físicos y digitales
- Préstamos y devoluciones
- Búsqueda por título
- Datos guardados en `biblioteca.txt`

## 🚀 Uso

```bash
python gestor_biblioteca.py
```

### Menú
1. Agregar libro físico
2. Agregar libro digital
3. Eliminar libro
4. Ver todos los libros
5. Ver libros disponibles
6. Buscar libro
7. Marcar como prestado
8. Devolver libro
9. Salir (guarda cambios)

## 📁 Formato de Archivo

**Libro físico:**
```
Don Quijote|Miguel de Cervantes|1605|disponible
```

**Libro digital:**
```
DIGITAL|Clean Code|Robert C. Martin|2008|disponible|PDF
```

## 🏗️ Clases

- **`Libro`**: Clase base (título, autor, año, estado)
- **`LibroDigital`**: Hereda de Libro (+ formato)
- **`Biblioteca`**: Gestiona la colección

## 🎓 POO Implementado

- ✅ Encapsulación (atributos privados)
- ✅ Herencia (LibroDigital ← Libro)
- ✅ Polimorfismo (sobrescritura de métodos)
- ✅ Manejo de excepciones

## 📋 Requisitos

- Python 3.6+
- Sin librerías externas

---

**Nota**: El archivo `biblioteca.txt` se crea automáticamente la primera vez que uses el programa.
