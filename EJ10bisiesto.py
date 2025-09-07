import os

#programa para comvertir grados celsius a fahrenheit

def limpiar_pantalla():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    

while True:
    try:
        limpiar_pantalla()
        año = float(input("Ingrese el año: "))
        break
    except ValueError:
        print(" Error: Debe ingresar lo  correspondiente).")
        input("Presione Enter para seguir...")
        
        
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
else:
    print("El año no es bisiesto")
