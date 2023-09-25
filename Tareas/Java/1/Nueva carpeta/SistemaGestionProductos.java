// Clase base Producto
class Producto {
    private String nombre;
    private double precio;
    private String categoria;

    public Producto(String nombre, double precio, String categoria) {
        this.nombre = nombre;
        this.precio = precio;
        this.categoria = categoria;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public String getCategoria() {
        return categoria;
    }

    public void mostrarDetalle() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Precio: $" + precio);
        System.out.println("Categoría: " + categoria);
    }
}

// Clase derivada Electrónico
class Electronico extends Producto {
    private String marca;

    public Electronico(String nombre, double precio, String categoria, String marca) {
        super(nombre, precio, categoria);
        this.marca = marca;
    }

    public String getMarca() {
        return marca;
    }

    @Override
    public void mostrarDetalle() {
        super.mostrarDetalle();
        System.out.println("Marca: " + marca);
    }
}

// Clase derivada Alimenticio
class Alimenticio extends Producto {
    private String fechaCaducidad;

    public Alimenticio(String nombre, double precio, String categoria, String fechaCaducidad) {
        super(nombre, precio, categoria);
        this.fechaCaducidad = fechaCaducidad;
    }

    public String getFechaCaducidad() {
        return fechaCaducidad;
    }

    @Override
    public void mostrarDetalle() {
        super.mostrarDetalle();
        System.out.println("Fecha de Caducidad: " + fechaCaducidad);
    }
}

// Clase derivada Vestimenta
class Vestimenta extends Producto {
    private String talla;

    public Vestimenta(String nombre, double precio, String categoria, String talla) {
        super(nombre, precio, categoria);
        this.talla = talla;
    }

    public String getTalla() {
        return talla;
    }

    @Override
    public void mostrarDetalle() {
        super.mostrarDetalle();
        System.out.println("Talla: " + talla);
    }
}

public class SistemaGestionProductos {
    public static void main(String[] args) {
        Electronico celular = new Electronico("Smartphone", 699.99, "Electrónico", "Samsung");
        Alimenticio leche = new Alimenticio("Leche", 2.99, "Alimenticio", "2023-10-15");
        Vestimenta camiseta = new Vestimenta("Camiseta", 19.99, "Vestimenta", "M");

        System.out.println("Detalles del Celular:");
        celular.mostrarDetalle();

        System.out.println("\nDetalles de la Leche:");
        leche.mostrarDetalle();

        System.out.println("\nDetalles de la Camiseta:");
        camiseta.mostrarDetalle();
    }
}
