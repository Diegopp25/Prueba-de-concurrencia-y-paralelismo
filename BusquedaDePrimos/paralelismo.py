from multiprocessing import Pool
from utils import es_primo
import time


def contar_primos(rango):

    inicio, fin = rango

    contador = 0

    for numero in range(inicio, fin):

        if es_primo(numero):
            contador += 1

    return contador


def ejecutar_paralelismo(num_procesos, inicio=1, fin=10_000_000):

    tamaño = (fin - inicio) // num_procesos

    rangos = []

    for i in range(num_procesos):

        inicio_rango = inicio + i * tamaño

        if i == num_procesos - 1:
            fin_rango = fin + 1
        else:
            fin_rango = inicio_rango + tamaño

        rangos.append((inicio_rango, fin_rango))

    tiempo_inicio = time.perf_counter()

    with Pool(processes=num_procesos) as pool:
        resultados = pool.map(contar_primos, rangos)

    tiempo_fin = time.perf_counter()

    return {
        "primos": sum(resultados),
        "tiempo": tiempo_fin - tiempo_inicio
    }