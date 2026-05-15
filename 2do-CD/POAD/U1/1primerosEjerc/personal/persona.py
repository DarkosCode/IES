class Persona:
    #edad, nombre, vivo, altura
    #constructor
    def __init__(self, nombre: str, edad: int, altura: float, vivo: bool = True):
        self.nombre: str = nombre
        self.edad: int = edad
        self.altura: float = altura
        self.vivo: bool = vivo

    def presentarse(self):
        if self.vivo:
            print(f"Hola, soy {self.nombre}.")
        else:
            print(f"QEPD {self.nombre}.")
