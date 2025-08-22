class Menus:
    def menu(self):
        print("\nBIENVENIDO AL MENÚ DE BEAUTIFUL ROSE")
        print("[1] Registro de productos")
        print("[2] Registro de empleados")
        print("[3] Compra de productos")
        print("[4] venta de productos")
        print("[5] Salir del menú")

class BaseDatos:
    productos = {}
    categorias = {}
    clientes = {}
    empleados = {}
    proveedores = {}
    ventas = {}
    compras = {}
    detalles_venta = {}
    detalles_compra = {}

class Producto:
    def __init__(self, id_producto, nombre, id_categoria, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.id_categoria = id_categoria
        self.precio = precio
        self.stock = stock
        self.total_compras = 0
        self.total_ventas = 0

        BaseDatos.productos[self.id_producto] = self

    def actualizar_stock(self, cantidad, operacion):
        if operacion == 'compra':
            self.stock += cantidad
            self.total_compras += cantidad
        elif operacion == 'venta':
            self.stock -= cantidad
            self.total_ventas += cantidad

class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre
        BaseDatos.categorias[self.id_categoria] = self

class Cliente:
    def __init__(self, nit, nombre,telefono, direccion, correo):
        self.nit = nit
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        BaseDatos.clientes[self.nit] = self
class Empleado:
    def __init__(self, id_empleado, nombre, telefono, direccion, correo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        BaseDatos.empleados[self.id_empleado] = self