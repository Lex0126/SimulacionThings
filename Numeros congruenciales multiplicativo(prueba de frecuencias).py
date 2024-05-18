
def mult(a, x0, m, n):
    numeros = []
    suma_total = 0
    for _ in range(n):
        x0 = (a * x0) % m
        numeros.append(x0 / 10000)
        suma_total += x0
    promedio = suma_total / (n * 10000)
    return numeros, promedio

' lo que hacemos en esta funcion es juntar en tuplas el valor de FO y FE para hacer la resta y hacerla a la potencia para poder divir entre la FE'
def chi_cuadrada(frec_observadas):
    n = 100
    frec_esperadas = [n / 10]
    chi_cuadrada = 0
    for obs, esp in zip(frec_observadas, frec_esperadas):
        chi_cuadrada += ((obs - esp) ** 2) / esp

    return chi_cuadrada


a = 109
x0 = 5001
m = 5000
n = 100

numeros, promedio = mult(a, x0, m, n)

print("Números generados:")
for numero in numeros:
    print(numero)

frecuencias_observadas = [0] * 10
for num in numeros:
    intervalo = int(num /0.1)
    frecuencias_observadas[intervalo] += 1

print("Frecuencias observadas en cada intervalo:")
for i, frecuencia in enumerate(frecuencias_observadas):
    print("Intervalo {}: {}".format(i, frecuencia))

result = chi_cuadrada(frecuencias_observadas)
print("Resultado:", result)


if result < 9.9:
    print('los numeros son aleatorios')
else:
    print('los numeros no son aleatorios')

