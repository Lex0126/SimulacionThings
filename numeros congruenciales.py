def congruencia_lineal(semilla, a, m, n):

  x = semilla
  lista = []
  for i in range(n):
    x = (a * x + semilla) % m
    lista.append(x)
  return lista


if __name__ == "__main__":
  semilla = 1
  a = 2
  m = 1000
  n = 100
  lista = congruencia_lineal(semilla, a, m, n)
  print(lista, "\n")