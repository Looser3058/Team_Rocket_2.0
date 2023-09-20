CREATE DATA BASE tienda.animati_BD;
use tienda.animati_BD;

CREATE TABLE `Pedidos` (
  `Nro de pedido` Numero
);

CREATE TABLE `Cliente` (
  `DNI` Numero,
  `Correo Electronico` Email,
  `Nombre` Texto,
  `Direccion ` Texto,
  `Telefono` Numero
);

CREATE TABLE `Producto` (
  `ID del Producto` Numero,
  `Nombre del Producto` Texto,
  `Categoria` Texto,
  `Precio` Numero,
  `Stock` Numero
);

