# El modelo

Basado en **Liu & Estep (2025)**, *A multiscale stochastic cellular automata model for dispersion of mountain pine beetles*, Royal Society Open Science 12: 241934. DOI [10.1098/rsos.241934](https://doi.org/10.1098/rsos.241934). Código de los autores: <https://github.com/Irene-liu-724/MPB-Infestation>.

## Qué representa cada celda

Cada celda es un **parche de bosque**, no un árbol. Su estado es la **densidad de escarabajos** $\pi_{ij}(t) \in [0, 1]$: 0 es sin escarabajos y 1 es la capacidad máxima. La grilla es **hexagonal**: cada celda tiene 6 vecinos, y la vecindad completa son 7 celdas (ella más sus vecinos).

## Un paso de tiempo (un año)

### 1. Microescala: nacimiento y muerte

Cada celda corre $M$ réplicas de $N$ pasos ($\Delta\tau = 1/N$) desde $X(0) = \pi_{ij} C$:

$$P(n \to n+1) = b\,n\left(1 - \frac{n}{C}\right)\Delta\tau \qquad P(n \to n-1) = d\,n\,\Delta\tau$$

$$\pi_{ij} \leftarrow \frac{1}{M}\sum_{\ell=1}^{M}\frac{X_\ell(1)}{C}$$

### 2. Emisión

$$\bar\pi_{ij} = \text{media de la vecindad} \qquad e_{ij} = \gamma_1(\pi_{ij} - \bar\pi_{ij}) \text{ si } \pi_{ij} > \bar\pi_{ij}$$

### 3. Actualización

Lo emitido se reparte en partes iguales entre la vecindad, y llega sólo la fracción $\gamma_2$. Una celda que recibe escarabajos se establece con probabilidad:

$$p_S = \varphi + \rho \arctan(\pi)$$

### Fronteras

Absorbentes: fuera del mapa hay celdas auxiliares que reciben dispersión pero no dispersan.

## Parámetros (Tabla 2 del paper)

| Parámetro | Valor | Significado |
|---|---|---|
| `b` | 1.0 | natalidad |
| `d` | 0.2 | mortalidad |
| `C` | 100 | capacidad de carga por celda |
| `N` | 100 | pasos microscópicos por año |
| `M` | 20 | réplicas por celda |
| `gamma1` | 0.8 | fracción del exceso que se dispersa |
| `gamma2` | 0.8 | fracción de dispersores que sobrevive al viaje |
| `phi` | 1/3 | supervivencia base |
| `rho` | 1/3 | supervivencia dependiente de la densidad |

## Decisiones pendientes

1. **¿Vecindad local o la del paper?** El paper calcula la media sobre "vecindades de interacción": grupos de celdas infestadas separadas por como máximo dos celdas vacías. Esos grupos pueden cruzar todo el mapa y no son locales, lo que complica la paralelización con halos. Propuesta: usar la vecindad de 7 celdas y documentar la diferencia.
2. **Inclusión estocástica.** En el paper no todas las celdas participan: se sortea con $p_I = \frac{w}{1+w}\,d_{\max}$. ¿La incluimos?
3. **Supervivencia.** En el paper, una celda receptora que falla el sorteo queda en 0 aunque ya estuviera infestada. ¿Lo aplicamos sólo a colonizaciones nuevas?
4. **Redondeo** de $\pi C$ a entero en la microescala.
5. **Estacionalidad** (natalidad periódica del paper): ¿sí o no?

## Datos para calibrar

Imagen aérea de una infestación real (ScienceBase): <https://www.sciencebase.gov/catalog/item/560312d0e4b03bc34f5449aa>. Guardarla procesada en `datos/` como `.npy`.
