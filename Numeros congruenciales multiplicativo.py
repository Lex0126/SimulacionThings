def mult(a, x0, m, n):

  numeros = []
  for i in range(n):
    x0 = (a * x0) % m
    numeros.append(x0)
  return numeros
a = 109
x0 = 5001
m = 5000
n = 100

numeros = mult(a, x0, m, n)
for numero in numeros:
  print(numero)