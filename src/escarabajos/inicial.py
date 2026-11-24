"""Condiciones iniciales (grilla global, sin relleno)."""


def foco_central(rows, cols):
    """Un solo foco en el centro. TODO"""
    raise NotImplementedError


def focos_aleatorios(rows, cols, k, seed):
    """k focos al azar, reproducible con `seed`. TODO"""
    raise NotImplementedError


def bosque_infestado(rows, cols, seed):
    """Todas las celdas ocupadas (carga pareja, para medir rendimiento). TODO"""
    raise NotImplementedError


def desde_archivo(ruta):
    """Cargar un mapa .npy, por ejemplo la imagen aérea ya procesada. TODO"""
    raise NotImplementedError
