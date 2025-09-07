import math
import os

#programa para calcular el Area de un circulo con el radio

def limpiar_pantalla():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    

while True:
    try:
        limpiar_pantalla()
        radio = float(input("Ingrese el radio del circulo: "))
        break
    except ValueError:
        print(" Error: Debe ingresar el Radio correctamente).")
        input("Presione Enter para seguir...")
        

radioalcuadrado = radio * radio
area = radioalcuadrado * math.pi

print(f"La area del circulo es {area:.2f}, que tenga un buen dia")