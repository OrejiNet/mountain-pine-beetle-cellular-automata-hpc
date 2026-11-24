"""Reglas de transición: un paso macroscópico (un año).

Orden dentro de un paso (Liu & Estep 2025):
    1. microescala   : nacimiento y muerte dentro de cada celda
    2. emisión       : cuánto dispersa cada celda
    3. actualización : reparto de lo emitido + supervivencia

Recomendaciones para paralelizar (ver docs/paralelizacion.md):
    - Arreglos con 1 celda de relleno por borde: P.shape == (filas + 2, cols + 2).
      El relleno hace de frontera absorbente y, en MPI, de halo.
    - Doble buffer: leer de P(t), escribir en P(t+1).
    - Escribir la dispersión como "gather" (cada celda suma lo que le llega)
      para evitar condiciones de carrera.
    - Escribir cada función de modo que se pueda compilar con njit y con
      njit(parallel=True) usando prange en el bucle de filas.
"""


def microescala(P, params, t, fila_inicio):
    """Proceso de nacimiento y muerte en cada celda (en sitio).

    Para cada celda: M réplicas de N pasos, partiendo de X = round(P * C):
        P(n -> n+1) = b * n * (1 - n/C) / N
        P(n -> n-1) = d * n / N
    Nueva densidad = promedio de las réplicas / C.

    `fila_inicio` es la fila global de la primera fila local (para MPI y el RNG).

    TODO
    """
    raise NotImplementedError


def emision(P, E, params):
    """E = gamma1 * (P - media de la vecindad) si P está sobre la media; si no, 0.

    TODO
    """
    raise NotImplementedError


def actualizacion(P, E, P_nuevo, params, t, fila_inicio):
    """Reparte lo emitido entre las 7 celdas de cada vecindad (llega gamma2).

    - Celda infestada: P_nuevo = P - E + llegada
    - Celda vacía: se coloniza con probabilidad p_S = phi + rho * arctan(llegada)

    TODO
    """
    raise NotImplementedError
