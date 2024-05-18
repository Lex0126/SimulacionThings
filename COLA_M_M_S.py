import simpy
import numpy as np

# Parámetros de la simulación
arrivals_rate = 50  # tasa de llegadas por hora
service_rate = 4  # tasa de servicio por hora (1/4 de hora)
simulation_hours = 100  # horas de simulación


# Función para generar los tiempos de servicio (distribución exponencial)
def generate_service_time():
    return np.random.exponential(1 / service_rate)


# Función que representa el comportamiento del cliente en el sistema de cola
def customer(env, name, server):
    service_time = generate_service_time()
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
def simulation(env, num_servers):
    server = simpy.Resource(env, capacity=num_servers)

    while True:
        yield env.timeout(np.random.exponential(1 / arrivals_rate))
        env.process(customer(env, env.now, server))


# Simulamos con diferentes cantidades de cajas
for num_servers in range(1, 11):
    print(f"Simulación con {num_servers} cajas:")
    env = simpy.Environment()
    env.process(simulation(env, num_servers))
    env.run(until=simulation_hours)
    print()

