class Menus:
    def menu(self):
        print("\nBIENVENIDO AL MENÚ DE BEAUTIFUL ROSE")
        print("[1] Registro de empleados")
        print("[2] Registro de proveedores")
        print("[3] Administrar producto")
        print("[4] Venta de productos")
        print("[5] Salir del menú")
    def menu_administracion(self):
        print("\nBIENVENIDO AL MENÚ ADMINISTRATIVO")
        print("[1] Registro de categorias")
        print("[2] Registro de productos")
        print("[3] Compra de productos")
        print("[4] Productos a la venta")
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

class Categoria:
    def __init__(self):
        self.cargar_categoria()
    def cargar_categoria(self):
        try:
            with open('categoria.txt', 'r', encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_categoria, nombre = linea.split(":")
                        BaseDatos.categorias[id_categoria] = {
                            "Nombre": nombre
                        }
            print("Categoria importados desde categoria.txt")
        except FileNotFoundError:
            print("El archivo categoria aun no existe, se creara automaticamente después de guardar")

class AgregarCategoria:
    def __init__(self, nombre):
        self.id_categoria = str(len(BaseDatos.categorias) + 1)
        self.nombre = nombre
        BaseDatos.categorias[self.id_categoria] = {
            "Nombre": nombre
        }
        self.guardar_categoria()
        print("Se guardo la categoria")

    def guardar_categoria (self):
        with open('categoria.txt', 'w', encoding="utf-8") as archivo:
            for id_categoria, categoria in BaseDatos.categorias.items():
                archivo.write(f"{id_categoria}:{categoria['Nombre']}\n")

class MostrarCategoria:
    @staticmethod
    def mostrar_categoria():

        print("\nLISTADO DE CATEGORIAS")
        for id_categoria, categoria in BaseDatos.categorias.items():
            print(f"ID: {id_categoria}: Nombre: {categoria['Nombre']}")


class Producto:
    def __init__(self):
        self.cargar_producto()
    def cargar_producto(self):
        try:
            with open('producto.txt', 'r', encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_producto, nombre, id_categoria, precio, stock, total_compras, total_ventas = linea.split(":")
                        BaseDatos.productos[id_producto] = {
                            "Nombre": nombre,
                            "id_categoria": id_categoria,
                            "Precio": float(precio),
                            "Stock": int(stock),
                            "total_compras": int(total_compras),
                            "total_ventas": int(total_ventas)

                        }
            print("Productos importados desde producto.txt")
        except FileNotFoundError:
            print("El archivo producto aun no existe, se creara automaticamente después de guardar")


class AgregarProducto:
    def __init__(self, id_categoria, nombre, precio, stock):
        self.id_producto = f"{id_categoria}-{len(BaseDatos.productos) + 1000}"
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.total_compras = 0
        self.total_ventas = 0

        BaseDatos.productos[self.id_producto] = {
            "Nombre": nombre,
            "id_categoria": id_categoria,
            "Precio": precio,
            "Stock": stock,
            "total_compras": self.total_compras,
            "total_ventas": self.total_ventas
        }
        self.guardar_producto()
        print("Se guardo el producto")

    def guardar_producto(self):
        with open('producto.txt', 'w', encoding="utf-8") as archivo:
            for id_producto, productos in BaseDatos.productos.items():
                archivo.write(f"{id_producto}:{productos['Nombre']}:{productos['id_categoria']}:"
                    f"{productos['Precio']}:{productos['Stock']}:{productos['total_compras']}:{productos['total_ventas']}\n")


class MostrarProducto:
    @staticmethod
    def mostrar_producto():

        print("\nLISTADO DE PRODUCTOS")
        for id_producto, productos in BaseDatos.productos.items():
            print(f"ID: {id_producto} | Nombre: {productos['Nombre']} | ID de categoria: {productos['id_categoria']} | precio: {productos['Precio']} | Stock{productos['Stock']} | Compras: {productos['total_compras']} | Total de ventas: {productos['total_ventas']}\n")

class Ordenamiento:
    @staticmethod
    def quicksort_productos(lista_productos):
        if len(lista_productos) <= 1:
            return lista_productos
        else:
            pivote = lista_productos[0]
            menor = [x for x in lista_productos[1:] if x[1].get("id_categoria", "") <= pivote[1].get("id_categoria", "")]
            mayor = [x for x in lista_productos[1:] if x[1].get("id_categoria", "") > pivote[1].get("id_categoria", "")]
            return Ordenamiento.quicksort_productos(menor) + [pivote] + Ordenamiento.quicksort_productos(mayor)


class Cliente:
    def __init__(self):
        self.cargar_cliente()
    def cargar_cliente(self):
        try:
            with open('clientes.txt', 'r', encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
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
        print(f"Cliente con NIT {nit} se guardo correctamente")

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
                    linea = linea.strip()
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
        print(f"Empleado con ID {id_empleado} se guardo correctamente")

    def guardar_empleado (self):
        with open('empleados.txt', 'w', encoding="utf-8") as archivo:
            for id_empleado, empleado in BaseDatos.empleados.items():
                archivo.write(f"{id_empleado}:{empleado['Nombre']}:{empleado['Telefono']}:{empleado['Direccion']}:{empleado['Correo']}\n")

class Proveedor:
    def __init__(self):
        self.cargar_proveedor()
    def cargar_proveedor(self):
        try:
            with open('proveedor.txt', 'r', encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_proveedor, nombre, empresa, telefono, direccion, correo,id_categoria = linea.split(":")
                        BaseDatos.proveedores[id_proveedor] = {
                            "Nombre": nombre,
                            "Empresa": empresa,
                            "Telefono": telefono,
                            "Direccion": direccion,
                            "Correo": correo,
                            "id_categoria": id_categoria
                        }
            print("Proveedores importados desde proveedor.txt")
        except FileNotFoundError:
            print("El archivo proveedor aun no existe, se creara automaticamente después de guardar")


class AgregarProveedor:
    def __init__(self, id_proveedor, nombre, empresa, telefono, direccion, correo,id_categoria):
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
            "Correo": correo,
            "id_categoria": id_categoria
        }
        self.guardar_proveedor()
        print(f"Proveedor con ID {id_proveedor} se guardo correctamente")

    def guardar_proveedor (self):
        with open('proveedor.txt', 'w', encoding="utf-8") as archivo:
            for id_proveedor, proveedor in BaseDatos.proveedores.items():
                archivo.write(f"{id_proveedor}:{proveedor['Nombre']}:{proveedor['Empresa']}:{proveedor['Telefono']}:{proveedor['Direccion']}:{proveedor['Correo']}:{proveedor['id_categoria']}\n")

class MostrarProveedor:
    @staticmethod
    def mostrar_proveedor():
        print("\nLISTADO DE PROVEEDORES")
        for id_proveedor, provedor in BaseDatos.proveedores.items():
            print(f"ID: {id_proveedor}: Nombre: {provedor['Nombre']} :{provedor['Empresa']} :{provedor['Telefono']}:{provedor['Direccion']}:{provedor['Correo']}\n")

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


Categoria()
Producto()
Cliente()
Empleado()
Proveedor()
opcion=0
menu=Menus()
while(opcion!=5):
    try:
        menu.menu()
        opcion=int(input("Elija una opción (Ingrese números enteros solamente): "))
        if opcion in [1,2,3,4,5]:
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
                    print("\nBIENVENIDO NUEVO PROVEEDOR")
                    if not BaseDatos.categorias:
                        print("No hay categorias registradas. ingrese primero una categoria")
                    else:
                        print("CATEGORIAS DISPONIBLES")
                        MostrarCategoria.mostrar_categoria()
                        id_categoria = input("Ingrese la categoria que vende el proveedor: ")
                        if id_categoria not in BaseDatos.categorias:
                            print("Categoría no válida")
                        else:
                            id_proveedor=input("ID de Proveedor: ")
                            if id_proveedor in BaseDatos.proveedores:
                                print(f"El proveedor con ID {id_proveedor} ya existe")
                            else:
                                nombre=input("Nombre: ")
                                empresa=input("Empresa: ")
                                telefono=int(input("Telefono: "))
                                direccion=input("Direccion: ")
                                correo=input("Correo: ")
                                nuevo_proveedor= AgregarProveedor(id_proveedor, nombre, empresa, telefono, direccion, correo, id_categoria)
                case 3:
                    intentos=3
                    while intentos!=0:
                        print("\nADMINISTRACION")
                        id_empleado=input("Para tener acceso ingrese el ID de Empleado: ")
                        if id_empleado in BaseDatos.empleados:
                            while True:
                                menu.menu_administracion()
                                opcion2 = int(input("Elija una opción (Ingrese números enteros solamente)"))
                                if opcion2 in [1, 2, 3, 4, 5]:
                                    match opcion2:
                                        case 1:
                                            print("REGISTRO DE CATEGORIAS")
                                            nombre=input("Nombre de la categoria: ")

                                            if any(categoria["Nombre"].lower() == nombre.lower() for categoria in
                                                   BaseDatos.categorias.values()):
                                                print("La categoría ingresada ya existe")

                                            else:
                                                nueva_categoria = AgregarCategoria(nombre)
                                        case 2:
                                            if not BaseDatos.categorias:
                                                print("No hay categorias registradas. ingrese primero una categoria")
                                            else:
                                                MostrarCategoria.mostrar_categoria()
                                                produc_categoria=input("Ingrese el id de la categoria: ")
                                                if produc_categoria not in BaseDatos.categorias:
                                                    print("La categoria ingresada no existe")
                                                else:
                                                    nombre = input("Nombre del producto: ")
                                                    precio = float(input("Precio del producto: "))
                                                    stock = int(input("Cantidad inicial en stock: "))
                                                    nuevo_producto = AgregarProducto(produc_categoria,nombre, precio, stock)
                                                    print("Producto Guardado")
                                        case 3:
                                            if not BaseDatos.productos:
                                                print("No hay productos registrados. Primero registre un producto")
                                            elif not BaseDatos.proveedores:
                                                print("No hay proveedores registrados. Primero registre un proveedor")
                                            else:
                                                MostrarProducto.mostrar_producto()
                                                id_producto = input("Ingrese el id del producto que desea comprar: ")
                                                if id_producto not in BaseDatos.productos:
                                                    print("Producto ingresado no existe")
                                                else:
                                                    MostrarProveedor.mostrar_proveedor()
                                                    id_proveedor = input("Ingrese el ID del proveedor: ")
                                                    if id_proveedor not in BaseDatos.proveedores:
                                                        print("Proveedor no existe")
                                                    else:
                                                        producto = BaseDatos.productos[id_producto]
                                                        proveedor = BaseDatos.proveedores[id_proveedor]
                                                        if producto["id_categoria"] != proveedor["id_categoria"]:
                                                            print("El proveedor no vende esta categoría de producto")
                                                        else:
                                                            cantidad = int(input("Ingrese la cantidad a comprar: "))
                                                            precio = float(input("Ingrese el precio de compra por unidad: "))
                                                            fecha = input("Ingrese la fecha de la compra (DD/MM/AAAA): ")

                                                            id_compra = len(BaseDatos.compras) + 1
                                                            nueva_compra = Compra(id_compra, fecha, id_proveedor,id_empleado)

                                                            id_detalle_compra = len(BaseDatos.detalles_compra) + 1
                                                            detalle = DetalleCompra(id_detalle_compra, id_compra, id_producto,cantidad, precio, fecha)
                                                            nueva_compra.agregar_detalle(detalle)

                                                            BaseDatos.productos[id_producto]["Stock"] += cantidad
                                                            BaseDatos.productos[id_producto]["total_compras"] += cantidad
                                                            print(f"Compra registrada correctamente. Producto {id_producto} abastecido con {cantidad} unidades.")
                                        case 4:
                                            if not BaseDatos.productos:
                                                print("No hay productos registrados.")
                                            else:
                                                lista_productos = list(BaseDatos.productos.items())
                                                productos_ordenados = Ordenamiento.quicksort_productos(lista_productos)

                                                print("\nPRODUCTOS A LA VENTA (ordenados por categoria):")
                                                for id_producto, producto in productos_ordenados:
                                                    print(f"ID: {id_producto} : Nombre: {producto['Nombre']} ")
                                                    print(f"Categoría: {producto['id_categoria']} : Precio: {producto['Precio']}")
                                                    print(f"Stock: {producto['Stock']} : Total Compras: {producto['total_compras']}")
                                                    print(f"Total Ventas: {producto['total_ventas']}")
                                        case 5:
                                            print("Volviendo al menú principal...")
                                            break
                                else:
                                    print("Ingreso una opcion no valida o inexistente")
                            break
                        else:
                            print("\nID mal ingresado o no existe un empleado con ese ID. No puede acceder")
                            print(f"{intentos-1} Intentos disponibles")
                            intentos=intentos-1
                        if intentos==0:
                            print("\nIntentos terminados, volviendo al menú principal...")
                case 4:
                    if not BaseDatos.productos:
                        print("No hay productos registrados para la venta")
                    else:
                        print("\nVENTA DE PRODUCTOS")
                        print("Productos disponibles:\n")
                        for id_producto, producto in BaseDatos.productos.items():
                            print(
                                f"ID: {id_producto} - {producto['Nombre']} | Precio: {producto['Precio']} | Stock: {producto['Stock']}")

                        carrito = {}
                        while True:
                            id_producto = input("\nIngrese el ID del producto a comprar (0 para terminar): ")
                            if id_producto == "0":
                                break
                            if id_producto not in BaseDatos.productos:
                                print("Producto no válido")
                                continue

                            cantidad = int(input("Ingrese la cantidad: "))
                            if cantidad <= 0:
                                print("La cantidad debe ser mayor a 0")
                                continue
                            if cantidad > BaseDatos.productos[id_producto]["Stock"]:
                                print("No hay suficiente stock disponible")
                                continue

                            carrito[id_producto] = carrito.get(id_producto, 0) + cantidad
                            print(f"{BaseDatos.productos[id_producto]['Nombre']} x{cantidad} agregado al carrito")

                        if not carrito:
                            print("No se compró ningún producto.")
                            break

                        total = sum(BaseDatos.productos[i]["Precio"] * c for i, c in carrito.items())
                        print(f"\nTOTAL A PAGAR: Q{total}")

                        nit = input("Ingrese su NIT: ")
                        if nit in BaseDatos.clientes:
                            cliente = BaseDatos.clientes[nit]
                            print("\nCliente encontrado:")
                            print(
                                f"Nombre: {cliente['Nombre']} | Dirección: {cliente['Direccion']} | Teléfono: {cliente['Telefono']} | Correo: {cliente['Correo']}")
                        else:
                            print("\nCliente no registrado. Ingrese sus datos:")
                            nombre = input("Nombre: ")
                            direccion = input("Dirección: ")
                            telefono = input("Teléfono: ")
                            correo = input("Correo: ")
                            nuevo_cliente = AgregarCliente(nit, nombre, direccion, telefono, correo)

                        fecha = input("Ingrese la fecha de la venta (DD/MM/AAAA): ")
                        id_empleado = input("Ingrese el ID del empleado que atiende: ")
                        if id_empleado not in BaseDatos.empleados:
                            print("Empleado no registrado, no se puede registrar la venta.")
                        else:
                            id_venta = len(BaseDatos.ventas) + 1
                            nueva_venta = Venta(id_venta, fecha, nit, id_empleado)

                            for id_producto, cantidad in carrito.items():
                                id_detalle = len(BaseDatos.detalles_venta) + 1
                                precio = BaseDatos.productos[id_producto]["Precio"]
                                detalle = DetalleVenta(id_detalle, id_venta, id_producto, cantidad, precio)
                                nueva_venta.agregar_detalle(detalle)

                                BaseDatos.productos[id_producto]["Stock"] -= cantidad
                                BaseDatos.productos[id_producto]["total_ventas"] += cantidad

                            print("\nVenta registrada correctamente")
                            print("Detalle de compra:")
                            for id_producto, cantidad in carrito.items():
                                nombre = BaseDatos.productos[id_producto]["Nombre"]
                                precio = BaseDatos.productos[id_producto]["Precio"]
                                print(f"{nombre} x{cantidad} - Q{precio * cantidad}")
                            print(f"TOTAL PAGADO: Q{total}")

                case 5:
                    print("Saliendo del menú")
        else:
            print("Ingreso una opcion no valida o inexistente")
    except ValueError:
        print("Ingreso un dato incorrecto")
    if opcion!=5:
        print("Presione ENTER para continuar")
        input()