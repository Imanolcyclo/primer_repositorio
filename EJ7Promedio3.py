import os

#programa para calcular el promedio de 3 numeros

def limpiar_pantalla():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    

while True:
    try:
        limpiar_pantalla()
        numero1 = float(input("Ingrese el primer numero: "))
        break
    except ValueError:
        print(" Error: Debe ingresar lo  correspondiente).")
        input("Presione Enter para seguir...")
        

while True:
    try:
        limpiar_pantalla()
        numero2 = float(input("Ingrese el segundo numero: "))
        break
    except ValueError:
        print(" Error: Debe ingresar lo  correspondiente).")
        input("Presione Enter para seguir...")
        

while True:
    try:
        limpiar_pantalla()
        numero3 = float(input("Ingrese el tercer numero: "))
        break
    except ValueError:
        print(" Error: Debe ingresar lo  correspondiente).")
        input("Presione Enter para seguir...")


promedio = numero1 + numero2 + numero3 /3


print(F"El promedio de los numeros son {promedio} ")