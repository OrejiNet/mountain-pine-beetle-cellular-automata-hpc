# Mountain Pine Beetle Cellular Automata HPC 🪲🌲

Proyecto del curso de Computación Paralela (USACH). Simulación de la expansión del **escarabajo del pino de montaña** (*Dendroctonus ponderosae*) con un autómata celular estocástico multiescala, paralelizado con **Numba** (memoria compartida, como OpenMP) y **MPI** (memoria distribuida, con halos y modelo BSP).

Modelo base: [Liu & Estep (2025), *Royal Society Open Science*](https://doi.org/10.1098/rsos.241934).

> **Estado:** esqueleto del proyecto. Las funciones tienen firma, documentación y `TODO`, pero aún no están implementadas.

## Idea

- Cada **celda** de una grilla hexagonal es un parche de bosque y guarda la **densidad de escarabajos** (entre 0 y 1).
- Cada **año**:
  1. **Microescala:** la población nace y muere dentro de cada celda (proceso estocástico).
  2. **Emisión:** las celdas con más escarabajos que su vecindad dispersan una parte.
  3. **Actualización:** lo dispersado llega a los vecinos; parte muere en el viaje y las celdas vacías se colonizan con cierta probabilidad.
- Cada celda sólo depende de sus vecinas, así que el problema es un *stencil* paralelizable.

Detalles: [`docs/modelo.md`](docs/modelo.md) y [`docs/paralelizacion.md`](docs/paralelizacion.md).

## Estructura

```
src/escarabajos/
  params.py       parámetros del modelo (Tabla 2 del paper)
  hexgrid.py      vecindad en grilla hexagonal
  rng.py          números aleatorios reproducibles en paralelo
  reglas.py       microescala, emisión y actualización
  simulacion.py   bucle en un proceso (NumPy, Numba, Numba paralelo)
  mpi_sim.py      bucle distribuido: reparto por filas + halos
  inicial.py      condiciones iniciales
  viz.py          gráficos, GIF y curvas de escalamiento
scripts/          simular.py, simular_mpi.py, benchmark.py
tests/            tests planificados (marcados como skip)
slurm/            script para el clúster Xi
datos/            mapas de entrada (.npy)
resultados/       salidas (no se versionan)
docs/             modelo, paralelización, referencias
```

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

MPI requiere OpenMPI o MPICH instalado. El clúster Xi trae OpenMPI 4.0.4.

## Uso previsto

```bash
python scripts/simular.py --rows 50 --cols 50 --steps 60 --gif
NUMBA_NUM_THREADS=4 python scripts/simular.py --backend numba-par --rows 400 --cols 400
mpiexec -n 4 python scripts/simular_mpi.py --rows 400 --cols 400
python scripts/benchmark.py --modo mpi --max 8
pytest -q
```

## Plan de trabajo

**Modelo**
- [ ] `hexgrid`: vecinos y coordenadas
- [ ] `rng`: RNG por contador
- [ ] `reglas`: microescala, emisión, actualización
- [ ] `simulacion`: versión NumPy de referencia
- [ ] Resolver las decisiones pendientes de `docs/modelo.md`

**Paralelización**
- [ ] Numba secuencial y paralelo (`prange`)
- [ ] MPI: reparto de filas, intercambio de halos, BSP
- [ ] Versión híbrida MPI + hilos
- [ ] (Opcional) Dask

**Experimentos**
- [ ] Tests de consistencia: paralelo y MPI iguales al secuencial
- [ ] Escalamiento fuerte en el clúster Xi
- [ ] Análisis de desbalance de carga
- [ ] Calibración con la imagen aérea real (ScienceBase)

**Entrega**
- [ ] Visualizaciones (PNG, GIF, curvas de speedup)
- [ ] Informe

## Equipo

Cristopher Angulo · Estrella Parraguez · Pablo

## Referencias

Ver [`docs/referencias.md`](docs/referencias.md).
