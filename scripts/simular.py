#!/usr/bin/env python3
"""Simulación en un proceso (NumPy, Numba secuencial o Numba paralelo).

Uso previsto:
    python scripts/simular.py --rows 50 --cols 50 --steps 60 --gif
    NUMBA_NUM_THREADS=4 python scripts/simular.py --backend numba-par --rows 400 --cols 400
"""

import argparse


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rows", type=int, default=50)
    ap.add_argument("--cols", type=int, default=50)
    ap.add_argument("--steps", type=int, default=30)
    ap.add_argument("--seed", type=int, default=12345)
    ap.add_argument("--backend", choices=["numpy", "numba", "numba-par"], default="numba-par")
    ap.add_argument("--inicial", default="centro", help="centro | aleatorio | uniforme | ruta.npy")
    ap.add_argument("--salida", default="resultados")
    ap.add_argument("--gif", action="store_true")
    args = ap.parse_args()

    # TODO: construir Params, condición inicial, llamar a calentar() y simular(),
    #       guardar final.npy, resumen.json (tiempos) y los gráficos.
    raise NotImplementedError


if __name__ == "__main__":
    main()
