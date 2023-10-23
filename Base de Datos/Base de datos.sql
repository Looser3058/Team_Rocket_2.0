CREATE DATABASE tiendaAnimati_BD;
use tiendaAnimati_BD;


CREATE TABLE `Cliente` (
  `DNI` int (8) primary key not null,
  `Correo_Electronico` VARCHAR (25),
  `Nombre` varchar (30),
  `Apellido` varchar (30),
  `Direccion` varchar (40),
  `Telefono` int (20)
);


Insert into Cliente (DNI, Correo_Electronico, Nombre, Apellido, Direccion, Telefono)
values
 (45345678, "juanito_perez@gmail.com", "Juan", "Perez", "Velez Sarfield 45",351405598),
 (40456789, "maria_diaz@gmail.com", "Maria", "Diaz", "Av Color 1500",351579913),
 (35567019, "esteban_lopez@gmail.com", "Esteban", "Lopez", "Simon Bolivar 560", 351506798);

-- --------------------------------------------------------

CREATE TABLE `Pedidos` (
  `Nro_pedido` int key auto_increment,
  `ID_Producto` int, foreign key (`ID_Producto`) references Producto(`ID_Producto`),
  `DNI` int, foreign key(`DNI`) references Cliente (DNI) constraint `pedido`,
  `Cantidad` int
);

INSERT INTO Pedidos (Nro_pedido, ID_Producto, DNI,Cantidad)
values ( 1, 010, 35567019, 3), (2, 005, 40456789, 1), (3, 015, 45345678,2);

-- --------------------------------------------------------

CREATE TABLE `Producto` (
  `ID_Producto` int primary key,
  `Nombre_Producto` VARCHAR (25),
  `Precio` int,
  `Stock` int,
  `Nro_categoria` int, foreign key (`Nro_categoria`) references Categoria(`Nro_categoria`)
);

Insert into Producto (ID_Producto, Nombre_producto, precio, Stock,`Nro_categoria`)
values 
(001, "Posters",  200, 30, 1),
(002, "Polaroid",  50, 400, 2),
(003, "Stickers",  80, 400, 1),
(004, "Stickers Holograficos", 200, 150, 2),
(005, "Imanes", 150, 100, 1),
(006, "Cuadernos", 600, 20, 2),
(007, "Lapiceras", 300, 5, 2),
(008, "Señaladores", 300, 15, 2),
(009, "Anotadores", 200, 5, 2),
(010, "Aritos", 400, 30, 2),
(011, "Llaveros", 400, 30, 1),
(015, "Collares", 500, 10, 1),
(016, "Vasos", 1000, 5, 1);


-- --------------------------------------------------------
CREATE TABLE `Categoria` (
  `Nro_categoria` int primary key auto_increment,
  `Nombre_categoria` varchar (30),
  `Descripcion_categoria` varchar (30)
);

INSERT INTO Categoria(Nro_categoria,Nombre_categoria,Descripcion_categoria)
VALUES ( 1, "Papeleria", "hojas y cuadernos"), (2, "Accesorios", "mucha variedad de Accesorios" );

-- --------------------------------------------------------

-- --------------------------------------------------------
CREATE TABLE `Usuario` (
  `ID_Usuario` int primary key auto_increment,
  `Nombre_Usuario` varchar (30),
  `Correo_Usuario` varchar (30),
  `Numero_Telefono` varchar (30)
);

INSERT INTO Usuario (ID_Usuario,Nombre_Usuario,Correo_Usuario,Numero_Telefono)
VALUES ( 1, "Pedro", "Pepedro@hotmail.com", 351876512), (2, "naty", "naty02@hotmail.com", 2451123222 );

-- --------------------------------------------------------

/* 1) corregi nombre de atributos, la tabla producto guardara el id de la categoria y no un nombre para hacer la relacion. 
   2) cree tabla categoria.
   3) quite en la tabla Cliente el `Nro_pedido`con clave foránea a Pedido, ya que cuando carguemos el pedido traera el cliente y no al reves
   4) agregue clave foranea a pedido , con cliente a traves de su DNI.
   5) agregue los atributo fecha y cantidad a la tabla pedidos.
   6) Agregue tabla usuario.

*/