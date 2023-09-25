# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_detalle(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Categoría: {self.categoria}")

# Clase derivada Electrónico
class Electronico(Producto):
    def __init__(self, nombre, precio, categoria, marca):
        super().__init__(nombre, precio, categoria)
        self.marca = marca

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Marca: {self.marca}")

# Clase derivada Alimenticio
class Alimenticio(Producto):
    def __init__(self, nombre, precio, categoria, fecha_vencimiento):
        super().__init__(nombre, precio, categoria)
        self.fecha_vencimiento = fecha_vencimiento

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Fecha de Vencimiento: {self.fecha_vencimiento}")

# Clase derivada Vestimenta
class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoria, talla):
        super().__init__(nombre, precio, categoria)
        self.talla = talla

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Talla: {self.talla}")

# Ejemplo de uso
electronico = Electronico("Laptop", 999.99, "Electrónica", "HP")
alimenticio = Alimenticio("Leche", 2.99, "Alimentos", "2023-12-31")
vestimenta = Vestimenta("Camiseta", 19.99, "Ropa", "M")

print("Detalles del producto electrónico:")
electronico.mostrar_detalle()

print("\nDetalles del producto alimenticio:")
alimenticio.mostrar_detalle()

print("\nDetalles del producto de vestimenta:")
vestimenta.mostrar_detalle()
