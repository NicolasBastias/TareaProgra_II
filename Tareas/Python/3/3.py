# Clase base Animal
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Función para hacer sonar al animal
def sonido(animal):
    if isinstance(animal, Perro):
        return f"{animal.nombre} dice: Woof Woof!"
    elif isinstance(animal, Gato):
        return f"{animal.nombre} dice: Miau Miau!"
    elif isinstance(animal, Pajaro):
        return f"{animal.nombre} canta: Pío Pío!"
    else:
        return "Animal desconocido"

# Clase derivada Perro
class Perro(Animal):
    pass

# Clase derivada Gato
class Gato(Animal):
    pass

# Clase derivada Pájaro
class Pajaro(Animal):
    pass

# Función principal
def main():
    perro = Perro("Fido", 3)
    gato = Gato("Garfield", 5)
    pajaro = Pajaro("Piolín", 2)

    print(sonido(perro))
    print(sonido(gato))
    print(sonido(pajaro))

if __name__ == "__main__":
    main()
