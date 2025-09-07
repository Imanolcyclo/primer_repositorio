import os

#programa para comvertir grados celsius a fahrenheit

def limpiar_pantalla():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    

while True:
    try:
        limpiar_pantalla()
        numero1 = float(input("Ingrese el numero: "))
        break
    except ValueError:
        print(" Error: Debe ingresar el dato correctamente).")
        input("Presione Enter para seguir...")
        
        

while True:
    try:
        limpiar_pantalla()
        numero2 = float(input("Ingrese el numero: "))
        break
    except ValueError:
        print(" Error: Debe ingresar el dato correctamente).")
        input("Presione Enter para seguir...")
        
        

while True:
    try:
        limpiar_pantalla()
        numero3 = float(input("Ingrese el numero: "))
        break
    except ValueError:
        print(" Error: Debe ingresar el dato correctamente).")
        input("Presione Enter para seguir...")
        
        

if numero1 >= numero2 and numero1 >= numero3:
    print(f"El numero {numero1} es mayor que {numero2} y {numero3}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"El numero {numero2} es mayor que {numero1} y {numero3}")
elif numero3 >= numero1 and numero3 >= numero2:
    print(f"El numero {numero3} es mayor que {numero1} y {numero2}")