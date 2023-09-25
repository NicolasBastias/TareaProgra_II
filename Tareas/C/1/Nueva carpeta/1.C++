#include <iostream>
#include <string>

// Clase base Producto
class Producto {
public:
    Producto(std::string nombre, double precio, std::string categoria)
        : nombre(nombre), precio(precio), categoria(categoria) {}

    void mostrar_detalle() {
        std::cout << "Nombre: " << nombre << std::endl;
        std::cout << "Precio: $" << precio << std::endl;
        std::cout << "Categoría: " << categoria << std::endl;
    }

private:
    std::string nombre;
    double precio;
    std::string categoria;
};

// Clase derivada Electrónico
class Electronico : public Producto {
public:
    Electronico(std::string nombre, double precio, std::string categoria, std::string marca)
        : Producto(nombre, precio, categoria), marca(marca) {}

    void mostrar_detalle() {
        Producto::mostrar_detalle();
        std::cout << "Marca: " << marca << std::endl;
    }

private:
    std::string marca;
};

// Clase derivada Alimenticio
class Alimenticio : public Producto {
public:
    Alimenticio(std::string nombre, double precio, std::string categoria, std::string fecha_vencimiento)
        : Producto(nombre, precio, categoria), fecha_vencimiento(fecha_vencimiento) {}

    void mostrar_detalle() {
        Producto::mostrar_detalle();
        std::cout << "Fecha de Vencimiento: " << fecha_vencimiento << std::endl;
    }

private:
    std::string fecha_vencimiento;
};

// Clase derivada Vestimenta
class Vestimenta : public Producto {
public:
    Vestimenta(std::string nombre, double precio, std::string categoria, std::string talla)
        : Producto(nombre, precio, categoria), talla(talla) {}

    void mostrar_detalle() {
        Producto::mostrar_detalle();
        std::cout << "Talla: " << talla << std::endl;
    }

private:
    std::string talla;
};

int main() {
    Electronico electronico("Laptop", 999.99, "Electrónica", "HP");
    Alimenticio alimenticio("Leche", 2.99, "Alimentos", "2023-12-31");
    Vestimenta vestimenta("Camiseta", 19.99, "Ropa", "M");

    std::cout << "Detalles del producto electrónico:" << std::endl;
    electronico.mostrar_detalle();

    std::cout << "\nDetalles del producto alimenticio:" << std::endl;
    alimenticio.mostrar_detalle();

    std::cout << "\nDetalles del producto de vestimenta:" << std::endl;
    vestimenta.mostrar_detalle();

    return 0;
}
