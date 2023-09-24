# main.py

from usuarios import Usuario
from productos import Producto
from pedidos import Pedidos

# Usuarios
usuario1 = Usuario("Juan", "juan@example.com")
usuario2 = Usuario("María", "maria@example.com")

# Crear productos
producto001 = Producto("Posters", 200, Papeleria, 30)
producto002 = Producto("Polaroid", 50, Papeleria, 400)
producto003 = Producto("Stickers", 80, Papeleria, 400)
producto004 = Producto("Stickers Holograficos", 200, Papeleria, 150)
producto005 = Producto("Imanes", 150, Papeleria, 100)
producto006 = Producto("Cuadernos", 600, Papeleria, 20)
producto007 = Producto("Lapiceras", 300, Papeleria, 5)
producto008 = Producto("Señaladores", 300, Papeleria, 15)
producto009 = Producto("Anotadores", 200, Papeleria, 5)
producto010 = Producto("Aritos", 400, Accesorios, 30)
producto011 = Producto("Llaveros", 400, Accesorios, 30)
producto012 = Producto("Collares", 500, Accesorios, 10)
producto013 = Producto("Vasos", 1000, Accesorios, 5)

# Realizar una venta
venta = Venta(producto001, 2)

# Mostrar información
print(usuario1)
print(usuario2)
print(producto001)
print(producto002)
print(venta)
