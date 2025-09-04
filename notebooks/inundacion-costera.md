# Evaluación de Riesgos por Inundación Costera

## Introducción

Este cuaderno presenta una metodología completa para la evaluación de riesgos por inundación costera, enfocándose en los procesos físicos y las herramientas computacionales necesarias para cuantificar estos riesgos a escalas regionales y globales.

## Contexto

Las inundaciones costeras representan una de las amenazas naturales más significativas para las comunidades ubicadas en zonas litorales. Estas pueden ser causadas por:

- **Mareas extremas**: Variaciones naturales en el nivel del mar
- **Marejadas ciclónicas**: Sobreelevación del nivel del mar causada por tormentas
- **Aumento del nivel del mar**: Efectos del cambio climático a largo plazo
- **Oleaje extremo**: Ondas generadas por viento que pueden sobrepasar las defensas costeras

## Metodología de Evaluación de Riesgos

La evaluación de riesgos por inundación costera sigue una aproximación sistemática que integra:

### 1. Análisis de Amenaza

La amenaza se caracteriza mediante:
- Niveles de agua extremos históricos y proyectados
- Períodos de retorno asociados
- Escenarios de aumento del nivel del mar
- Análisis de frecuencia de eventos extremos

### 2. Análisis de Vulnerabilidad

Se evalúan los elementos expuestos:
- Población en zonas de riesgo
- Infraestructura crítica
- Actividades económicas
- Ecosistemas costeros

### 3. Cálculo del Riesgo

El riesgo se cuantifica como:

```
Riesgo = Amenaza × Vulnerabilidad × Exposición
```

## Conjuntos de Datos Utilizados

### Modelos Globales de Mareas y Marejadas (GTSMv3.0)

- Resolución espacial: ~25 km
- Cobertura temporal: 1979-2014
- Variables: Nivel total del agua, mareas, marejadas
- Fuente: Instituto Deltares

### Herramienta de Proyección del Nivel del Mar (NASA)

- Proyecciones hasta 2150
- Escenarios de emisiones múltiples
- Resolución: 0.25° × 0.25°
- Incluye componentes regionales del cambio del nivel del mar

### Mapas Globales de Inundación (Microsoft Planetary Computer)

- Mapas de profundidad y extensión de inundación
- Períodos de retorno: 2, 5, 10, 25, 50, 100, 250, 500, 1000 años
- Resolución: ~90m (3 arcosegundos)
- Cobertura global

### Datos de Monitoreo Terrestre (Copernicus)

- Uso del suelo y cobertura terrestre
- Impermeabilización del suelo
- Densidad de población
- Infraestructura urbana

## Flujo de Trabajo de Análisis

### Paso 1: Exploración de Niveles de Agua Extremos

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr

# Cargar datos de GTSM
def load_water_levels(lat, lon, scenario):
    """
    Carga series temporales de niveles de agua para una ubicación específica
    """
    # Código para cargar y procesar datos de GTSM
    pass

# Análisis estadístico de extremos
def extreme_value_analysis(data):
    """
    Realiza análisis de valores extremos usando distribución GEV
    """
    # Ajuste de distribución de valores extremos
    pass
```

### Paso 2: Evaluación de Amenazas usando Mapas Globales

```python
# Procesamiento de mapas de inundación
def process_flood_maps(region_bounds, return_periods):
    """
    Procesa mapas de inundación para la región de interés
    """
    flood_depths = {}
    for rp in return_periods:
        # Cargar mapa de profundidad de inundación
        depth_map = load_flood_depth_map(rp)
        flood_depths[rp] = clip_to_region(depth_map, region_bounds)
    return flood_depths
```

### Paso 3: Evaluación de Riesgos y Daños Potenciales

```python
# Cálculo de daños económicos
def calculate_flood_damages(flood_depths, exposure_data, damage_curves):
    """
    Calcula daños económicos por inundación
    """
    damages = {}
    for rp, depth in flood_depths.items():
        # Aplicar curvas de daño por tipo de infraestructura
        damage = apply_damage_curves(depth, exposure_data, damage_curves)
        damages[rp] = damage
    return damages
```

## Consideraciones Importantes

### Limitaciones de los Datos Globales

- Los conjuntos de datos globales no consideran defensas costeras locales
- La resolución puede ser insuficiente para análisis detallados
- Se recomienda complementar con modelado local de inundaciones

### Incertidumbres

- Variabilidad en las proyecciones climáticas
- Limitaciones en la representación de procesos físicos
- Incertidumbres en los datos de exposición

### Recomendaciones

1. **Validación local**: Comparar resultados con observaciones locales
2. **Análisis de sensibilidad**: Evaluar el impacto de diferentes parámetros
3. **Actualización continua**: Incorporar nuevos datos y mejoras metodológicas

## Resultados Esperados

El flujo de trabajo produce:

1. **Gráficos de series temporales**: Niveles de agua históricos y proyectados
2. **Mapas de profundidad de inundación**: Por escenario y período de retorno
3. **Mapas de daños económicos**: Distribución espacial de pérdidas potenciales
4. **Análisis de riesgo**: Probabilidades anuales de excedencia

## Aplicaciones

Esta metodología puede aplicarse para:

- Planificación del uso del suelo costero
- Diseño de defensas costeras
- Evaluación de seguros por inundación
- Estrategias de adaptación al cambio climático
- Sistemas de alerta temprana

## Referencias

- Aleksandrova, N., & Buskop, T. (2023). Coastal Flood Risk Assessment Workflow. Deltares.
- Global Tide and Surge Model (GTSMv3.0). Deltares Institute.
- NASA Sea Level Projection Tool. NASA Goddard Space Flight Center.
- Microsoft Planetary Computer Global Flood Maps.
- Copernicus Land Monitoring Service.

## Autores

**Instituto de Investigación Aplicada Deltares**
- Natalia Aleksandrova
- Ted Buskop

---

*Adaptado del workflow original de CLIMAAX para evaluación de riesgos por inundación costera*