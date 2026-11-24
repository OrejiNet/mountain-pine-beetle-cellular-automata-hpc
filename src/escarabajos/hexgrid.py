"""Grilla hexagonal en coordenadas offset por columnas.

Cada celda tiene 6 vecinos y cuáles son depende de la paridad de la columna
(ver la Figura 2 del paper). La "vecindad de Moore" hexagonal son 7 celdas:
la celda más sus 6 vecinos.

Decisión pendiente: ¿columnas impares desplazadas hacia abajo o hacia arriba?
Lo que se elija tiene que ser consistente con viz.py.
"""


def vecinos(i, j, rows, cols):
    """Lista de (fila, columna) de los vecinos de (i, j) que están dentro del mapa.

    TODO: definir los 6 desplazamientos para columnas pares e impares.
    """
    raise NotImplementedError


def centros(rows, cols):
    """Coordenadas (x, y) del centro de cada hexágono, para graficar.

    TODO
    """
    raise NotImplementedError
