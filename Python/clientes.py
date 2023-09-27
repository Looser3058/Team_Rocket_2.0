# usuarios.py

class Cliente:
    
    def __init__(self, nombre, correo, direccion, telefono, dni):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.dni= dni

    def __str__(self):
        return f"Nombre: {self.nombre}, Correo: {self.correo}, Telefono: {self.telefono}, dni:{self.dni}"

