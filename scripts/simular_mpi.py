#!/usr/bin/env python3
"""Simulación distribuida con MPI.

Uso previsto:
    mpiexec -n 4 python scripts/simular_mpi.py --rows 400 --cols 400 --steps 30
    NUMBA_NUM_THREADS=4 mpiexec -n 2 python scripts/simular_mpi.py --backend numba-par   # híbrido
"""

import argparse


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rows", type=int, default=50)
    ap.add_argument("--cols", type=int, default=50)
    ap.add_argument("--steps", type=int, default=30)
    ap.add_argument("--seed", type=int, default=12345)
    ap.add_argument("--backend", choices=["numba", "numba-par"], default="numba")
    ap.add_argument("--inicial", default="centro")
    ap.add_argument("--salida", default="resultados")
    args = ap.parse_args()

    # TODO: llamar a simular_mpi(); en rank 0 guardar final_mpi{n}.npy e imprimir
    #       JSON con tiempo total y tiempos de cálculo/comunicación por proceso.
    raise NotImplementedError


if __name__ == "__main__":
    main()
