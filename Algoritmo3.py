def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
numero = int(input("Ingrese un número entero: "))
resultado = factorial(numero)
print(f"El factorial de ", numero, " es ", resultado)



