# usuarios.py

class Usuario:
    """Class representing a usuario."""
    def __init__(self, nombre, correo, direccion, telefono):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Correo: {self.correo}, Telefono: {self.telefono}"

