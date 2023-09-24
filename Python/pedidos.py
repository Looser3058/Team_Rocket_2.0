# pedidos.py

class Pedidos:
    """Class representing a pedidos."""
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_total(self):
        """Returns the total cost of the product."""
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"Producto: {self.producto.nombre}, Cantidad: {self.cantidad}, Total: {self.calcular_total()}"
    
    def venta():
        venta
