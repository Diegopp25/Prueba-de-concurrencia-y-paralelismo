from utils import es_primo
import threading
import time


def ejecutar_concurrencia(num_threads, inicio=1, fin=10_000_000):

    contador_global = 0
    lista_global = []

    lock = threading.Lock()

    def trabajador(inicio_rango, fin_rango):
        nonlocal contador_global
        nonlocal lista_global

        contador_local = 0
        lista_local = []

        for numero in range(inicio_rango, fin_rango):

            if es_primo(numero):
                contador_local += 1
                lista_local.append(numero)

        with lock:
            contador_global += contador_local
            lista_global.extend(lista_local)

    tamaño = (fin - inicio) // num_threads

    threads = []

    tiempo_inicio = time.perf_counter()

    for i in range(num_threads):

        inicio_rango = inicio + i * tamaño

        if i == num_threads - 1:
            fin_rango = fin + 1
        else:
            fin_rango = inicio_rango + tamaño

        t = threading.Thread(
            target=trabajador,
            args=(inicio_rango, fin_rango)
        )

        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    tiempo_fin = time.perf_counter()

    return {
        "primos": contador_global,
        "tiempo": tiempo_fin - tiempo_inicio
    }