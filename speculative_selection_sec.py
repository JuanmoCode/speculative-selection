import requests
import time


def consultar_servidor(nombre, url):
    inicio = time.time()

    try:
        respuesta = requests.get(url, timeout=10)

        if respuesta.status_code == 200:
            tiempo = time.time() - inicio
            return nombre, tiempo

    except requests.RequestException:
        pass

    return nombre, None


def seleccion_secuencial():

    servidores = [
        ("Servidor A", "https://httpbin.org/delay/9"),
        ("Servidor B", "https://httpbin.org/delay/2"),
        ("Servidor C", "https://httpbin.org/delay/7")
    ]

    inicio = time.time()

    print("Consultando los servidores secuencialmente...\n")

    for nombre, url in servidores:

        print(f"Consultando {nombre}...")

        servidor, tiempo = consultar_servidor(nombre, url)

        if tiempo is not None:
            print(f"{servidor} respondió correctamente.")
            print(f"Tiempo de respuesta: {tiempo:.2f} segundos")

            print("\nSe selecciona este servidor.")
            break

    total = time.time() - inicio

    print(f"\nTiempo total: {total:.2f} segundos")


seleccion_secuencial()