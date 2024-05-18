import math
def mult(a, x0, m, n):
    numeros = []
    suma_total = 0
    for i in range(n):
        x0 = (a * x0) % m
        numeros.append(x0 / 10000)
        suma_total += x0
    promedio = suma_total / (n * 10000)
    return numeros, promedio

def pruebaz(n, promedio):
    z = ((promedio - 0.5) * (math.sqrt(n))/math.sqrt(1/12))
    return z

a = 109
x0 = 5001
m = 5000
n = 100

numeros, promedio = mult(a, x0, m, n)
print("Números generados:")
for numero in numeros:
    print(numero)
print("Promedio:", promedio)
result=pruebaz(n,promedio)
if result < 1.96:
    print("Los números generados son aleatorios.")
else:
    print("Los números generados no son aleatorios.")

print("Resultado de la prueba Z", result)

