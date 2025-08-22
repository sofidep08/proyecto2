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

class Proveedor:
    def __init__(self, id_proveedor, nombre, empresa, telefono, direccion, correo, id_categoria):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.id_categoria = id_categoria
        BaseDatos.proveedores[self.id_proveedor] = self


class Venta:
    def __init__(self, id_venta, fecha, nit_cliente, id_empleado):
        self.id_venta = id_venta
        self.fecha = fecha
        self.nit_cliente = nit_cliente
        self.id_empleado = id_empleado
        self.detalles_ids = []
        BaseDatos.ventas[self.id_venta] = self

    def agregar_detalle(self, detalle_venta):
        BaseDatos.detalles_venta[detalle_venta.id_detalle_venta] = detalle_venta
        self.detalles_ids.append(detalle_venta.id_detalle_venta)

    def calcular_total(self):
        return sum(BaseDatos.detalles_venta[d].subtotal() for d in self.detalles_ids)
