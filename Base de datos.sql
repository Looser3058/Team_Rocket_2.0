CREATE DATA BASE tienda.animati_BD;
use tienda.animati_BD;

-- --------------------------------------------------------

CREATE TABLE `Cliente` (
  `DNI` int (8) primary key not null,
  `Correo Electronico` date (25),
  `Nombre` varchar (30),
  `Apellido` varchar (30),
  `Direccion ` varchar (40),
  `Telefono` int (10),
  `Nro_pedido` foreign key, references  Pedidos (Nro_pedido)
);

Insert into Cliente (DNI, Correo Electronico, Nombre, Apellido, Direccion, Telefono, Nro_pedido)
values
 (45345678, juanito_perez@gmail.com, Juan, Perez, Velez Sarfield 45, 3514055987, 1),
 (40456789, maria_diaz@gmail.com, Maria, Diaz, Av Color 1500, 3515799135, 2),
 (35567019, esteban_lopez@gmail.com, Esteban, Lopez, Simon Bolivar 560, 3515067981, 3);

-- --------------------------------------------------------

CREATE TABLE `Pedidos` (
  `Nro_pedido` primary key auto_incremet,
  `ID del Producto` int, foreign key, references Producto (ID del Producto)
);

Insert into Pedidos (Nro_pedido, ID del Producto)
values ( 1, 010), (2, 005), (3, 015);

-- --------------------------------------------------------

CREATE TABLE `Producto` (
  `ID del Producto` int primary key,
  `Nombre del Producto` values (25),
  `Categoria` values (20),
  `Precio` date,
  `Stock` int,
);

Insert into Producto (ID del Producto, Nombre del producto, Categoria, precio, Stock)
values 
(001, Posters, Papeleria, $200, 30),
(002, Polaroid, Papeleria, $50, 400),
(003, Stickers, Papeleria, $80, 400),
(004, Stickers Holograficos, Papeleria, $200, 150),
(005, Imanes, Papeleria, $150, 100),
(006, Cuadernos, Papeleria, $600, 20),
(007, Lapiceras, Papeleria, $300, 5),
(008, Señaladores, Papeleria, $300, 15),
(009, Toma nota, Papeleria, $200, 5),
(010, Aritos, Accesorios, $400, 30),
(011, Llaveros, Accesorios, $400, 30),
(015, Collares, Accesorios, $500, 10),
(016, Vasos, Accesorios, $1000, 5);


-- --------------------------------------------------------