import random

def simular_corridas(corridas):
    cantidad_inicial = 30
    apuesta_inicial = 10
    victorias = 0

    for _ in range(corridas):
        cantidad_actual = cantidad_inicial
        apuesta_actual = apuesta_inicial
        print("Corrida ", _ + 1)

        while 0 < cantidad_actual < 50:
            numero_aleatorio = random.random() > 0.5
            print("Numero Uniforme", numero_aleatorio)
            print("Apuesta Actual: ", apuesta_actual)

            if numero_aleatorio < 0.5:
                cantidad_actual += apuesta_actual
                print("Ganador, cantidad actual: ", cantidad_actual)
                apuesta_actual = apuesta_inicial
            else:
                cantidad_actual -= apuesta_actual
                print("Perdedor, cantidad actual: ", cantidad_actual)
                apuesta_actual *= 2

            print("-------")

        if cantidad_actual >= 50:
            print("Has alcanzado la meta de 50")
            victorias += 1
        else:
            print("Quebrado")

    probabilidad = victorias / corridas
    print("Probabilidad de llegar a la meta: ", probabilidad)

if __name__ == "__main__":
    corridas = int(input("Digite el numero de corridas: "))
    simular_corridas(corridas)
