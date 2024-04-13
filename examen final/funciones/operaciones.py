from conexiones.conexion_db import conectar_db
from models.clases import Productos, Trabajadores, Proveedores


def insertar_producto(id_producto, nombre, fecha_ingreso, fecha_vencimiento):
    db = conectar_db()
    cursor = db.cursor()
    sql = "INSERT INTO productos (id_producto, nombre, fecha_ingreso, fecha_vencimiento) VALUES (%s, %s, %s, %s)"
    val = (id_producto, nombre, fecha_ingreso, fecha_vencimiento) 
    cursor.execute(sql, val) 
    db.commit()
    print("los campos del producto se a ingresado a la BD.")
    db.close()

def buscar_producto(nombre):
    db = conectar_db()
    cursor = db.cursor()
    sql = "SELECT * FROM productos WHERE nombre = %s"
    val = (nombre,)
    cursor.execute(sql, val)
    resultado = cursor.fetchall()
    for producto in resultado:
        print(producto)
    db.close()

def mostrar_productos():
    db = conectar_db()
    cursor = db.cursor()
    sql = "SELECT * FROM productos"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for producto in resultado:
        print(producto)
    db.close()

def eliminar_producto(id_producto):
    db = conectar_db()
    cursor = db.cursor()
    sql = "DELETE FROM productos WHERE id_producto = %s"
    val = (id_producto,)
    cursor.execute(sql, val)
    db.commit()
    print("El Producto se a eliminado de la BD")
    db.close()

def actualizar_fecha_vencimiento(id_producto, nueva_fecha_vencimiento):
    db = conectar_db()
    cursor = db.cursor()
    sql = "UPDATE productos SET fecha_vencimiento = %s WHERE id_producto = %s"
    val = (nueva_fecha_vencimiento, id_producto)
    cursor.execute(sql, val)
    db.commit()
    print("Fecha de vencimiento se a actualizado a la BD.")
    db.close()

def insertar_trabajador(id_trabajador, nombre, cargo):
    db = conectar_db()
    cursor = db.cursor()
    sql = "INSERT INTO trabajadores (id_trabajador, nombre, cargo) VALUES (%s, %s, %s)"
    val = (id_trabajador, nombre, cargo)
    cursor.execute(sql, val)
    db.commit()
    print("A insertado correctamente los campos del trabajdor a la BD")
    db.close()

def insertar_proveedor(id_proveedor, nombre, nombre_vendedor, direccion, telefono):
    db = conectar_db()
    cursor = db.cursor()
    sql = "INSERT INTO proveedores (id_proveedor, nombre, nombre_vendedor, direccion, telefono) VALUES (%s, %s, %s, %s, %s)"
    val = (id_proveedor, nombre, nombre_vendedor, direccion, telefono)
    cursor.execute(sql, val)
    db.commit()
    print("A insertado correctamente los campos del Proveedor a la BD")
    db.close()

def menu():
    while True: 
        print("\n|BIENVENIDO AL MENÚ DE REGISTRO DE INVENTARIO|")
        print("|-------------FARMACIA BIENESTAR-------------|")
        print("1. Insertar producto")
        print("2. Buscar producto")
        print("3. Mostrar todos los productos")
        print("4. Eliminar producto")
        print("5. Actualizar fecha de vencimiento")
        print("6. Insertar trabajador")
        print("7. Insertar proveedor")
        print("8. Salir")
        opcion = input("ingrese una opción:\n ")
        if opcion == "1":
            id_producto = input("Ingrese ID del producto\n ")
            nombre = input("Ingrese nombre del producto\n ")
            fecha_ingreso = input("Ingrese fecha de ingreso (YYYY-MM-DD)\n ")
            fecha_vencimiento = input("Ingrese fecha de vencimiento (YYYY-MM-DD\n ")
            insertar_producto(id_producto, nombre, fecha_ingreso, fecha_vencimiento)
        elif opcion == "2":
            nombre = input("Ingrese nombre del producto que desea buscar\n")
            buscar_producto(nombre)
        elif opcion == "3":
            mostrar_productos()
        elif opcion == "4":
            id_producto = input("Ingrese ID del producto que desea eliminar\n ")
            eliminar_producto(id_producto)
        elif opcion == "5":
            id_producto = input("Ingrese ID del producto que va a actualizar: ")
            nueva_fecha_vencimiento = input("Ingrese nueva fecha de vencimiento (YYYY-MM-DD)\n ")
            actualizar_fecha_vencimiento(id_producto, nueva_fecha_vencimiento)
        elif opcion == "6":
            id_trabajador = input("Ingrese ID del trabajador\n ")
            nombre = input("Ingrese el nombre del trabajador\n ")
            cargo = input("Ingrese el cargo del trabajador\n ")
            insertar_trabajador(id_trabajador, nombre, cargo)
        elif opcion == "7":
            id_proveedor = input("Ingrese ID del proveedor: ")
            nombre = input("Ingrese el nombre del proveedor: ")
            nombre_vendedor = input("Ingrese el nombre del vendedor: ")
            direccion = input("Ingrese la dirección del proveedor: ")
            telefono = input("Ingrese el teléfono del proveedor: ")
            insertar_proveedor(id_proveedor, nombre, nombre_vendedor, direccion, telefono)
        elif opcion == "8":
            print("TE ESPERAMOS PRONTO")
            break
        else:
            print("OPCION INGRESADA NO ES CORRECTA, INGRESE LA OPCION CORRETA DEL 1-8")
