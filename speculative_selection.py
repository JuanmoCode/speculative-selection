import concurrent.futures
import requests
import time


def consultar_servidor(nombre, url):
    inicio = time.time()

    try:
        respuesta = requests.get(url, timeout=10)

        if respuesta.status_code == 200:
            tiempo = time.time() - inicio
            return nombre, respuesta.status_code, tiempo

    except requests.RequestException:
        pass

    return nombre, None, None


def seleccion_especulativa():

    servidores = [
        ("Servidor A", "https://httpbin.org/delay/9"),
        ("Servidor B", "https://httpbin.org/delay/2"),
        ("Servidor C", "https://httpbin.org/delay/7")
    ]

    inicio = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:

        tareas = [
            executor.submit(consultar_servidor, nombre, url)
            for nombre, url in servidores
        ]

        print("Consultando los 3 servidores en paralelo...\n")

        for tarea in concurrent.futures.as_completed(tareas):

            nombre, estado, tiempo = tarea.result()

            if estado == 200:
                print(f"{nombre} respondió primero.")
                print(f"Tiempo de respuesta: {tiempo:.2f} segundos")

                print("\nSe selecciona este servidor.")
                break

    total = time.time() - inicio

    print(f"\nTiempo total: {total:.2f} segundos")


seleccion_especulativa()