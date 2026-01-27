---
title: Cuadernos Reproducibles de Conocimiento del Riesgo
date: 2025-01-27
license: CC-BY-4.0
keywords:
  - Notebooks
  - Python
  - Métodos
  - Amenazas
  - Vulnerablidad
  - Exposición
  - Riesgo
  - Riesgo de desastres
  - Daños y pérdidas
abbreviations:
  IGN: Instituto Geográfico Nacional
  UTC: Coordinated Universal Time
  USGS: United States Geological Survey
---
:::{figure} ../images/banner.png
:name: banner-image
:class: banner-image
:width: 100%

+++ {"part": "abstract"}

Cuadernos Reproducibles de Conocimiento del Riesgo
:::

Los Cuadernos Reproducibles de Conocimiento del Riesgo tienen el objetivo de compartir datos, herramientas y flujos de trabajo para fomentar la investigación y tecnologías reproducibles y reutilizables en gestión del riesgo de desastres.

Los cuadernos  son un espacio para el intercambio de ideas, trabajos recientes e impactos dentro de la comunidad profesional y de investigación en riesgos de desastres en Colombia. Bajo la sombrilla de plataforma Riesgos, busca que estudiantes, investigadores y profesionales compartan sus investigaciones más recientes y aplicaciones que emplean el modelado y la simulación computacional para comprender y reducir los riesgos de desastres.

```         

### Spatial Distribution

The spatial distribution of earthquakes reveals two main clusters:

**Cluster 1 - Shallow/Intermediate (8-15 km depth)**
- Located beneath the central part of the island
- Associated with crustal magma reservoir
- Earthquake magnitudes typically ML 2.0-3.5

**Cluster 2 - Deep (20-35 km depth)**  
- Located slightly offshore to the west
- Associated with mantle reservoir and deep magma ascent
- Earthquake magnitudes typically ML 1.5-4.5

```{figure} spatial_distribution.png
---
name: fig-spatial
width: 100%
---
Spatial distribution of earthquakes colored by depth. The shallow cluster (red) is located beneath the island, while the deep cluster (blue) extends offshore. The eruption site is marked with a star.
```

### Depth Distribution

The depth distribution analysis confirms the two-reservoir model:

$$N(z) = A_1 \exp\left(-\frac{(z-z_1)^2}{2\sigma_1^2}\right) + A_2 \exp\left(-\frac{(z-z_2)^2}{2\sigma_2^2}\right)$$ (eq:depth-dist)

Where: - $z_1 = 12 \pm 2$ km (crustal reservoir depth) - $z_2 = 28 \pm 4$ km (mantle reservoir depth) - $A_1, A_2$ are amplitude parameters - $\sigma_1, \sigma_2$ are depth uncertainties

### Magnitude-Frequency Analysis

The Gutenberg-Richter relationship for La Palma seismicity follows:

$$\log_{10} N = a - bM$$ (eq:gutenberg-richter)

Where: - $N$ = cumulative number of earthquakes ≥ magnitude $M$ - $a = 4.2 \pm 0.1$ (activity parameter) - $b = 1.1 \pm 0.1$ (slope parameter)

The b-value of 1.1 is typical for volcanic environments and indicates a high proportion of smaller earthquakes relative to larger ones {cite}`mcnutt2005seismic`.

\`\`\`{figure} magnitude_frequency.png 31b8e172-b470-440e-83d8-e6b185028602:dAB5AHAAZQA6AFoAUQBBAHgAQQBEAGcAQQBNAFEAQQA1AEEARABZAEEATQBBAEEAMQBBAEMAMABBAE0AQQBCAGgAQQBHAE0AQQBaAEEAQQB0AEEARABRAEEAWgBnAEIAaABBAEcAVQBBAEwAUQBBADQAQQBHAEkAQQBPAFEAQQA1AEEAQwAwAEEATwBRAEIAagBBAEQARQBBAFkAZwBBADMAQQBHAEkAQQBaAEEAQQAzAEEARwBNAEEATQBBAEIAbQBBAEQARQBBAAoAcABvAHMAaQB0AGkAbwBuADoATgB3AEEAeABBAEQASQBBAE0AQQBBAD0ACgBwAHIAZQBmAGkAeAA6AAoAcwBvAHUAcgBjAGUAOgBMAFEAQQB0AEEAQwAwAEEAQwBnAEIAdQBBAEcARQBBAGIAUQBCAGwAQQBEAG8AQQBJAEEAQgBtAEEARwBrAEEAWgB3AEEAdABBAEcAMABBAFkAUQBCAG4AQQBHADQAQQBhAFEAQgAwAEEASABVAEEAWgBBAEIAbABBAEEAbwBBAGQAdwBCAHAAQQBHAFEAQQBkAEEAQgBvAEEARABvAEEASQBBAEEANABBAEQAQQBBAEoAUQBBAEsAQQBDADAAQQBMAFEAQQB0AEEAQQA9AD0ACgBzAHUAZgBmAGkAeAA6AA==:31b8e172-b470-440e-83d8-e6b185028602

Magnitude-frequency distribution for La Palma earthquakes. The plot shows the characteristic power-law relationship with a b-value of 1.1, typical for volcanic seismicity.

```         

## Statistical Analysis

### Seismic Rate Changes

We applied change-point analysis to identify significant changes in seismic rate:

```python
import ruptures as rpt

# Prepare time series data
daily_counts = df.groupby(df['datetime'].dt.date).size()
signal = daily_counts.values

# Change-point detection
algo = rpt.Pelt(model="rbf").fit(signal)
result = algo.predict(pen=10)

print(f"Change points detected: {result}")
```

The analysis identified three major change points: 1. **May 2020**: Transition from background to elevated activity\
2. **July 2021**: Onset of pre-eruptive intensification 3. **September 19, 2021**: Eruption onset

### Correlation Analysis

Cross-correlation between shallow and deep seismicity reveals:

$$r(τ) = \frac{\sum_{t} [x_s(t) - \bar{x}_s][x_d(t+τ) - \bar{x}_d]}{\sqrt{\sum_t [x_s(t) - \bar{x}_s]^2 \sum_t [x_d(t+τ) - \bar{x}_d]^2}}$$ (eq:correlation)

Where $x_s(t)$ and $x_d(t)$ are shallow and deep earthquake counts at time $t$.

Results show maximum correlation at τ = 0 days with r = 0.72, indicating synchronized activation of both reservoir levels.

## Discussion

### Magma System Dynamics

The seismic data supports a model where:

1.  **Deep reservoir activation** (2017-2020): Slow magma accumulation at mantle depths
2.  **Crustal reservoir charging** (2020-2021): Magma ascent and storage at crustal levels\
3.  **Final ascent** (September 2021): Rapid magma transport to surface

### Hazard Implications

The analysis has important implications for volcanic hazard assessment:

:::{admonition} Key Findings :class: important

-   **Early warning**: Deep seismicity provides months of advance warning
-   **Eruption timing**: Shallow swarms indicate imminent eruption (days to weeks)
-   **Duration prediction**: Correlation between pre-eruptive seismic energy and eruption duration :::

### Comparison with Other Systems

La Palma's seismic patterns are similar to those observed at other ocean island volcanoes:

| Volcano      | Deep Swarm Depth | Shallow Swarm Depth | Lead Time    |
|--------------|------------------|---------------------|--------------|
| Kilauea      | 30-60 km         | 3-8 km              | Weeks-Months |
| Etna         | 20-30 km         | 5-15 km             | Days-Weeks   |
| **La Palma** | **20-35 km**     | **8-15 km**         | **Months**   |
| Stromboli    | 10-20 km         | 2-6 km              | Hours-Days   |

: Comparison of seismic patterns at ocean island volcanoes {#tbl-comparison}

## Conclusions

The 2021 La Palma eruption was preceded by a complex pattern of seismic activity that provides insights into the magma plumbing system:

1.  **Two-reservoir system**: Seismicity confirms mantle (20-35 km) and crustal (8-15 km) magma reservoirs
2.  **Long-term precursors**: Deep seismicity began increasing in 2017, providing years of warning
3.  **Short-term precursors**: Shallow seismicity intensified weeks before eruption
4.  **Synchronized activation**: Strong correlation between deep and shallow earthquake rates

These findings have important implications for: - **Volcanic monitoring**: Multi-depth seismic networks essential for eruption forecasting - **Hazard assessment**: Different phases of unrest require different response protocols\
- **Scientific understanding**: Confirms conceptual models of ocean island volcano plumbing systems

Future work should focus on: - Real-time implementation of change-point detection algorithms - Integration with other monitoring techniques (geodesy, gas emissions) - Development of probabilistic eruption forecasting models

## Acknowledgments

The authors thank the Instituto Geográfico Nacional (IGN) for providing the earthquake catalog data. We also acknowledge the staff at the Observatorio Geofísico Central for their continuous monitoring efforts during the crisis.

## Data Availability

The earthquake catalog data used in this study is available from the IGN at https://www.ign.es/web/ign/portal/sis-catalogo-terremotos. Processing scripts and analysis code are available at https://github.com/curvenote/la-palma-seismicity.

## References

```{bibliography}
:style: agu
:filter: docname in docnames
```