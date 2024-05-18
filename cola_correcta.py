import random
import numpy as np

if __name__ == '__main__':
    for j in range(1, 13):
        promedio_clientes = 50
        clienxhora = np.random.poisson(promedio_clientes)
        clientes = list(range(1, clienxhora + 1))

        num_cajas = j
        cajas = [0] * num_cajas
        contador = [0] * num_cajas

        for i in range(1, 60 + 1):
            print("Hora", j, "- Minuto", i)

            for c in range(num_cajas):
                if cajas[c] == 0:
                    print("La caja", c+1, "se abre")

                    tiempo_aleatorio = random.randint(15,30)
                    print("Tiempo aleatorio para la caja", c+1, ":", tiempo_aleatorio)
                    cajas[c] = 1
                    contador[c] = tiempo_aleatorio
                    print("Contador para la caja", c+1, ":", contador[c])
                else:
                    contador[c] -= 1
                    print("Contador para la caja", c+1, ":", contador[c])
                    if contador[c] == 0 and clientes:
                        cajas[c] = 0
                        cliente_atendido = clientes.pop(0)
                        print("Caja", c+1, "cerrada. Cliente", cliente_atendido, "atendido.")

            print("Estado de las cajas:", cajas)


        personas_en_cajas = sum(cajas)
        personas_pendientes = len(clientes)
        promedio_personas = (personas_en_cajas + personas_pendientes) / num_cajas
        print("Promedio de personas al final de la hora", j, ": ", promedio_personas)