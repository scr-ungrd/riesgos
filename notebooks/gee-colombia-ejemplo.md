---
title: Google Earth Engine en la Plataforma UNGRD
subtitle: Análisis satelital de amenazas naturales — JavaScript, Python y mapas embebidos
authors:
  - name: Subdirección para el Conocimiento del Riesgo
    affiliation: UNGRD
    github: scr-ungrd
keywords: [Google Earth Engine, GEE, geemap, teledetección, amenazas, Colombia, NDVI, inundaciones]
date: 2025-01-01
---

# Google Earth Engine en la Plataforma UNGRD

**Google Earth Engine (GEE)** es una plataforma de procesamiento geoespacial en la nube que da acceso a más de 70 petabytes de imágenes satelitales, datos climáticos, topografía y modelos digitales de terreno — de forma gratuita para investigación, educación y uso no comercial.

Esta página explica **tres formas de usar GEE** desde esta plataforma, según el nivel técnico del usuario y el tipo de análisis:

::::{grid} 1 2 3 3
:gutter: 3

:::{card}
:class-header: bg-warning
**Modo 1**
JavaScript · Code Editor
^^^
Escribe y ejecuta código GEE directamente en el navegador. Sin instalar nada.
**→ Requiere cuenta Google**
:::

:::{card}
:class-header: bg-primary text-white
**Modo 2**
Python · geemap · Binder
^^^
Análisis reproducibles con Python usando `geemap`. Ejecutable en Binder sin instalación local.
**→ Requiere cuenta Google**
:::

:::{card}
:class-header: bg-success text-white
**Modo 3**
Mapas embebidos
Visualización pública
^^^
Mapas GEE publicados como apps embebidas directamente en la plataforma.
**→ Sin cuenta requerida**
:::

::::

---

## Modo 1 — JavaScript en el Code Editor de GEE

El **Code Editor** de GEE (`code.earthengine.google.com`) es un entorno de desarrollo JavaScript en el navegador. Es la interfaz principal de GEE y la más usada por la comunidad científica para exploración y prototipado.

:::{admonition} Cuenta Google requerida
:class: note
Para ejecutar código en el Code Editor necesitas una cuenta Google con acceso a Earth Engine. El registro es gratuito en [earthengine.google.com/signup](https://earthengine.google.com/signup) para uso académico o de investigación.
:::

### Ejemplo: Detección de Inundaciones con Sentinel-1 (SAR)

El siguiente script analiza imágenes de radar de apertura sintética (SAR) del satélite Sentinel-1 para detectar zonas inundadas en Colombia durante un evento de inundación. El SAR penetra las nubes, lo que lo hace ideal para análisis de inundaciones en regiones tropicales.

```{code-block} javascript
:caption: "Script GEE — Detección de inundaciones con Sentinel-1 SAR"
:linenos:

// ============================================================
// Detección de inundaciones con Sentinel-1 SAR — Colombia
// Plataforma UNGRD · Subdirección para el Conocimiento del Riesgo
// ============================================================

// 1. Área de estudio — Depresión Momposina (región Caribe)
var aoi = ee.Geometry.Rectangle([-75.5, 8.5, -73.5, 10.5]);

// 2. Colección Sentinel-1 — polarización VV, modo IW
var s1 = ee.ImageCollection('COPERNICUS/S1_GRD')
  .filter(ee.Filter.eq('instrumentMode', 'IW'))
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
  .filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'))
  .filterBounds(aoi);

// 3. Imágenes antes y durante el evento de inundación
var antes     = s1.filterDate('2021-09-01', '2021-09-30').mean().select('VV');
var durante   = s1.filterDate('2021-11-01', '2021-11-30').mean().select('VV');

// 4. Diferencia de backscatter — zonas con gran cambio = inundadas
var diferencia = durante.subtract(antes);
var umbral     = -3;  // dB — ajustar según el evento

// 5. Máscara de agua permanente para excluir cuerpos de agua naturales
var jrcPerm = ee.Image('JRC/GSW1_4/GlobalSurfaceWater')
  .select('seasonality')
  .gte(10);  // agua presente >10 meses/año

// 6. Clasificación de inundación
var inundacion = diferencia.lt(umbral)
  .and(jrcPerm.not())
  .selfMask();

// 7. Calcular área inundada
var areaInundada = inundacion.multiply(ee.Image.pixelArea())
  .reduceRegion({
    reducer: ee.Reducer.sum(),
    geometry: aoi,
    scale: 10,
    maxPixels: 1e10
  });

print('Área inundada (km²):',
      ee.Number(areaInundada.get('VV')).divide(1e6).round());

// 8. Visualización
Map.centerObject(aoi, 8);
Map.addLayer(antes, {min: -25, max: 0}, 'SAR antes (sep 2021)', false);
Map.addLayer(durante, {min: -25, max: 0}, 'SAR durante (nov 2021)', false);
Map.addLayer(diferencia, {min: -10, max: 5, palette: ['blue','white','red']},
             'Cambio SAR (dB)');
Map.addLayer(inundacion, {palette: ['0000FF']}, 'Inundación detectada');

// 9. Exportar a Google Drive (opcional)
Export.image.toDrive({
  image: inundacion.toByte(),
  description: 'inundacion_momposina_2021',
  folder: 'GEE_UNGRD',
  region: aoi,
  scale: 10,
  crs: 'EPSG:4326'
});
```

:::{admonition} Abrir en Google Earth Engine Code Editor
:class: tip
Copia el código y pégalo en [code.earthengine.google.com](https://code.earthengine.google.com) para ejecutarlo. Necesitas una cuenta Google con acceso a Earth Engine.
:::

---

### Ejemplo: Susceptibilidad a Incendios — NDVI + temperatura

```{code-block} javascript
:caption: "Script GEE — Índice de susceptibilidad a incendios forestales"
:linenos:

// ============================================================
// Susceptibilidad a incendios — NDVI + LST + Humedad
// Colombia — Temporada seca (enero-marzo 2024)
// ============================================================

var colombia = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')
  .filter(ee.Filter.eq('country_co', 'CO'));

// MODIS Terra — NDVI mensual
var ndvi = ee.ImageCollection('MODIS/061/MOD13A3')
  .filterDate('2024-01-01', '2024-03-31')
  .filterBounds(colombia)
  .select('NDVI')
  .mean()
  .multiply(0.0001)           // factor de escala
  .clip(colombia);

// MODIS — Temperatura superficial LST (Land Surface Temperature)
var lst = ee.ImageCollection('MODIS/061/MOD11A2')
  .filterDate('2024-01-01', '2024-03-31')
  .filterBounds(colombia)
  .select('LST_Day_1km')
  .mean()
  .multiply(0.02).subtract(273.15)  // convertir a °C
  .clip(colombia);

// Puntos de calor activos (FIRMS — VIIRS 375m)
var incendios = ee.ImageCollection('FIRMS')
  .filterDate('2024-01-01', '2024-03-31')
  .filterBounds(colombia)
  .select('T21')
  .max()
  .clip(colombia);

// Índice de susceptibilidad combinado (normalizado 0-1)
var susceptibilidad = lst.subtract(lst.reduceRegion(ee.Reducer.min(),colombia,1000).getNumber('LST_Day_1km'))
  .divide(50)  // normalizar temperatura
  .add(ndvi.multiply(-1).add(1))  // inverso de NDVI (vegetación seca = mayor riesgo)
  .divide(2)
  .rename('susceptibilidad');

// Visualización
Map.centerObject(colombia, 6);

var paletaVerde  = ['darkgreen','yellow','orange','red','darkred'];
Map.addLayer(ndvi, {min: 0, max: 1, palette: paletaVerde.reverse()}, 'NDVI (ene-mar 2024)');
Map.addLayer(lst,  {min: 20, max: 45, palette: ['blue','yellow','orange','red']}, 'Temperatura LST (°C)');
Map.addLayer(susceptibilidad, {min: 0, max: 1, palette: ['green','yellow','red']},
             'Susceptibilidad a incendios');

print('NDVI promedio Colombia:', ndvi.reduceRegion(ee.Reducer.mean(), colombia, 5000));
print('LST promedio Colombia:', lst.reduceRegion(ee.Reducer.mean(), colombia, 5000));
```

---

## Modo 2 — Python con geemap (ejecutar en Binder)

`geemap` es una biblioteca Python que envuelve la API de GEE y añade visualización interactiva con `ipyleaflet` y `folium`. Funciona perfectamente en el entorno **Binder** de esta plataforma.

:::{admonition} Cómo ejecutar este cuaderno en Binder
:class: tip
Haz clic en el botón **"Abrir en Binder"** en la parte superior de esta página. Se lanzará un servidor Jupyter gratuito con todas las dependencias instaladas. La primera ejecución tarda 2-5 minutos mientras el entorno se construye.

**Nota:** Al ejecutar la primera celda, GEE pedirá autenticación. Sigue las instrucciones para vincular tu cuenta Google.
:::

```python
# ── Celda 1: Configuración del entorno ────────────────────────────────────────
import sys

_ES_JUPYTERLITE = 'pyodide' in sys.modules

if _ES_JUPYTERLITE:
    # geemap no está disponible en JupyterLite (requiere conexión a GEE)
    print("⚠️ Los análisis GEE con Python requieren el entorno Binder.")
    print("   Haz clic en 'Abrir en Binder' para ejecutar este cuaderno.")
else:
    import ee
    import geemap
    import geemap.foliumap as geemap_folium
    import pandas as pd
    import matplotlib.pyplot as plt

    # Autenticación (solo la primera vez por sesión)
    try:
        ee.Initialize(project='tu-proyecto-gee')
        print("✅ Google Earth Engine autenticado correctamente")
    except Exception:
        ee.Authenticate()
        ee.Initialize(project='tu-proyecto-gee')
        print("✅ Autenticación completada")
```

```python
# ── Celda 2: Mapa interactivo de deforestación con geemap ────────────────────
if not _ES_JUPYTERLITE:
    # Crear mapa centrado en Colombia
    Map = geemap.Map(center=[4.5, -74.0], zoom=6)
    Map.add_basemap('SATELLITE')

    colombia = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017') \
                 .filter(ee.Filter.eq('country_co', 'CO'))

    # Hansen Global Forest Change (2000-2023)
    gfc = ee.Image('UMD/hansen/global_forest_change_2023_v1_11')

    # Pérdida forestal acumulada
    perdida = gfc.select('lossyear').gte(1).selfMask()

    # Ganancia forestal
    ganancia = gfc.select('gain').selfMask()

    # Cobertura forestal año 2000
    cobertura_2000 = gfc.select('treecover2000').updateMask(
        gfc.select('treecover2000').gte(30)
    )

    Map.addLayer(cobertura_2000.clip(colombia),
                 {'min': 30, 'max': 100, 'palette': ['lightgreen', 'darkgreen']},
                 'Cobertura forestal 2000')
    Map.addLayer(perdida.clip(colombia),
                 {'palette': ['red']}, 'Pérdida forestal 2001-2023')
    Map.addLayer(ganancia.clip(colombia),
                 {'palette': ['blue']}, 'Ganancia forestal')
    Map.addLayer(colombia, {'color': 'black', 'fillColor': '00000000'}, 'Colombia')

    Map.add_legend(
        title='Cobertura Forestal',
        legend_dict={
            'Cobertura 2000 (≥30%)': '006400',
            'Pérdida 2001-2023':     'FF0000',
            'Ganancia':              '0000FF',
        }
    )
    Map
```

```python
# ── Celda 3: Estadísticas de pérdida forestal por año ────────────────────────
if not _ES_JUPYTERLITE:
    # Calcular área perdida por año (en km²)
    registros = []
    for anio in range(1, 24):  # años 1-23 corresponden a 2001-2023
        mascara = gfc.select('lossyear').eq(anio)
        area = mascara.multiply(ee.Image.pixelArea()).divide(1e6) \
                      .reduceRegion(
                          reducer=ee.Reducer.sum(),
                          geometry=colombia.geometry(),
                          scale=30,
                          maxPixels=1e11
                      )
        registros.append({
            'año': 2000 + anio,
            'perdida_km2': area.getInfo().get('lossyear', 0)
        })

    df_perdida = pd.DataFrame(registros)

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.bar(df_perdida['año'], df_perdida['perdida_km2'],
           color='#c0392b', alpha=0.85, edgecolor='white')
    ax.set_title('Pérdida forestal anual en Colombia (2001-2023)\nFuente: Hansen/UMD/GLAD',
                 fontsize=12, fontweight='bold')
    ax.set_ylabel('Área perdida (km²)')
    ax.set_xlabel('Año')
    plt.tight_layout()
    plt.show()

    print(f"Pérdida total 2001-2023: {df_perdida['perdida_km2'].sum():,.0f} km²")
    print(f"Año con mayor pérdida:   {df_perdida.loc[df_perdida['perdida_km2'].idxmax(), 'año']}")
```

```python
# ── Celda 4: Análisis de sequía con el índice PDSI (Palmer) ──────────────────
if not _ES_JUPYTERLITE:
    # TERRACLIMATE — índice de sequía de Palmer (PDSI)
    pdsi = ee.ImageCollection('IDAHO_EPSCOR/TERRACLIMATE') \
             .filterDate('2015-01-01', '2024-12-31') \
             .filterBounds(colombia) \
             .select('pdsi') \
             .map(lambda img: img.multiply(0.01).copyProperties(img, ['system:time_start']))

    # Estadística mensual para Colombia
    def stats_mensuales(img):
        stats = img.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=colombia.geometry(),
            scale=4638,
            maxPixels=1e9
        )
        return ee.Feature(None, {
            'fecha': img.date().format('YYYY-MM'),
            'pdsi': stats.get('pdsi')
        })

    tabla_pdsi = pdsi.map(stats_mensuales)
    df_pdsi    = geemap.ee_to_df(tabla_pdsi)[['fecha', 'pdsi']].dropna()
    df_pdsi['fecha'] = pd.to_datetime(df_pdsi['fecha'])
    df_pdsi = df_pdsi.sort_values('fecha')

    fig, ax = plt.subplots(figsize=(14, 4))
    colores = ['#c0392b' if v < 0 else '#2980b9' for v in df_pdsi['pdsi']]
    ax.bar(df_pdsi['fecha'], df_pdsi['pdsi'], color=colores, alpha=0.8, width=20)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axhline(-2, color='orange', linewidth=1, linestyle='--', label='Sequía moderada (PDSI < -2)')
    ax.axhline(-4, color='red',    linewidth=1, linestyle='--', label='Sequía severa (PDSI < -4)')
    ax.set_title('Índice de Sequía de Palmer (PDSI) — Colombia 2015-2024\nFuente: TERRACLIMATE',
                 fontsize=12, fontweight='bold')
    ax.set_ylabel('PDSI')
    ax.legend(fontsize=9)
    plt.tight_layout()
    plt.show()
```

---

## Modo 3 — Mapas GEE Embebidos (sin cuenta requerida)

Los mapas publicados como **Earth Engine Apps** se pueden embeber directamente en cualquier página de la plataforma usando un bloque HTML con `<iframe>`. Esta opción no requiere que el usuario tenga cuenta de GEE.

### Cómo publicar y embeber un mapa GEE

**Paso 1** — En el Code Editor, crea tu mapa y haz clic en **"Apps" → "New App"**

**Paso 2** — Configura la app como pública y copia la URL generada
(ejemplo: `https://ee-miusuario.projects.earthengine.app/view/inundaciones-colombia`)

**Paso 3** — En cualquier página `.md` de la plataforma, usa el bloque HTML:

````markdown
```{raw} html
<div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; border-radius:8px; box-shadow: 0 2px 12px rgba(0,0,0,0.15);">
  <iframe
    src="https://ee-miusuario.projects.earthengine.app/view/inundaciones-colombia"
    style="position:absolute; top:0; left:0; width:100%; height:100%; border:none;"
    allowfullscreen>
  </iframe>
</div>
```
````

### Ejemplo de mapa embebido — FIRMS (Incendios activos NASA)

El siguiente mapa usa el **Global Surface Water Explorer** del JRC (Joint Research Centre), publicado como app pública por Google:

```{raw} html
<div style="position:relative; padding-bottom:60%; height:0; overflow:hidden;
     border-radius:10px; box-shadow: 0 2px 16px rgba(0,0,0,0.18); margin: 1.5em 0;">
  <iframe
    src="https://global-surface-water.appspot.com/map"
    style="position:absolute; top:0; left:0; width:100%; height:100%; border:none;"
    allowfullscreen
    loading="lazy"
    title="JRC Global Surface Water — Agua superficial global">
  </iframe>
</div>
```

*Mapa: JRC Global Surface Water Explorer — muestra la extensión y estacionalidad del agua superficial global. Útil para análisis de cuerpos de agua, humedales y zonas inundables en Colombia.*

---

## Comparativo de los Tres Modos

| Característica | Modo 1 (JS) | Modo 2 (Python/Binder) | Modo 3 (Embebido) |
|---|---|---|---|
| **Requiere cuenta GEE** | Sí | Sí | No |
| **Requiere instalación** | No | No (Binder) | No |
| **Lenguaje** | JavaScript | Python | N/A |
| **Reproducible en plataforma** | Enlace externo | Sí (Binder) | Sí (iframe) |
| **Ideal para** | Prototipado rápido | Análisis científico | Divulgación pública |
| **Acceso a todos los datos GEE** | Sí | Sí | Depende de la app |
| **Exportar resultados** | Drive/Cloud | Drive/local | No |

---

## Datasets GEE Relevantes para Colombia

::::{tab-set}

:::{tab-item} Amenaza Sísmica y Geológica
| Dataset | ID en GEE | Uso |
|---|---|---|
| USGS Landslide Hazard | `USGS/ScienceBase/...` | Susceptibilidad a deslizamientos |
| ALOS DEM 30m | `JAXA/ALOS/AW3D30/V3_2` | Pendientes, cuencas, morfología |
| Global Lithological Map | `CSP/ERGo/1_0/Global/lithology` | Tipo de material geológico |
| OpenLandMap Soil Texture | `OpenLandMap/SOL/SOL_TEXTURE-CLASS_USDA-TT_M/v02` | Textura de suelo |
:::

:::{tab-item} Amenazas Hidrometeorológicas
| Dataset | ID en GEE | Uso |
|---|---|---|
| CHIRPS Daily Precip | `UCSB-CHG/CHIRPS/DAILY` | Lluvias diarias alta resolución |
| PERSIANN-CDR | `NOAA/PERSIANN-CDR` | Precipitación satelital histórica |
| ERA5 Daily Aggregates | `ECMWF/ERA5/DAILY` | Reanálisis clima (temp, viento, precip) |
| JRC Global Surface Water | `JRC/GSW1_4/GlobalSurfaceWater` | Agua superficial histórica |
| GFMS Flood Severity | `GLOBAL_FLOOD_DB/MODIS_EVENTS/V1` | Base de datos global de inundaciones |
:::

:::{tab-item} Cobertura y Vegetación
| Dataset | ID en GEE | Uso |
|---|---|---|
| Hansen Forest Change | `UMD/hansen/global_forest_change_2023_v1_11` | Deforestación 2000-2023 |
| MODIS Land Cover | `MODIS/061/MCD12Q1` | Uso del suelo anual |
| Sentinel-2 SR | `COPERNICUS/S2_SR_HARMONIZED` | Imágenes ópticas de alta res. |
| VIIRS FIRMS | `FIRMS` | Incendios activos en tiempo real |
| NDVI MODIS | `MODIS/061/MOD13A3` | Vegetación mensual |
:::

:::{tab-item} Océanos y Costas
| Dataset | ID en GEE | Uso |
|---|---|---|
| NOAA CoRTAD SST | `NOAA/CDR/OISST/V2_1` | Temperatura superficial del mar |
| Copernicus DEM GLO-30 | `COPERNICUS/DEM/GLO30` | Elevación zonas costeras |
| AWEI (Water Index) | Calculado con Landsat | Cuerpos de agua costeros |
| GEBCO Bathymetry | `projects/sat-io/open-datasets/gebco-x` | Batimetría costera |
:::

::::

---

## Recursos para Empezar con GEE

::::{grid} 1 2 2 3
:gutter: 3

:::{card}
:link: https://developers.google.com/earth-engine/guides
:class-header: bg-warning
📚 **Documentación GEE**
^^^
Guía oficial de Google Earth Engine con tutoriales, referencia API JavaScript y Python.
:::

:::{card}
:link: https://geemap.org
:class-header: bg-primary text-white
🐍 **geemap.org**
^^^
Documentación de la librería Python geemap con ejemplos, tutoriales y cuadernos Jupyter.
:::

:::{card}
:link: https://developers.google.com/earth-engine/datasets
:class-header: bg-success text-white
🛰️ **Catálogo de datos**
^^^
Más de 900 datasets públicos disponibles en GEE: imágenes satelitales, clima, topografía y más.
:::

::::

---

:::{admonition} Contribuye con tu análisis GEE
:class: tip
¿Tienes un análisis GEE aplicado a la gestión del riesgo en Colombia? Compártelo a través de la [Convocatoria de Cuadernos Reproducibles UNGRD](../convocatoria/convocatoria-cuadernos.md). Aceptamos tanto cuadernos Python con `geemap` como scripts JavaScript documentados.
:::
