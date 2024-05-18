import random

def getBinomial(n, p):
    x = 0
    for i in range(n):
        if random.random() < p:
            x += 1
    return x

n_value = 10
p_value = 0.5
num_samples = 100

print(f"Generando y mostrando {num_samples} valores binomiales con n = {n_value} y p = {p_value}:")
for _ in range(num_samples):
    binomial_value = getBinomial(n_value, p_value)
    print("Valor binomial:", binomial_value)
