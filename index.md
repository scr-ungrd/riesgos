---
title: Plataforma de Análisis de Riesgos
subtitle: Repositorio Científico y Plataforma de Conocimiento — UNGRD
authors:
  - name: Subdirección para el Conocimiento del Riesgo
    affiliation: Unidad Nacional para la Gestión del Riesgo de Desastres (UNGRD)
    github: scr-ungrd
---

::::{hero}

# Plataforma de Análisis de Riesgos

## Subdirección para el Conocimiento del Riesgo · UNGRD

Repositorio científico abierto para el análisis, modelado y visualización del riesgo de desastres en Colombia. Integra análisis reproducibles, datos geoespaciales y herramientas de inteligencia territorial.

:::{button-link} conceptos/amenaza-sismica
:color: primary
:shadow:
Explorar Amenazas →
:::
:::{button-link} notebooks/cuadernos-de-conocimiento
:color: secondary
:shadow:
Ver Cuadernos de Análisis →
:::
::::

---

## ¿Qué es esta plataforma?

Esta plataforma reúne contenidos, datos y herramientas para entender cómo se distribuyen los riesgos naturales en Colombia y cómo pueden incorporarse en procesos de análisis territorial, ordenamiento, adaptación y toma de decisiones. Está diseñada para investigadores, tomadores de decisiones y profesionales de la gestión del riesgo que necesitan acceder, reproducir y construir sobre análisis científicos rigurosos.

Los mapas e indicadores de amenaza y riesgo deben interpretarse de acuerdo con su escala, resolución y propósito. Un resultado nacional permite identificar patrones, contrastes regionales y zonas prioritarias, pero no reemplaza estudios de detalle para diseño, ordenamiento o intervención local. Por eso esta plataforma combina una mirada general del país con rutas de profundización por fenómeno, región y fuente técnica.

::::{grid} 1 2 2 4
:gutter: 3

:::{card}
:class-header: bg-primary text-white
:link: conceptos/identificacion-escenarios
:link-type: doc
📊 **Análisis Reproducibles**
^^^
Cuadernos Jupyter ejecutables con datos reales. Reproduce, adapta y extiende los análisis directamente en el navegador o tu entorno local.
:::

:::{card}
:class-header: bg-success text-white
:link: conceptos/amenaza-sismica
:link-type: doc
🗺️ **Datos Geoespaciales**
^^^
Visualización interactiva de amenazas, fallas activas, zonas de riesgo y datos satelitales integrados con Google Earth Engine.
:::

:::{card}
:class-header: bg-warning
:link: notebooks/cuadernos-de-conocimiento
:link-type: doc
🔬 **Ciencia Abierta**
^^^
Todo el código, datos y metodologías son abiertos y reproducibles, siguiendo los principios FAIR de la ciencia abierta.
:::

:::{card}
:class-header: bg-danger text-white
:link: eventos/taller-radares
:link-type: doc
📡 **Conocimiento Aplicado**
^^^
Integración de eventos de formación, talleres técnicos y documentación de capacidades institucionales.
:::

::::

---

## Del Peligro al Riesgo

Los fenómenos naturales no se convierten en desastre por sí solos. Sus efectos dependen de dónde ocurren, qué población e infraestructura están expuestas, cuáles son las condiciones sociales y ambientales del territorio y qué tan preparada está la sociedad para anticiparlos, responder y recuperarse.

::::{grid} 1 2 2 4
:gutter: 3

:::{card}
:class-header: bg-danger text-white
⚡ **Amenaza**
^^^
La posible ocurrencia e intensidad de un fenómeno físico potencialmente dañino (sismo, inundación, deslizamiento).
:::

:::{card}
:class-header: bg-warning
🏘️ **Exposición**
^^^
La población, infraestructura, ecosistemas y actividades ubicadas en áreas donde el fenómeno puede ocurrir.
:::

:::{card}
:class-header: bg-primary text-white
🧩 **Vulnerabilidad**
^^^
Qué tan susceptibles son esos elementos a sufrir daños o pérdidas ante la ocurrencia del fenómeno.
:::

:::{card}
:class-header: bg-success text-white
📊 **Riesgo**
^^^
Resultado de la interacción entre amenaza, exposición y vulnerabilidad. Cambia entre regiones, municipios y escalas de análisis.
:::

::::

:::{admonition} Un mismo fenómeno, efectos distintos
:class: tip
Un mismo evento puede producir consecuencias muy diferentes según la calidad del hábitat, el acceso a servicios, las condiciones ambientales, la resiliencia institucional y la capacidad de preparación y respuesta de cada territorio.
:::

---

## Amenazas Naturales

En Colombia convergen procesos tectónicos, climáticos, geomorfológicos e hidrológicos que configuran un territorio dinámico y diverso. Esa combinación explica la presencia simultánea de sismos, actividad volcánica, inundaciones, avenidas torrenciales, movimientos en masa, sequías, incendios forestales y fenómenos costeros. Las amenazas se manifiestan de forma distinta según la región: mientras las áreas andinas concentran la mayor parte de la amenaza sísmica y volcánica, las llanuras aluviales presentan alta recurrencia de inundaciones, y las zonas costeras están expuestas a procesos marinos.

[→ Ver análisis completo de fenómenos naturales en Colombia](conceptos/fenomenos-naturales.md)

::::{grid} 1 2 3 3
:gutter: 3

:::{card}
:link: conceptos/amenaza-sismica
:link-type: doc
:class-header: bg-danger text-white
🏔️ **Amenaza Sísmica**
^^^
Colombia se ubica en la convergencia de las placas Nazca, Caribe y Sudamérica. El **39.7%** de la población vive en zonas de amenaza sísmica alta.

**→ Ver análisis completo**
:::

:::{card}
:class-header: bg-primary text-white
🌊 **Inundaciones**
^^^
Las inundaciones son la amenaza de mayor recurrencia en Colombia, afectando principalmente las cuencas del Magdalena, Cauca y las zonas costeras.

*En desarrollo*
:::

:::{card}
:class-header: bg-warning
🌋 **Volcanes**
^^^
Colombia cuenta con más de 15 volcanes activos o potencialmente activos, monitoreados por el Sistema Geológico Colombiano.

*En desarrollo*
:::

:::{card}
:class-header: bg-success text-white
💧 **Movimientos en Masa**
^^^
Los deslizamientos y flujos de detritos son frecuentes en las zonas montañosas, exacerbados por eventos de lluvia intensa.

*En desarrollo*
:::

:::{card}
:class-header: bg-info text-white
🌀 **Ciclones Tropicales**
^^^
Las costas Atlántica y Pacífica están expuestas a la influencia de sistemas tropicales y el fenómeno ENSO.

*En desarrollo*
:::

:::{card}
:class-header: bg-secondary text-white
🌊 **Tsunamis**
^^^
La costa Pacífica colombiana presenta historial de tsunamis locales y lejanos, como el evento de Tumaco de 1906.

*En desarrollo*
:::

::::

---

## Cuadernos de Análisis

Los cuadernos de conocimiento son **documentos científicos ejecutables** que combinan texto, código, datos y visualizaciones en un solo entorno reproducible.

::::{grid} 1 2 2 2
:gutter: 3

:::{card}
:link: notebooks/la-palma-seismicity
:link-type: doc
:class-header: bg-danger text-white
🌋 **Sismicidad La Palma 2021**
^^^
Análisis de la crisis sísmica asociada a la erupción volcánica de La Palma, Canarias. Incluye detección de enjambres, análisis espacio-temporal y modelado de precursores.

`Python` · `Sismología` · `Series Temporales`
:::

:::{card}
:link: notebooks/lector-precipitacion-mensual
:link-type: doc
:class-header: bg-primary text-white
🌧️ **Precipitación Mensual**
^^^
Procesamiento y análisis de registros de precipitación de estaciones hidrometeorológicas del IDEAM. Visualización de patrones temporales y espaciales.

`Python` · `Hidrología` · `IDEAM`
:::

:::{card}
:link: notebooks/estaciones-hidrometeorologicas
:link-type: doc
:class-header: bg-success text-white
📡 **Red Hidrometeorológica**
^^^
Catálogo y análisis de la red de estaciones hidrometeorológicas de Colombia. Acceso a datos en tiempo real e históricos.

`Python` · `APIs` · `Geoespacial`
:::

:::{card}
:link: notebooks/inundacion-costera
:link-type: doc
:class-header: bg-warning
🌊 **Inundación Costera**
^^^
Modelado de inundación costera con escenarios de cambio climático. Análisis del nivel del mar y zonas de exposición en litorales colombianos.

`Python` · `Oceanografía` · `SLR`
:::

::::

---

## Integración con Google Earth Engine

:::{admonition} Análisis Geoespacial con GEE
:class: tip

Esta plataforma se integra con **Google Earth Engine (GEE)** para el acceso y análisis de datos satelitales a escala continental. GEE permite procesar petabytes de imágenes satelitales directamente en la nube sin necesidad de descargas locales.
:::

::::{grid} 1 2 2 3
:gutter: 3

:::{card}
:link: https://earthengine.google.com/
:class-header: bg-primary text-white
🛰️ **Imágenes Satelitales**
^^^
Acceso a archivos históricos de Landsat, Sentinel, MODIS y otros sensores para el análisis de cambios en el uso del suelo y cobertura vegetal.
:::

:::{card}
:link: https://earthengine.google.com/
:class-header: bg-success text-white
🌍 **Datos Climáticos**
^^^
Series temporales de precipitación (CHIRPS, ERA5), temperatura y humedad para análisis de exposición y vulnerabilidad climática.
:::

:::{card}
:link: https://earthengine.google.com/
:class-header: bg-warning
🗺️ **Cartografía de Amenazas**
^^^
Generación de mapas de amenaza combinando modelos físicos con datos satelitales: susceptibilidad a deslizamientos, inundaciones y sequías.
:::

::::

---

## Metodologías de Análisis

::::{tab-set}

:::{tab-item} Análisis Probabilista de Amenaza (PSHA)
El **Análisis Probabilista de Amenaza Sísmica (PSHA)** es el estándar internacional para la evaluación de la amenaza sísmica. Permite estimar la probabilidad de excedencia de diferentes niveles de movimiento del terreno en un sitio determinado.

**Herramientas utilizadas:**

- OpenQuake Engine (GEM Foundation)
- CRISIS V7.2
- Python: `numpy`, `scipy`, `pandas`, `matplotlib`

[→ Ver ejemplo en el cuaderno AGU](notebooks/agu-notebook.ipynb)
:::

:::{tab-item} Análisis Espacial
El análisis espacial integra datos geográficos de diferentes fuentes para identificar patrones de exposición, vulnerabilidad y riesgo en el territorio.

**Herramientas utilizadas:**

- QGIS / ArcGIS
- Python: `geopandas`, `rasterio`, `folium`, `leafmap`
- Google Earth Engine

[→ Ver estaciones hidrometeorológicas](notebooks/estaciones-hidrometeorologicas.md)
:::

:::{tab-item} Series Temporales
El análisis de series temporales permite identificar tendencias, patrones estacionales y anomalías en datos hidrometeorológicos, sísmicos y de teledetección.

**Herramientas utilizadas:**

- Python: `pandas`, `statsmodels`, `scikit-learn`
- R: `forecast`, `tsibble`
- Jupyter Notebooks

[→ Ver análisis de precipitación](notebooks/lector-precipitacion-mensual.ipynb)
:::

:::{tab-item} Modelado de Impacto
La evaluación de impacto combina modelos de amenaza, exposición y vulnerabilidad para estimar pérdidas potenciales en vidas humanas, infraestructura y economía.

**Herramientas utilizadas:**

- OpenQuake (pérdidas sísmicas)
- HAZUS (adaptado para Colombia)
- Python: `pandas`, `scipy`

[→ Ver análisis La Palma](notebooks/la-palma-seismicity.md)
:::

::::

---

## Sobre la Plataforma

::::{grid} 1 2 2 2
:gutter: 3

:::{card}
**🏛️ Institución**
^^^
**Unidad Nacional para la Gestión del Riesgo de Desastres (UNGRD)**

Subdirección para el Conocimiento del Riesgo
:::

:::{card}
**📋 Licencia y Datos**
^^^
El contenido de esta plataforma está disponible bajo licencia **Creative Commons BY 4.0**.

Los datos fuente provienen de entidades oficiales del Estado colombiano.
:::

:::{card}
**🔧 Tecnologías**
^^^
Construido con [MyST Markdown](https://mystmd.org), Jupyter Notebooks, Python y Google Earth Engine.

Alojado en GitHub Pages.
:::

:::{card}
**📬 Contacto**
^^^
Para colaborar, reportar errores o sugerir contenido, abre un issue en el repositorio de GitHub o contacta a la SCR-UNGRD.
:::

::::

---

:::{note}
Esta es una plataforma en construcción activa. Si deseas contribuir con análisis, datos o documentación, consulta las guías de contribución en el repositorio de GitHub.
:::
