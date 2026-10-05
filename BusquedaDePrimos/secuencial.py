from utils import es_primo
import time


def ejecutar_secuencial(inicio=1, fin=10_000_000):

    contador = 0
    lista_primos = []

    tiempo_inicio = time.perf_counter()

    for numero in range(inicio, fin + 1):

        if es_primo(numero):
            contador += 1
            lista_primos.append(numero)

    tiempo_fin = time.perf_counter()

    return {
        "primos": contador,
        "tiempo": tiempo_fin - tiempo_inicio
    }