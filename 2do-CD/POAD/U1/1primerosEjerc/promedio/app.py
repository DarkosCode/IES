def main():
    ENTEROS: list[int] = [8, 20, 3, 5, 7, 9, -11]
    acumulador: int = 0
    promedio: float
    for entero in ENTEROS:
        acumulador += entero
        #acumulador = acumulador + entero
    promedio = acumulador / len(ENTEROS)
    print(promedio)

if __name__ == "__main__":
    main()