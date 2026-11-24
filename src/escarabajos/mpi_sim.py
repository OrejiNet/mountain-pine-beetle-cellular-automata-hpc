"""Versión distribuida con MPI (mpi4py).

Diseño propuesto:
    - Descomposición por franjas de filas: cada proceso tiene un bloque contiguo.
    - Una fila de halo arriba y otra abajo con la copia de la fila borde del vecino.
    - En los extremos del mapa, el vecino es MPI.PROC_NULL (halo = 0, frontera absorbente).

Un año = un superpaso BSP:
    microescala (local)
    -> intercambio de halos de P
    -> emisión (local)
    -> intercambio de halos de E
    -> actualización (local)
    -> allreduce de estadísticas

Medir por separado el tiempo de cálculo y el de comunicación de cada proceso,
para poder analizar el desbalance de carga.
"""


def reparto_filas(rows, nprocs, rank):
    """Filas [inicio, fin) que le tocan a `rank`, lo más parejo posible.

    TODO
    """
    raise NotImplementedError


def intercambiar_halos(A, comm, arriba, abajo):
    """Enviar la primera y la última fila propias a los vecinos y recibir sus halos.

    TODO: usar comm.Sendrecv (dos llamadas: hacia arriba y hacia abajo).
    """
    raise NotImplementedError


def simular_mpi(params, P0_global, backend="numba", comm=None):
    """Simulación distribuida. Devuelve el resultado completo sólo en rank 0.

    TODO
    """
    raise NotImplementedError
