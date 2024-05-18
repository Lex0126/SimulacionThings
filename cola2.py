import simpy
import numpy as np

# Parámetros de la simulación
arrival_mean = 50  # Promedio de llegadas por hora
service_rate = 4  # tasa de servicio por hora (1/4 de hora)
simulation_hours = 100  # horas de simulación


# Función que representa el comportamiento del cliente en el sistema de cola
def customer(env, name, server):
    service_time = np.random.exponential(1 / service_rate)
    arrival_time = env.now
    print(f"Cliente {name} llega a la hora {arrival_time}")

    with server.request() as req:
        yield req

        service_start_time = env.now
        print(f"Cliente {name} comienza a ser atendido a la hora {service_start_time}")

        yield env.timeout(service_time)

        departure_time = env.now
        print(f"Cliente {name} termina de ser atendido a la hora {departure_time}")


# Función de simulación
def simulation(env, num_servers, results):
    server = simpy.Resource(env, capacity=num_servers)
    total_servers_opened = 0

    for _ in range(simulation_hours):
        num_arrivals = np.random.poisson(arrival_mean)  # Número de llegadas en esta hora
        for _ in range(num_arrivals):
            env.process(customer(env, env.now, server))
            total_servers_opened += 1

        yield env.timeout(1)  # Esperar una hora de simulación

    results.append(total_servers_opened)  # Almacenamos el total de cajas abiertas en la lista results


# Simulamos con diferentes cantidades de cajas
for num_servers in range(1, 11):
    print(f"Simulación con {num_servers} cajas:")
    env = simpy.Environment()
    results = []  # Lista para almacenar los resultados de la simulación

    env.process(simulation(env, num_servers, results))
    env.run()

    if results:  # Verificamos si la lista de resultados no está vacía antes de acceder a los resultados
        total_opened = results[0]  # Obtenemos el total de cajas abiertas de la lista de resultados
        print(f"Total de cajas abiertas: {total_opened}\n")
    else:
        print("La lista de resultados está vacía. La simulación no se ejecutó correctamente.\n")






