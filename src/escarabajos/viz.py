"""Visualización (matplotlib)."""


def guardar_png(P, ruta, titulo=None):
    """Dibujar la grilla con hexágonos coloreados por densidad.

    TODO: matplotlib.collections.PolyCollection con hexagonos en hexgrid.centros().
    """
    raise NotImplementedError


def guardar_series(poblacion, infestadas, ruta):
    """Población total y celdas infestadas en el tiempo. TODO"""
    raise NotImplementedError


def guardar_gif(historia, ruta, fps=4):
    """Animación de la expansión. TODO: FuncAnimation + PillowWriter."""
    raise NotImplementedError


def graficar_escalamiento(csv, ruta):
    """Speedup y eficiencia a partir del CSV del benchmark. TODO"""
    raise NotImplementedError
