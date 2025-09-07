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
        print(" Error: Debe ingresar el dato correctamente).")
        input("Presione Enter para seguir...")
        
        

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es bisiesto")
else:
    print(f"{año} no es bisiesto")