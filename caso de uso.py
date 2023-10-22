class Usuario:
    def __init__(self):
        self.base_de_datos_usuarios = {}

    def crear_usuario(self, nombre, correo, contraseña):
        if correo not in self.base_de_datos_usuarios:
            self.base_de_datos_usuarios[correo] = {
                "nombre": nombre,
                "contraseña": contraseña
            }
            return True
        else:
            return False

# Uso del caso de uso
usuario_sistema = Usuario()

nombre = input("Ingrese su nombre: ")
correo = input("Ingrese su correo electrónico: ")
contraseña = input("Ingrese su contraseña: ")

if usuario_sistema.crear_usuario(nombre, correo, contraseña):
    print("¡Usuario creado con éxito!")
else:
    print("El correo electrónico ingresado ya está en uso. Por favor, utilice otro correo electrónico.")
