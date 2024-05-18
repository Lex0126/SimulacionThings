import math
import random

def getPoisson(lambda_):
    L = math.exp(-lambda_)
    p = 1.0
    k = 0

    while p > L:
        k += 1
        p *= random.random()

    return k - 1

# Ejemplo de uso e impresión de 100 valores de la distribución de Poisson
lambda_value = 2.5
num_samples = 100  # Número de muestras a generar e imprimir

print(f"Generando y mostrando {num_samples} valores de la distribución de Poisson con lambda = {lambda_value}:")
for _ in range(num_samples):
    poisson_value = getPoisson(lambda_value)
    print("Valor Poisson:", poisson_value)

