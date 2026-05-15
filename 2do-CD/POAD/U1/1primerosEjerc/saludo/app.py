def main():
    nombre: str = input("Hola, ingrese su nombre: ")
    print(f"Hola, {nombre.title()}.") #f-string
    # print("Hola, " + nombre.capitalize() + ".")
    # print("Hola, {}.".format(nombre))

if __name__ == "__main__":
    main()