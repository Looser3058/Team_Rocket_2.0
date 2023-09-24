# main.py

from usuarios import Usuario
from productos import Producto
from productos import categoria
from pedidos import Pedidos # Usuariosusuario1 = Usuario("Juan Perez", "juanito_perez@gmail.com", "Velez Sarfield 45", 3514055987)
usuario2 = Usuario("Maria Diaz", "maria_diaz@gmail.com", "Av Color 1500", 351579135)
usurio3 = Usuario("Esteban Lopez", "esteban_lopez@gmail.com", "Simon Bolivar 560", 3515067981)

# Crear productos
producto001 = Producto("Posters", 200, categoria[0], 30)
producto002 = Producto("Polaroid", 50, categoria[0], 400)
producto003 = Producto("Stickers", 80, categoria[0], 400)
producto004 = Producto("Stickers Holograficos", 200, categoria[0], 150)
producto005 = Producto("Imanes", 150, categoria[0], 100)
producto006 = Producto("Cuadernos", 600, categoria[0], 20)
producto007 = Producto("Lapiceras", 300, categoria[0], 5)
producto008 = Producto("Señaladores", 300, categoria[0], 15)
producto009 = Producto("Anotadores", 200, categoria[0], 5)
producto010 = Producto("Aritos", 400, categoria[1], 30)
producto011 = Producto("Llaveros", 400, categoria[1], 30)
producto012 = Producto("Collares", 500, categoria[1], 10)
producto013 = Producto("Vasos", 1000, categoria[1], 5)

# Realizar una venta
venta = Venta(producto001, 2)


# Mostrar información
print(usuario2)
print(producto001)
print(producto002)
print(venta)
