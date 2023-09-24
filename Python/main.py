# main.py
from clientes import *
from productos import * # Usuariosusuario1 = Usuario("Juan Perez", "juanito_perez@gmail.com", "Velez Sarfield 45", 3514055987)
from pedidos import *
cliente1 = Cliente("Maria Diaz", "maria_diaz@gmail.com", "Av Color 1500", 351579135, 40496587)
cliente2 = Cliente("Esteban Lopez", "esteban_lopez@gmail.com", "Simon Bolivar 560", 3515067981, 59476465)

# Crear productos
producto001 = Producto("Posters", 200, Producto.categoria[0], 30, 1)
producto002 = Producto("Polaroid", 50, Producto.categoria[0], 400, 2)
producto003 = Producto("Stickers", 80, Producto.categoria[0], 400, 3)
producto004 = Producto("Stickers Holograficos", 200, Producto.categoria[0], 150, 4)
producto005 = Producto("Imanes", 150, Producto.categoria[0], 100, 5)
producto006 = Producto("Cuadernos", 600, Producto.categoria[0], 20, 6)
producto007 = Producto("Lapiceras", 300, Producto.categoria[0], 5, 7)
producto008 = Producto("Señaladores", 300, Producto.categoria[0], 15,8)
producto009 = Producto("Anotadores", 200, Producto.categoria[0], 5,9)
producto010 = Producto("Aritos", 400, Producto.categoria[1], 30, 10)
producto011 = Producto("Llaveros", 400, Producto.categoria[1], 30, 11)
producto012 = Producto("Collares", 500, Producto.categoria[1], 10, 12)
producto013 = Producto("Vasos", 1000, Producto.categoria[1], 5, 13)

# Realizar una venta



# Mostrar información
print(cliente1)
print(producto001)
print(producto012)

