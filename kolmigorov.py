import numpy as np
from scipy.stats import kstest

#primero generamos una muestra de 100 numeros aleatorios con una libreria de python
np.random.seed(0)
sample_size = 100
random_numbers = np.random.rand(sample_size)

# ordenamos los numeros de menor a mayor
sorted_numbers = np.sort(random_numbers)

# imprimimos esos numeros generados para la verficacion
print("Números generados aleatoriamente:")
print(random_numbers)
print("\nNúmeros ordenados:")
print(sorted_numbers)

# Realizar la prueba de Kolmogorov-Smirnov
# La distribución es entre 0 y 1
D, _ = kstest(sorted_numbers, 'uniform')

print("\nEstadístico D de Kolmogorov-Smirnov:", D)
d = 0.134  # nivel a 100 numeros con una significancia de 0.5
if D < d:
    print("Los números parecen ser uniformemente distribuidos.")
else:
    print("Los números no parecen ser uniformemente distribuidos.")
