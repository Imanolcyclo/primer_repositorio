#progema para calcular el area de una triangulo con la base y la altura

import os  # para limpiar la pantalla

def limpiar_pantalla():
    
    os.system('cls' if os.name == 'nt' else 'clear')



while True:
    try:
        limpiar_pantalla()
        base = float(input("Ingrese La Base del Triangulo: "))
        break
    except ValueError:
        print(" Error: Debe ingresar La base correctamente).")
        input("Presione Enter para intentar de nuevo...")  
        
while True:
    try:
        limpiar_pantalla()
        altura = float(input("Ingrese La Altura del Triangulo: "))
        break
    except ValueError:
        print(" Error: Debe ingresar La Altura correctamente).")
        input("Presione Enter para intentar de nuevo...")  

area = base * altura /2

print(f"La base del Triangulo es {base}")
print(f"La Altura del Triangulo es {altura}")
print(f"La Area del Triangulo es {area}, que tenga un buen dia")

