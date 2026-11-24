"""Números aleatorios reproducibles en paralelo.

Problema: si cada hilo o proceso usa su propio generador, el resultado cambia
según cuántos hilos o procesos se usen, y no se puede comparar la versión
paralela con la secuencial.

Idea propuesta: un generador "por contador". Cada número aleatorio se obtiene
aplicando un hash a (semilla, paso t, celda global, flujo), por ejemplo con
SplitMix64. Así la celda (i, j) en el paso t usa siempre el mismo número, sin
importar quién la calcule.
"""


def uniforme(seed, t, celda, flujo):
    """U(0, 1) determinista para (semilla, t, celda, flujo).

    TODO: implementar (debe poder compilarse con Numba).
    """
    raise NotImplementedError
