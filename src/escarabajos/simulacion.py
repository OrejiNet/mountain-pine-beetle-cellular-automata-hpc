"""Bucle de simulación en un solo proceso.

Backends previstos:
    "numpy"     : referencia en NumPy puro (para verificar)
    "numba"     : reglas compiladas con njit, secuencial
    "numba-par" : njit(parallel=True) + prange (equivalente a OpenMP).
                  Hilos con NUMBA_NUM_THREADS.

Ojo: si se compilan las variantes secuencial y paralela desde la misma función
con cache=True, la caché de Numba puede mezclarlas. Verificar el speedup.
"""

from dataclasses import dataclass, field


@dataclass
class Resultado:
    P: object = None                               # estado final (rows, cols)
    poblacion: list = field(default_factory=list)  # suma de densidades por paso
    infestadas: list = field(default_factory=list) # n° de celdas con densidad > 0
    historia: list = field(default_factory=list)   # grillas guardadas (para el GIF)
    tiempos: dict = field(default_factory=dict)    # segundos por etapa


def simular(params, P0, backend="numba-par", guardar_cada=0):
    """Corre params.steps pasos desde la grilla inicial P0 (rows, cols).

    TODO:
      1. Crear P, E y P_nuevo con relleno de 1 celda.
      2. Por cada paso: microescala -> emision -> actualizacion -> intercambiar buffers.
      3. Registrar población, celdas infestadas y tiempos por etapa.
    """
    raise NotImplementedError


def calentar(backend="numba-par"):
    """Compilar los kernels con una grilla mínima antes de medir tiempos.

    TODO
    """
    raise NotImplementedError
