"""Autómata celular estocástico multiescala para el escarabajo del pino.

Basado en Liu & Estep (2025), "A multiscale stochastic cellular automata model
for dispersion of mountain pine beetles", R. Soc. Open Sci. 12: 241934.

Módulos:
    params      parámetros del modelo
    hexgrid     vecindad en grilla hexagonal
    rng         números aleatorios reproducibles en paralelo
    reglas      reglas de transición (microescala, emisión, actualización)
    simulacion  bucle en un proceso (secuencial y Numba paralelo)
    mpi_sim     bucle distribuido con MPI y halos
    inicial     condiciones iniciales
    viz         gráficos y animaciones
"""
