# main.py
from usuarios import Usuario
from productos import * # Usuariosusuario1 = Usuario("Juan Perez", "juanito_perez@gmail.com", "Velez Sarfield 45", 3514055987)
from pedidos import *
usuario2 = Usuario("Maria Diaz", "maria_diaz@gmail.com", "Av Color 1500", 351579135)
usurio3 = Usuario("Esteban Lopez", "esteban_lopez@gmail.com", "Simon Bolivar 560", 3515067981)

# Crear productos
producto001 = Producto("Posters", 200, Producto.categoria[0], 30)
producto002 = Producto("Polaroid", 50, Producto.categoria[0], 400)
producto003 = Producto("Stickers", 80, Producto.categoria[0], 400)
producto004 = Producto("Stickers Holograficos", 200, Producto.categoria[0], 150)
producto005 = Producto("Imanes", 150, Producto.categoria[0], 100)
producto006 = Producto("Cuadernos", 600, Producto.categoria[0], 20)
producto007 = Producto("Lapiceras", 300, Producto.categoria[0], 5)
producto008 = Producto("Señaladores", 300, Producto.categoria[0], 15)
producto009 = Producto("Anotadores", 200, Producto.categoria[0], 5)
producto010 = Producto("Aritos", 400, Producto.categoria[1], 30)
producto011 = Producto("Llaveros", 400, Producto.categoria[1], 30)
producto012 = Producto("Collares", 500, Producto.categoria[1], 10)
producto013 = Producto("Vasos", 1000, Producto.categoria[1], 5)

# Realizar una venta



# Mostrar información
print(usuario2)
print(producto001)
print(producto002)

