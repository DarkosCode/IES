from automovil import Automovil
from bicicleta import Bicicleta
from vehiculo import Vehiculo

def main():
    VEHICULOS: list[Vehiculo] = [
        Automovil("Ford", 2718281.828, 50),
        Bicicleta("Clides", 314159.265), # en Python no da error coma y cierre
        ]
    for n, vehiculo in enumerate(VEHICULOS, 1):
        print("El vehiculo #{} tiene la marca {} y {} ruedas.".format(
            n, vehiculo.marca, vehiculo.ruedas
        ))
        print(f"Fue trasladado a {vehiculo.trasladarse(34, 56)}.")

if __name__ == "__main__":
    main()