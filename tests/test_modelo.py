"""Tests planificados. Correr con:  pytest -q

Se marcan como `skip` hasta que exista la implementación; quitar el skip a
medida que se completen.
"""

import pytest

pendiente = pytest.mark.skip(reason="TODO: falta implementación")


@pendiente
def test_vecindad_simetrica():
    """Si A es vecino de B, B es vecino de A."""


@pendiente
def test_numba_igual_numpy():
    """Numba secuencial da el mismo resultado que la referencia NumPy."""


@pendiente
def test_paralelo_igual_secuencial():
    """numba-par da EXACTAMENTE lo mismo que numba (requiere RNG por contador)."""


@pendiente
def test_mpi_igual_secuencial():
    """mpiexec -n 2 y -n 3 dan lo mismo que la versión secuencial."""


@pendiente
def test_densidades_en_rango():
    """Todas las densidades quedan en [0, 1]."""


@pendiente
def test_grilla_vacia_sigue_vacia():
    """Sin escarabajos al inicio, no aparecen escarabajos."""


@pendiente
def test_equilibrio_logistico():
    """Sin dispersión (gamma1 = 0), una celda tiende a densidad 1 - d/b = 0.8."""


@pendiente
def test_reparto_filas_cubre_todo():
    """El reparto MPI cubre todas las filas sin huecos ni solapes."""
