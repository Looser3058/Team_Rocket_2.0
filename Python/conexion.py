import mysql.connector

def conexion():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="1582",
    database="tiendaanimati_bd"
)
def cursor():
    database = conexion()
    db_cursor = database.cursor()

def mostrar_usuario():
    database = conexion()
    db_cursor = database.cursor()
    db_cursor.execute("SELECT * FROM Usuario")
    mostrar_cliente= db_cursor.fetchall()
    for cliente in mostrar_cliente:
        print(cliente)

def crear_usuario():
    database = conexion()
    db_cursor = database.cursor()
    nombre_usuario = input("Inserte nombre de usuario: ")
    correo_usuario = input("Insertar correo electrónico: ")
    numero_telefono = input("Insertar número de teléfono: ")
    db_cursor.execute("INSERT INTO Usuario (nombre_usuario,correo_usuario,numero_telefono) VALUES (%s,%s,%s)",
                      (nombre_usuario, correo_usuario, numero_telefono))
    database.commit()
    print("Usuario creado con éxito")

def actualizar_usuario():
    database = conexion()
    db_cursor = database.cursor()
    modificar_nombre = input("Inserte el nombre del usuario que desea actualizar: ")
    nombre_usuario = input("Inserte nombre de usuario: ")
    correo_usuario = input("Insertar correo electrónico: ")
    numero_telefono = input("Insertar número de teléfono: ")
    db_cursor.execute("UPDATE Usuario SET nombre_usuario = %s, correo_usuario = %s, numero_telefono = %s WHERE Nombre_Usuario = %s", (nombre_usuario, correo_usuario, numero_telefono, modificar_nombre))
    database.commit()
    print(db_cursor.rowcount, "Usuario modificado con éxito")

def borrar_usuario():
    database = conexion()
    db_cursor = database.cursor()
    id = input("Nombre de usuario a borrar: ")
    db_cursor.execute("DELETE FROM Usuario WHERE Nombre_Usuario = %s", (id,))
    database.commit()
    print(db_cursor.rowcount, "Usuario borrado con éxito")

def main():
    while True:
        print("1.Crear Usuario\n2.Ver Usuarios\n3.Actualizar Usuario\n4.Borrar Usuario\n5.Salir")
        eleccion= input("digite una opción: ")
        if eleccion == "1":
            crear_usuario()
        elif eleccion == "2":
            mostrar_usuario()
        elif eleccion == "3":
            actualizar_usuario()
        elif eleccion == "4":
            borrar_usuario()
        elif eleccion == "5":
            break
        else:
            print("Eleccion inválida")

if __name__ =="__main__" :
    main()

