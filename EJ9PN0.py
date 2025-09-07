import os

#programa para verificar si un numero es positivo, negativo o 0

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
        
        

if numero == 0:
    
    print("su numero es 0 ")
elif numero <0:
    print("Su numero es negativo")
else:
    print("su numero es positivo")






