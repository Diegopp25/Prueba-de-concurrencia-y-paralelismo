from secuencial import ejecutar_secuencial
from concurrencia import ejecutar_concurrencia
from paralelismo import ejecutar_paralelismo


def main():

    RANGO_INICIAL = 1
    RANGO_FINAL = 2_000_000

    valores = [2, 3, 4, 5, 6, 7, 8]

    print("=" * 60)
    print("PRUEBA SECUENCIAL")
    print("=" * 60)

    resultado = ejecutar_secuencial(
        RANGO_INICIAL,
        RANGO_FINAL
    )

    print(
        f"Primos: {resultado['primos']} | "
        f"Tiempo: {resultado['tiempo']:.4f}s"
    )

    print()

    print("=" * 60)
    print("PRUEBAS DE CONCURRENCIA")
    print("=" * 60)

    for num_threads in valores:

        resultado = ejecutar_concurrencia(
            num_threads,
            RANGO_INICIAL,
            RANGO_FINAL
        )

        print(
            f"Threads={num_threads} | "
            f"Primos={resultado['primos']} | "
            f"Tiempo={resultado['tiempo']:.4f}s"
        )

    print()

    print("=" * 60)
    print("PRUEBAS DE PARALELISMO")
    print("=" * 60)

    for num_procesos in valores:

        resultado = ejecutar_paralelismo(
            num_procesos,
            RANGO_INICIAL,
            RANGO_FINAL
        )

        print(
            f"Procesos={num_procesos} | "
            f"Primos={resultado['primos']} | "
            f"Tiempo={resultado['tiempo']:.4f}s"
        )


if __name__ == "__main__":
    main()