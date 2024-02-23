def par(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
n = int(input("Escriba un numero: "))
resultado = par(n)
print("El numero es: ",par(n))
