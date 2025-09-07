import os

#programa para verificar si un numero es par o impar

def limpiar_pantalla():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    

while True:
    try:
        limpiar_pantalla()
        numero = float(input("Ingrese el numero: "))
        break
    except ValueError:
        print(" Error: Debe ingresar lo  correspondiente).")
        input("Presione Enter para seguir...")
        
        

if numero % 2 == 0:
    
    print("su numero es par ")
else:
    print("su numero es impar")
