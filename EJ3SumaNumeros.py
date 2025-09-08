# Programa para sumar 2 numeros

import os  # para limpiar la pantalla

def limpiar_pantalla():
    # Windows usa 'cls', Linux/Mac usa 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

# suma de dos números
while True:
    try:
        limpiar_pantalla()
        numero1 = float(input("Ingrese el primer número a sumar: "))
        break
    except ValueError:
        print(" Error: Debe ingresar un número (entero o decimal).")
        input("Presione Enter para intentar de nuevo...")  # pausa antes de limpiar

while True:
    try:
        limpiar_pantalla()
        numero2 = float(input("Ingrese el segundo número a sumar: "))
        break
    except ValueError:
        print(" Error: Debe ingresar un número (entero o decimal).")
        input("Presione Enter para intentar de nuevo...")

limpiar_pantalla()
numero3 = numero1 + numero2
print(f" Su número es {numero3}. ¡Que tenga un buen día!")
