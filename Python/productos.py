# productos.py

class Producto:
    categoria=["Papelería","Accesorios"]

    def __init__(self, nombre, precio, categoria, stock, id):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.id=id

    

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Categoria: {self.categoria}, Stock: {self.stock}, id:{self.id}"

