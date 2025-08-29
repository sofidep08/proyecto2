class Menus:
    def menu(self):
        print("\nBIENVENIDO AL MENÚ DE BEAUTIFUL ROSE")
        print("[1] Registro de empleados")
        print("[2] Administrar producto")
        print("[3] Venta de productos")
        print("[4] Salir del menú")
    def menu_administracion(self):
        print("\nBIENVENIDO AL MENÚ ADMINISTRATIVO")
        print("[1] Registro de empleados")
        print("[2] Registro de productos")
        print("[3] Registro de categorias")
        print("[4] Compra de productos")
        print("[5] Eliminar productos")
        print("[6] Productos a la venta")
        print("[7] Salir del menú")

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

class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre
        BaseDatos.categorias[self.id_categoria] = self

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

class Cliente:
    def __init__(self):
        self.cargar_cliente()
    def cargar_cliente(self):
        try:
            with open('clientes.txt', 'r', encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = archivo.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo = linea.split(":")
                        BaseDatos.clientes[nit] = {
                            "Nombre": nombre,
                            "Direccion": direccion,
                            "Telefono": telefono,
                            "Correo": correo
                        }
            print("Clientes importados desde clientes.txt")
        except FileNotFoundError:
            print("El archivo clientes aun no existe, se creara automaticamente después de guardar")

class AgregarCliente:
    def __init__(self, nit, nombre, direccion, telefono, correo):
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        BaseDatos.clientes[self.nit] = {
            "Nombre": nombre,
            "Direccion": direccion,
            "Telefono": telefono,
            "Correo": correo
        }
        self.guardar_cliente()
        print(f"Cliente con {nit} se guardo correctamente")

    def guardar_cliente (self):
        with open('clientes.txt', 'w', encoding="utf-8") as archivo:
            for nit, cliente in BaseDatos.clientes.items():
                archivo.write(f"{nit}:{cliente['Nombre']}:{cliente['Direccion']}:{cliente['Telefono']}:{cliente['Correo']}\n")

class Empleado:
    def __init__(self):
        self.cargar_empleado()
    def cargar_empleado(self):
        try:
            with open('empleados.txt', 'r', encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = archivo.strip()
                    if linea:
                        id_empleado, nombre, telefono, direccion, correo = linea.split(":")
                        BaseDatos.empleados[id_empleado] = {
                            "Nombre": nombre,
                            "Telefono": telefono,
                            "Direccion": direccion,
                            "Correo": correo
                        }
            print("Empleados importados desde empleados.txt")
        except FileNotFoundError:
            print("El archivo empleados aun no existe, se creara automaticamente después de guardar")


class AgregarEmpleado:
    def __init__(self, id_empleado, nombre, telefono, direccion, correo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        BaseDatos.empleados[self.id_empleado] ={
            "Nombre": nombre,
            "Telefono": telefono,
            "Direccion": direccion,
            "Correo": correo
        }
        self.guardar_empleado()
        print(f"Empleado con {id_empleado} se guardo correctamente")

    def guardar_empleado (self):
        with open('empleados.txt', 'w', encoding="utf-8") as archivo:
            for id_empleado, empleado in BaseDatos.empleados.items():
                archivo.write(f"{id_empleado}:{empleado['Nombre']}:{empleado['Direccion']}:{empleado['Telefono']}:{empleado['Correo']}\n")

class Proveedor:
    def __init__(self):
        self.cargar_proveedor()
    def cargar_proveedor(self):
        try:
            with open('proveedor.txt', 'r', encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = archivo.strip()
                    if linea:
                        id_proveedor, nombre, empresa, telefono, direccion, correo = linea.split(":")
                        BaseDatos.empleados[id_proveedor] = {
                            "Nombre": nombre,
                            "Empresa": empresa,
                            "Telefono": telefono,
                            "Direccion": direccion,
                            "Correo": correo
                        }
            print("Proveedores importados desde proveedores.txt")
        except FileNotFoundError:
            print("El archivo proveedores aun no existe, se creara automaticamente después de guardar")


class AgregarProveedor:
    def __init__(self, id_proveedor, nombre, empresa, telefono, direccion, correo, id_categoria):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.id_categoria = id_categoria
        BaseDatos.proveedores[self.id_proveedor] = {
            "Nombre": nombre,
            "Empresa": empresa,
            "Telefono": telefono,
            "Direccion": direccion,
            "Correo": correo
        }
        self.guardar_proveedor()
        print(f"Proveedor con {id_proveedor} se guardo correctamente")

    def guardar_proveedor (self):
        with open('proveedor.txt', 'w', encoding="utf-8") as archivo:
            for id_proveedor, proveedor in BaseDatos.proveedores.items():
                archivo.write(f"{id_proveedor}:{proveedor['Nombre']}:{proveedor['Empresa']}:{proveedor['Direccion']}:{proveedor['Telefono']}:{proveedor['Correo']}\n")

class Compra:
    def __init__(self, id_compra, fecha, id_proveedor, id_empleado):
        self.id_compra = id_compra
        self.fecha = fecha
        self.id_proveedor = id_proveedor
        self.id_empleado = id_empleado
        self.detalles_ids = []
        BaseDatos.compras[self.id_compra] = self

    def agregar_detalle(self, detalle_compra):
        BaseDatos.detalles_compra[detalle_compra.id_detalle_compra] = detalle_compra
        self.detalles_ids.append(detalle_compra.id_detalle_compra)

    def calcular_total(self):
        return sum(BaseDatos.detalles_compra[d].subtotal() for d in self.detalles_ids)


class DetalleCompra:
    def __init__(self, id_detalle_compra, id_compra, id_producto, cantidad, precio_compra, fecha_caducidad):
        self.id_detalle_compra = id_detalle_compra
        self.id_compra = id_compra
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_compra = precio_compra
        self.fecha_caducidad = fecha_caducidad

    def subtotal(self):
        return self.cantidad * self.precio_compra

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
class DetalleVenta:
    def __init__(self, id_detalle_venta, id_venta, id_producto, cantidad, precio):
        self.id_detalle_venta = id_detalle_venta
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio = precio

    def subtotal(self):
        return self.cantidad * self.precio


opcion=0
menu=Menus()
while(opcion!=4):
    try:
        menu.menu()
        opcion=int(input("Elija una opción (Ingrese números enteros solamente)"))
        if opcion in [1,2,3,4]:
            match opcion:
                case 1:
                    print("\nBIENVENIDO NUEVO EMPLEADO")
                    id_empleado=input("ID de Empleado: ")
                    if id_empleado in BaseDatos.empleados:
                        print(f"El empleado con ID {id_empleado} ya existe")
                    else:
                        nombre=input("Nombre: ")
                        telefono=int(input("Telefono: "))
                        direccion=input("Direccion: ")
                        correo=input("Correo: ")
                        nuevo_empleado= AgregarEmpleado(id_empleado, nombre, telefono, direccion, correo)
                case 2:
                    intentos=3
                    print("\nADMINISTRACION")
                    id_empleado=input("Para tener acceso ingrese el ID de Empleado: ")
                    if id_empleado in BaseDatos.empleados:
                        print("\nBIENVENIDO AL MENÚ DE ADMINISTRACIÓN")
                    else:
                        print("\nID mal ingresado o no existe un empleado con ese ID. No puede acceder")
                        print(f"{intentos-1} disponibles")
                        intentos=intentos-1
                    if intentos==0:

        else:
            print("Ingreso una opcion no valida o inexistente")
    except ValueError:
        print("Ingreso un dato incorrecto")
    if opcion!=4:
        print("Presione ENTER para continuar")
        input()