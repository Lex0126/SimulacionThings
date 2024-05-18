import random


def aproximar_pi(n):
    dentro_circulo = 0
    total_puntos = n

    for _ in range(total_puntos):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distancia = x ** 2 + y ** 2
        if distancia <= 1:
            dentro_circulo +=1

    pi_aproximado = 4 * dentro_circulo / total_puntos
    return pi_aproximado


if __name__ == '__main__':
    n = 10000
    pi_aproximado = aproximar_pi(n)
    print('Pi Calculado (usando método de Monte Carlo):', pi_aproximado)
