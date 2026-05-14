import math

#! Ejercicio de crear un for dentro de un while
contador = 1
while(contador <= 5):
    # print("Ciclo While N°", contador)
    print(f"Ciclo While N° {contador}")
    for i in range(1,6):
        print(f"For N° {i}")
    contador += 1

print("\n")

#! Ejercicio de crear un while dentro de un for
for i in range(1,6):
    print(f"\nDentro del For N° {i}")
    j = 1
    while j <= 5:
        print(f"While N° {j}")
        j +=1
        
print("\n")

#! imprimir numeros primos entre 0 y 30
for num in range(1, 31):
    primo = True
    for j in range(2, int(num ** 0.5) + 1):
        # si un número tiene un divisor, ese divisor siempre va a ser menor o igual 
        # a su raíz cuadrada. Entonces no hace falta revisar todos los números hasta
        # num, sino solo hasta √num (**0.5)
        if num % j == 0:
            primo = False
            break
    if primo:
        print("PRIMO!: ", num)