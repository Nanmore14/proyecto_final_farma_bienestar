class Productos:
    def __init__(self, id_producto, nombre, fecha_ingreso, fecha_vencimiento):
        self.id_producto = id_producto 
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso
        self.fecha_vencimiento = fecha_vencimiento

class Trabajadores:
    def __init__(self, id_trabajador, nombre, cargo):
        self.id_trabajador = id_trabajador
        self.nombre = nombre
        self.cargo = cargo

class Proveedores:
    def __init__(self, id_proveedor, nombre, nombre_vendedor, direccion, telefono):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.nombre_vendedor = nombre_vendedor
        self.direccion = direccion
        self.telefono = telefono
