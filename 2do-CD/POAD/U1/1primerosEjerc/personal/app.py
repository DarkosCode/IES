from persona import Persona as P

def main():
    P("juan", 32, 1.78, True).presentarse()
    P("PABLO", 80, 1.85).presentarse()
    elvi: P = P("Elvira", 50, 1.65, False)
    elvi.presentarse()
    print(elvi.edad)

if __name__ == "__main__":
    main()