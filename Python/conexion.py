import mysql.connector

def conexion():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="1582",
    database="tiendaanimati_bd"
)


def mostrar_producto():
    database = conexion()
    db_cursor = database.cursor()
    db_cursor.execute("SELECT * FROM Producto")
    mostrar_producto= db_cursor.fetchall()
    for producto in mostrar_producto:
        print(producto)

def agregar_producto():
    database = conexion()
    db_cursor = database.cursor()
    nombre_producto = input("Inserte nombre de producto: ")
    precio_producto = int(input("Insertar precio del producto: "))
    stock_producto = int(input("Insertar número de stock disponible: "))
    categoria_producto = int(input("Ingrese el número de categoría del producto (1 o 2): "))
    db_cursor.execute("INSERT INTO Producto (Nombre_Producto, Precio, Stock, Nro_categoria) VALUES (%s,%s,%s,%s)",
                      (nombre_producto, precio_producto, stock_producto, categoria_producto))
    database.commit()
    print("Producto agregado con éxito")

def modificar_producto():
    database = conexion()
    db_cursor = database.cursor()
    cambio_producto = input("Inserte el nombre del producto que desea modificar: ")
    nombre_producto = input("Inserte nuevo nombre de producto: ")
    precio_producto = int(input("Insertar precio del producto: "))
    stock_producto = int(input("Insertar número de stock disponible: "))
    categoria_producto = int(input("Ingrese el número de categoría del producto (1 o 2): "))
    db_cursor.execute("UPDATE Producto SET Nombre_Producto = %s, Precio = %s, Stock = %s, Nro_categoria = %s WHERE Nombre_Producto = %s", (nombre_producto, precio_producto, stock_producto, cambio_producto, categoria_producto))
    database.commit()
    print(db_cursor.rowcount, "Producto modificado con éxito")

def borrar_producto():
    database = conexion()
    db_cursor = database.cursor()
    id = input("Nombre de producto a borrar: ")
    db_cursor.execute("DELETE FROM Producto WHERE Nombre_Producto = %s", (id,))
    database.commit()
    print(db_cursor.rowcount, "Producto borrado con éxito")

def main():
    while True:
        print("1.Agregar producto\n2.Ver Productos\n3.Modificar producto\n4.Borrar producto\n5.Salir")
        eleccion= input("digite una opción: ")
        if eleccion == "1":
            agregar_producto()
        elif eleccion == "2":
            mostrar_producto()
        elif eleccion == "3":
            modificar_producto()
        elif eleccion == "4":
            borrar_producto()
        elif eleccion == "5":
            break
        else:
            print("Eleccion inválida")

if __name__ =="__main__" :
    main()

