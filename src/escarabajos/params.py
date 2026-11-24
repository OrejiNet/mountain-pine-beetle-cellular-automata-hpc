"""Parámetros del modelo.

Valores por defecto: Tabla 2 de Liu & Estep (2025).
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Params:
    # --- Grilla y tiempo ---
    rows: int = 50          # filas de la grilla hexagonal
    cols: int = 50          # columnas
    steps: int = 30         # pasos macroscópicos (1 paso = 1 año)

    # --- Microescala: nacimiento y muerte ---
    b: float = 1.0          # natalidad (logística)
    d: float = 0.2          # mortalidad (lineal)
    C: int = 100            # capacidad de carga por celda
    N: int = 100            # pasos microscópicos por paso macroscópico
    M: int = 20             # réplicas microscópicas por celda

    # --- Macroescala: dispersión ---
    gamma1: float = 0.8     # fracción del exceso sobre la media que se dispersa
    gamma2: float = 0.8     # fracción de dispersores que sobrevive al viaje
    phi: float = 1 / 3      # supervivencia base
    rho: float = 1 / 3      # supervivencia dependiente de la densidad

    seed: int = 12345

    def __post_init__(self):
        # TODO: validar los parámetros. Por ejemplo:
        #   - gamma1 y gamma2 en [0, 1]
        #   - phi + (pi/4) * rho <= 1   (restricción del paper para que p_S <= 1)
        #   - b*C/(4N) + d*C/N <= 1     (probabilidades de un paso microscópico)
        pass
