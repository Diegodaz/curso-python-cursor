#Crea una calculadora y esta debe de botar el resultado y debe de antenerse abierta hasta poner salir

while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 5:
        break
    elif opcion == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        suma = num1 + num2
        print("La suma es: ", suma)