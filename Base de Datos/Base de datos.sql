CREATE DATA BASE tienda.animati_BD;
use tienda.animati_BD;

-- --------------------------------------------------------


CREATE TABLE `Cliente` (
  `DNI` int (8) primary key not null,
  `Nombre` varchar (30),
  `Apellido` varchar (30),
  `Direccion ` varchar (40),
  `Nro de Usuario` int, foreign key, references Usuario (ID_Usuario)
);


Insert into Cliente (DNI, Nombre, Apellido, Direccion, )
values
 (45345678, Juan, Perez, Velez Sarfield 45),
 (40456789, Maria, Diaz, Av Color 1500),
 (35567019, Esteban, Lopez, Simon Bolivar 565);

-- --------------------------------------------------------

CREATE TABLE `Pedidos` (
  `Nro_pedido` primary key auto_incremet,
  `ID_Producto` int, foreign key, references Producto (ID_Producto),
  `DNI` int, foreign key, references Cliente (DNI),
  `Fecha_pedido` date,
  `Cantidad` int,
);

Insert into Pedidos (Nro_pedido, ID_Producto, DNI, Fecha_pedido, Cantidad )
values ( 1, 010, 35567019 , 10/10/2023, 3), (2, 005, 40456789, 07/10/2023, 1), (3, 015, 45345678, 15/09/2023, 2);

-- --------------------------------------------------------

CREATE TABLE `Producto` (
  `ID_Producto` int primary key,
  `Nombre_Producto` values (25),
  `Precio` int,
  `Stock` int,
  `Nro_categoria` int, foreign key, references Categoria (Nro_categoria)
);

Insert into Producto (ID_Producto, Nombre_producto, Categoria, precio, Stock,Nro_categoria)
values 
(001, Posters,  $200, 30, 1),
(002, Polaroid,  $50, 400, 2),
(003, Stickers,  $80, 400, 1),
(004, Stickers Holograficos, $200, 150, 2),
(005, Imanes, $150, 100, 1),
(006, Cuadernos, $600, 20, 2),
(007, Lapiceras, $300, 5, 2),
(008, Señaladores, $300, 15, 2),
(009, Anotadores, $200, 5, 2),
(010, Aritos, $400, 30, 2),
(011, Llaveros, $400, 30, 1),
(015, Collares, $500, 10, 1),
(016, Vasos, $1000, 5, 1);


-- --------------------------------------------------------
CREATE TABLE `Categoria` (
  `Nro_categoria` primary key auto_incremet,
  `Nombre_categoria` varchar (30),
  `Descripcion_categoria` varchar (30),
  `ID_Producto` int, foreign key, references Producto (Id_Producto)

 
);

Insert into Categoria (Nro_categoria,Nombre_categoria,Descripcion_categoria)
values ( 1, Papeleria, hojas y cuadernos), (2, Accesorios, aritos collares y elementos de uso ), ;

-- --------------------------------------------------------

-- --------------------------------------------------------
CREATE TABLE `Usuario` (
  `ID_Usuario` primary key auto_incremet,
  `Nombre_Usuario` varchar (30),
  `Correo_Usuario` varchar (30),
  `Numero_Telefono` varchar (30),

);

Insert into Usuario (ID_Usuario,Nombre_Usuario,Correo_Usuario,Numero_Telefono)
values ( 1, Pedro, Pepedro@hotmail.com, 351876512), (2, naty, naty02@hotmail.com, 2451123222 ), ;

-- --------------------------------------------------------

/* 1) corregi nombre de atributos, la tabla producto guardara el id de la categoria y no un nombre para hacer la relacion. 
   2) cree tabla categoria.
   3) quite en la tabla Cliente el `Nro_pedido`con clave foránea a Pedido, ya que cuando cargemos el pedido traera el cliente y no al revez
   4) agrege clave foranea a pedido , con cliente a traves de su DNI.
   5) agrege los atributo fecha y cantidad a la tabla pedidos.
   6) Agrege tabla usuario.

*/

/* 1) Se quito los atributos "correo electronico" y "telefono" de la tabla cliente, ya que los mismos aparecen de nuevo en la tabla usuario.
   2) Se agrego clave foranea a las tablas Categoria y cliente. 
*/
