# Paralelización

El autómata es un **stencil**: el estado nuevo de cada celda depende sólo de ella y de sus vecinas en el paso anterior.

$$E^{(t+1)}[i,j] = f\big(E^{(t)}[i,j],\ V^{(t)}[i,j]\big)$$

## Reglas a respetar

1. **Doble buffer.** Leer de `P(t)` y escribir en `P(t+1)`; al final del paso se intercambian. Si no, una celda puede leer a una vecina ya actualizada (condición de carrera).
2. **Gather, no scatter.** Que cada celda sume lo que le llega de sus vecinas, en vez de "empujar" su emisión hacia ellas. Así cada hilo escribe sólo en sus propias celdas.
3. **Números aleatorios reproducibles.** Usar un RNG por contador (hash de semilla, t, celda y flujo) para que el resultado no dependa del número de hilos o procesos, y poder comparar contra la versión secuencial.

## Memoria compartida: Numba (equivalente a OpenMP)

`njit(parallel=True)` con `prange` en el bucle de filas, como `#pragma omp parallel for`. Los hilos se fijan con `NUMBA_NUM_THREADS`. Medir excluyendo la primera llamada, que es la compilación.

## Memoria distribuida: MPI con halos (BSP)

Reparto por franjas de filas; cada proceso guarda una fila de halo arriba y otra abajo.

```
         P0                  P1                  P2
   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
   │ halo (ceros) │    │ halo ← P0    │    │ halo ← P1    │
   │ filas 0..k   │    │ filas k..m   │    │ filas m..R   │
   │ halo ← P1    │    │ halo ← P2    │    │ halo (ceros) │
   └──────────────┘    └──────────────┘    └──────────────┘
```

Cada año es un superpaso BSP:

```
microescala (local)
   ├── Sendrecv halos de P
emisión (local)
   ├── Sendrecv halos de E
actualización (local) → allreduce de estadísticas
```

## Desbalance de carga (hipótesis a medir)

Si las celdas vacías se saltan para ahorrar cálculo, un foco concentrado hace que el proceso que lo tiene trabaje mucho más y los demás esperen en el intercambio de halos. Experimentos propuestos:

- Comparar `--inicial uniforme` (carga pareja) contra `--inicial centro` (carga concentrada).
- Medir tiempo de cálculo y de comunicación por proceso.
- Probar reparto cíclico de filas o reparto dinámico.
- En Numba, comparar el reparto estático de `prange` con lo observado en MPI.

## Experimentos de rendimiento

- Escalamiento fuerte con hilos y con procesos MPI (1, 2, 4, 8, 16): speedup y eficiencia.
- Híbrido: MPI × hilos con el mismo total de núcleos.
- En el clúster Xi: `slurm/escalamiento.slurm`.
