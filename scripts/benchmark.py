#!/usr/bin/env python3
"""Escalamiento fuerte: mismo problema, más hilos o más procesos.

Uso previsto:
    python scripts/benchmark.py --modo hilos --max 8 --rows 800 --cols 800
    python scripts/benchmark.py --modo mpi   --max 8 --rows 800 --cols 800

Salida: CSV con columnas n, tiempo_s, speedup, eficiencia.
"""

import argparse


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--modo", choices=["hilos", "mpi"], default="hilos")
    ap.add_argument("--max", type=int, default=8)
    ap.add_argument("--rows", type=int, default=800)
    ap.add_argument("--cols", type=int, default=800)
    ap.add_argument("--steps", type=int, default=10)
    ap.add_argument("--inicial", default="uniforme")
    ap.add_argument("--salida", default="resultados/benchmark")
    args = ap.parse_args()

    # TODO: para n = 1, 2, 4, ..., max lanzar simular.py (con NUMBA_NUM_THREADS=n)
    #       o simular_mpi.py (mpiexec -n n) como subproceso, leer el tiempo y
    #       calcular speedup = T1/Tn y eficiencia = speedup/n.
    raise NotImplementedError


if __name__ == "__main__":
    main()
