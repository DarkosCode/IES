from bicicleta import Bicicleta

def main():
    bici: Bicicleta = Bicicleta("Clides", 314159.265)
    print(bici.precio)
    bici.precio = -42
    print(bici.precio)
    print(bici.ubicacion)
    bici.trasladarse(34,46)
    print(bici.ubicacion)

if __name__ == "__main__":
    main()