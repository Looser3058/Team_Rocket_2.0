# productos.py

class Producto:
    categoria=["Papelería","Accesorios"]

    def __init__(self, nombre, precio, categoria, stock):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    def set_categoria(self):
        return self.categoria

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Categoria: {self.categoria}, Stock: {self.stock}"

