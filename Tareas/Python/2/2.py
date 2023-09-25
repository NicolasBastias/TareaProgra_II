// Clase base Empleado
class Empleado {
    private String nombre;
    private int edad;
    private double salario;

    public Empleado(String nombre, int edad, double salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    public void describirRol() {
        System.out.println("Soy un empleado de la empresa.");
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public double getSalario() {
        return salario;
    }
}

// Clase derivada Gerente
class Gerente extends Empleado {
    private String departamento;

    public Gerente(String nombre, int edad, double salario, String departamento) {
        super(nombre, edad, salario);
        this.departamento = departamento;
    }

    @Override
    public void describirRol() {
        System.out.println("Soy un gerente del departamento " + departamento);
    }

    public String getDepartamento() {
        return departamento;
    }
}

// Clase derivada Ingeniero
class Ingeniero extends Empleado {
    private String especialidad;

    public Ingeniero(String nombre, int edad, double salario, String especialidad) {
        super(nombre, edad, salario);
        this.especialidad = especialidad;
    }

    @Override
    public void describirRol() {
        System.out.println("Soy un ingeniero especializado en " + especialidad);
    }

    public String getEspecialidad() {
        return especialidad;
    }
}

// Clase derivada Asistente
class Asistente extends Empleado {
    public Asistente(String nombre, int edad, double salario) {
        super(nombre, edad, salario);
    }

    @Override
    public void describirRol() {
        System.out.println("Soy un asistente en la empresa.");
    }
}

public class Main {
    public static void main(String[] args) {
        Empleado empleado1 = new Gerente("Juan", 35, 60000.0, "Ventas");
        Empleado empleado2 = new Ingeniero("María", 28, 55000.0, "Software");
        Empleado empleado3 = new Asistente("Pedro", 22, 30000.0);

        empleado1.describirRol();
        empleado2.describirRol();
        empleado3.describirRol();
    }
}
