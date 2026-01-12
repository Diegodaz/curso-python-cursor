# Recorrer números del 1 al 50.
# Reglas:
# 1. Si el número es múltiplo de 3 y 5, imprimir "FizzBuzz"
# 2. Si solo es múltiplo de 3, imprimir "Fizz"
# 3. Si solo es múltiplo de 5, imprimir "Buzz"
# 4. En cualquier otro caso, imprimir el número.
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        