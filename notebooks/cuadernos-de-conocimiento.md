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
:::

+++ {"part": "abstract"}

Cuadernos Reproducibles de Conocimiento del Riesgo

## Introducción

La producción de conocimiento técnico y científico en gestión del riesgo de desastres ha crecido de manera sostenida en Colombia durante la última década. Sin embargo, persistente la brecha que separa la generación de ese conocimiento de su reutilización efectiva: los métodos quedan atrapados en artículos científicos informes institucionales de difícil acceso, los datos de entrada no se publican junto con los resultados, y los análisis rara vez pueden ser verificados, extendidos o adaptados por terceros. Esta convocatoria nace como respuesta a esa brecha.

La Subdirección para el Conocimiento del Riesgo de la Unidad Nacional para la Gestión del Riesgo de Desastres (UNGRD), en el marco de la Plataforma Riesgos como proyecto de ciencia abierta alojado en GitHub, convoca a investigadores, analistas y profesionales técnicos del Sistema Nacional para la Gestión del Riesgo de Desastres (SNGRD) y de la comunidad académica en general a presentar cuadernos computacionales reproducibles que documenten metodologías, análisis y flujos de trabajo aplicados al conocimiento del riesgo en Colombia.

Los Cuadernos Reproducibles de Conocimiento del Riesgo tienen el objetivo de compartir datos, herramientas y flujos de trabajo para fomentar la investigación y tecnologías reproducibles y reutilizables en gestión del riesgo de desastres.

Un cuaderno computacional reproducible no es simplemente un script con comentarios: es un documento científico ejecutable que combina narrativa explicativa, código verificable, datos de entrada accesibles y resultados interpretados en un único objeto publicable. Esta concepción está en el corazón del movimiento internacional de ciencia abierta soportado que los principios FAIR —Findable, Accessible, Interoperable, Reusable— que son la base de toda publicación científica moderna orientada a la transparencia y la reproducibilidad, especialmente en estudios con alta densidad de datos y computación intensiva. Los cuadernos computacionales son hoy el vehículo más directo para operacionalizar esos principios.

Existen iniciativas internacionales de referencia han consolidado ecosistemas de cuadernos abiertos que articulan datos, métodos y narrativa dentro de repositorios públicos en GitHub. Algunos ejemplos son:

-   Manual de Evaluación del Riesgo Climático de CLIMAAX (https://handbook.climaax.eu/intro.html)

-   Risk Data Library del Global Facility for Disaster Reduction and Recovery (https://gfdrr.github.io/CCDR-tools/home.html)

-   Design Safe (https://www.designsafe-ci.org/)

-   European Centre for Medium-Range Weather Forecasts, Probability of Fire Jupyter Book (https://ecmwf.github.io/AI-Probability-of-Fire)

-   Proyecto Pythia (https://projectpythia.org/) EM-DAT (https://github.com/em-dat/)

Estas iniciativas emplean arquitecturas que implementan usando Jupyter Notebooks enriquecidos con MyST Markdown, organizados por amenaza y publicados bajo licencia abierta, que en conjunto constituyen el modelo de referencia que esta convocatoria adopta y adapta al contexto colombiano. El propósito de esta convocatoria es doble: construir un corpus verificable de metodologías computacionales para el análisis del riesgo en Colombia, y establecer una comunidad de práctica que eleve los estándares de reproducibilidad y apertura en el campo de la gestión del riesgo a nivel institucional y académico.

## Enfoque de los cuadernos 

Esta convocatoria define los cuadernos aceptables a partir de cuatro líneas temáticas prioritarias, que corresponden a los componentes centrales del análisis del riesgo conforme al Marco de Sendai para la Reducción del Riesgo de Desastres 2015–2030 y a la Ley 1523 de 2012: 

**Evaluación de amenazas**. Cuadernos que documenten metodologías para la caracterización, modelación o cartografía de amenazas naturales o socio naturales como inundaciones, movimientos en masa, sismos, sequías, incendios de la cobertura vegetal, entre otras— relevantes para el territorio colombiano. Se valoran especialmente los enfoques probabilísticos, el uso de series históricas de registros institucionales (e.g. desde UNGRD, IDEAM, SGC, IGAC) y la integración de escenarios de cambio climático.

**Análisis de riesgo**. Cuadernos que articulen datos de amenaza con información de exposición y vulnerabilidad para estimar el riesgo relativo o absoluto a nivel municipal, departamental o de cuenca. Este tipo de contribución sigue la arquitectura metodológica consolidada por plataformas como CLIMAAX, donde los flujos de trabajo separan explícitamente la evaluación de la amenaza del análisis del riesgo en cuadernos encadenados dentro de un mismo repositorio.

**Indicadores de vulnerabilidad y exposición**. Cuadernos enfocados en la construcción, validación o comparación de indicadores de vulnerabilidad social, física o funcional, y de exposición de población, infraestructura o activos. Se invita a utilizar fuentes de datos abiertas como el Censo Nacional de Población (DANE), el Registro Único de Damnificados, y los datos de catastro multipropósito, documentando los criterios de selección, normalización y ponderación de variables.

**Metodologías transversales**. Cuadernos que presenten herramientas, pipelines de procesamiento o marcos analíticos aplicables a más de una amenaza o escala territorial. Este tipo de contribución es análoga a la categoría Workflows reconocida por diversas revistas científicas, que describe ensamblajes novedosos de herramientas de software o procedimientos empíricos organizados en pipelines útiles para el análisis de datos complejos de importancia demostrable. En el contexto de esta convocatoria, se entiende por metodología transversal cualquier contribución cuyo valor resida en la generalidad y transferibilidad del método, más que en los resultados aplicados a un caso específico. 

**Stack tecnológico**. Todos los cuadernos deben desarrollarse con el siguiente stack tecnológico:

- **MyST Markdown** como lenguaje de marcado para la narrativa científica, las referencias cruzadas, las notas metodológicas y los metadatos estructurados del cuaderno. MyST permite enriquecer la presentación con directivas semánticas (`{note}`, `{warning}`, `{figure}`, `{bibliography}`) y es el formato base del proyecto Riesgos de UNGRD en GitHub, así como del Manual de CLIMAAX.
- **Python 3.10 o superior** como lenguaje de programación para todos los componentes computacionales. Las bibliotecas recomendadas incluyen `xarray`, `geopandas`, `rasterio`, `pandas`, `matplotlib`, `cartopy` y `numpy`, sin perjuicio de otras que el autor justifique.
- **Jupyter Notebook o JupyterLab** como entorno de ejecución interactiva. Los cuadernos deben poder ejecutarse de inicio a fin sin intervención manual, salvo la descarga explícita de datos externos cuando esta sea inevitable.
- **GitHub** como plataforma de control de versiones y publicación pública del repositorio. No se aceptarán contribuciones que no cuenten con un repositorio público en GitHub al momento de la evaluación.

**Alineación con estándares de datos de riesgo**. Los cuadernos que utilicen o produzcan datos de riesgo deben alinearse, en la medida de lo posible, con el Risk Data Library Standard (RDLS) desarrollado por GFDRR, un estándar abierto que provee un lenguaje común para describir datos de amenaza, exposición, vulnerabilidad y pérdidas en evaluaciones de riesgo climático y de desastres. La adopción del RDLS facilita la interoperabilidad con colecciones de datos del Banco Mundial y con otras iniciativas de datos abiertos para la resiliencia, en línea con el principio de interoperabilidad de los datos FAIR.

## Requisitos de un cuaderno reproducible

La reproducibilidad no es una propiedad binaria: es un espectro que va desde la disponibilidad del código hasta la ejecución automática y verificable en cualquier entorno. Esta convocatoria adopta un estándar de reproducibilidad funcional y documentada, definido por los siguientes requisitos obligatorios y recomendados.

### Estructura del repositorio GitHub

El repositorio debe contener como mínimo:

- `README.md` con título, descripción breve, instrucciones de instalación, descripción de los datos de entrada y un ejemplo de ejecución.
- `environment.yml` (conda) o `requirements.txt` (pip) con todas las dependencias y sus versiones fijadas.
- Carpeta `notebooks/` con los cuadernos `.ipynb` numerados en orden de ejecución.
- Carpeta `data/` con los datos de ejemplo necesarios para ejecutar el cuaderno en su versión mínima, o instrucciones claras para su descarga automatizada.
- Archivo `LICENSE` con una licencia abierta. Se recomienda Apache 2.0 para el código y CC BY 4.0 para los datos y la documentación narrativa, siguiendo el modelo de CLIMAAX.

Se recomienda adicionalmente incluir un archivo `CITATION.cff` para facilitar la citación formal del repositorio, y configurar la integración con Binder (mybinder.org) mediante un botón de lanzamiento en el README, de modo que cualquier lector pueda ejecutar el cuaderno en la nube sin instalación local.

### Principios FAIR aplicados al cuaderno

Cada cuaderno debe operacionalizar los cuatro principios FAIR de la siguiente manera:

**Findable (Encontrable)**. El repositorio debe registrarse en Zenodo para obtener un DOI permanente antes de la evaluación final. El `README.md` debe incluir metadatos mínimos: título, autores, institución, palabras clave temáticas (amenaza, departamento, escala espacial) y referencia al DOI.

**Accessible (Accesible)**. El repositorio debe ser público en GitHub. Los datos de entrada utilizados en el cuaderno deben estar disponibles en formatos abiertos (GeoTIFF, GeoJSON, CSV, NetCDF) sin restricciones de licencia que impidan su descarga y reutilización. Si los datos provienen de fuentes institucionales con restricciones, el cuaderno debe incluir instrucciones precisas para su solicitud y un conjunto de datos sintéticos o de muestra que permita verificar la ejecución completa del flujo de trabajo.

**Interoperable (Interoperable)**. Los formatos de datos deben ser compatibles con las bibliotecas estándar del ecosistema Python científico. Los cuadernos que produzcan datos de riesgo deben documentar sus esquemas de salida con referencia al RDLS cuando aplique. Las unidades, sistemas de referencia de coordenadas (CRS) y convenciones de nomenclatura deben declararse explícitamente en el código.

**Reusable (Reutilizable)**. La licencia abierta es condición necesaria pero no suficiente. El código debe estar modularizado en funciones documentadas con docstrings. La narrativa en MyST debe explicar no solo el qué sino el por qué de cada decisión metodológica: selección de parámetros, umbrales de clasificación, fuentes de datos preferidas. Un cuaderno reutilizable es aquel que un técnico con conocimientos equivalentes puede adaptar a un municipio o amenaza diferente sin necesidad de contactar al autor. 

### Estructura narrativa del cuaderno

Los cuadernos deben seguir la siguiente estructura narrativa mínima, implementada en celdas de texto MyST intercaladas con el código:

- **Contexto y objetivo** — descripción del problema, escala territorial y justificación de la metodología seleccionada.
- **Datos de entrada** — descripción de fuentes, formatos, resolución espaciotemporal y limitaciones conocidas.
- **Metodología** — desarrollo paso a paso con explicación narrativa de cada bloque de código. Las celdas de código deben incluir comentarios en línea para las operaciones no triviales.
- **Resultados e interpretación** — visualizaciones comentadas con análisis del significado de los resultados en términos de gestión del riesgo.
- **Limitaciones y recomendaciones** — discusión honesta de los supuestos del modelo, las incertidumbres no cuantificadas y los pasos sugeridos para extender el análisis.
- **Referencias** — gestionadas mediante la directiva `{bibliography}` de MyST, con archivo `.bib` incluido en el repositorio.

### Control de calidad antes de la entrega

Antes de la presentación formal, el autor debe verificar que:

- El cuaderno se ejecuta completamente desde cero en un entorno limpio creado a partir del `environment.yml` o `requirements.txt` del repositorio.
- Ninguna celda depende de variables definidas en celdas ejecutadas fuera de orden.
- Las rutas de archivos son relativas al repositorio, no absolutas al sistema local del autor.
- El repositorio ha sido etiquetado con al menos un release en GitHub y la versión correspondiente en Zenodo tiene DOI activo.

El cumplimiento de estos requisitos será verificado por el comité evaluador mediante ejecución independiente del cuaderno en un entorno limpio, siguiendo el principio de que la reproducibilidad de un análisis sólo puede certificarse cuando alguien diferente al autor lo ejecuta sin asistencia.
