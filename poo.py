class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"


class Mascota(Animal):
    def __init__(self, nombre, edad, tipo_pelo):
        super().__init__(nombre, edad)
        self.tipo_pelo = tipo_pelo


class Perro(Mascota):
    def hacer_sonido(self):
        return "Guau"


class Gato(Mascota):
    def hacer_sonido(self):
        return "Miau"


class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu"


def main():
    perro = Perro("Firulais", 3, "Corto")
    gato = Gato("Bigotes", 2, "Largo")
    vaca = Vaca("Otis", 4)

    # Herencia
    print(f"{perro.nombre} tiene pelo {perro.tipo_pelo}.")
    print(f"{gato.nombre} tiene pelo {gato.tipo_pelo}.")

    # Polimorfismo
    animales = [perro, gato, vaca]
    for animal in animales:
        print(f"{animal} hace: {animal.hacer_sonido()}")

    # Sobrecarga de métodos
    def hacer_sonido_personalizado(animal):
        print(f"{animal} dice: {animal.hacer_sonido()}")

    hacer_sonido_personalizado(perro)
    hacer_sonido_personalizado(gato)
    hacer_sonido_personalizado(vaca)


if __name__ == "__main__":
    main()
