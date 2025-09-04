# Estaciones Hidrometeorológicas

## Introducción

Este cuaderno explora el acceso, exploración y visualización de datos de estaciones hidrometeorológicas del IDEAM (Instituto de Hidrología, Meteorología y Estudios Ambientales) utilizando herramientas de código abierto de Python como Pandas, Cartopy y Folium.

## Objetivos de Aprendizaje

- Acceder al catálogo nacional de estaciones hidrometeorológicas
- Visualizar estaciones en mapas estáticos e interactivos
- Consultar datos históricos de temperatura y precipitación
- Realizar consultas tipo SQL en la API de datos abiertos de Colombia
- Procesar y graficar series de datos en tiempo casi real

## Prerrequisitos

| Concepto | Importancia | Notas |
|----------|-------------|-------|
| Introducción a Pandas | Requerido | Lectura de datos tabulares |
| Datetime | Requerido | Comprensión de marcas de tiempo |
| Cartopy | Requerido | Visualización geoespacial |
| Folium | Útil | Mapas interactivos |

## Importación de Librerías

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import folium
from folium import plugins
import requests
import warnings
warnings.filterwarnings('ignore')

# Configuración de matplotlib para español
plt.rcParams['font.size'] = 12
plt.style.use('seaborn-v0_8')
```

## 1. Catálogo Nacional de Estaciones

### Acceso a Metadatos de Estaciones

El IDEAM mantiene un catálogo público de estaciones hidrometeorológicas a través de la API de datos abiertos de Colombia.

```python
# URL base para la API de datos abiertos de Colombia
base_url = "https://www.datos.gov.co/resource/"

# Endpoint para estaciones hidrometeorológicas
estaciones_endpoint = "sbwg-7ju4.json"

def cargar_catalogo_estaciones():
    """
    Carga el catálogo completo de estaciones hidrometeorológicas
    """
    url = f"{base_url}{estaciones_endpoint}"
    
    try:
        response = requests.get(url, params={'$limit': 10000})
        response.raise_for_status()
        data = response.json()
        
        df = pd.DataFrame(data)
        
        # Conversión de tipos de datos
        if 'latitud' in df.columns:
            df['latitud'] = pd.to_numeric(df['latitud'], errors='coerce')
        if 'longitud' in df.columns:
            df['longitud'] = pd.to_numeric(df['longitud'], errors='coerce')
        if 'altitud' in df.columns:
            df['altitud'] = pd.to_numeric(df['altitud'], errors='coerce')
            
        return df
        
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return None

# Cargar datos
estaciones_df = cargar_catalogo_estaciones()

if estaciones_df is not None:
    print(f"Total de estaciones cargadas: {len(estaciones_df)}")
    print(f"Columnas disponibles: {list(estaciones_df.columns)}")
    print("\nPrimeras 5 estaciones:")
    print(estaciones_df.head())
```

### Análisis del Catálogo

```python
# Estadísticas básicas del catálogo
def analizar_catalogo(df):
    """
    Análisis estadístico del catálogo de estaciones
    """
    print("=== ANÁLISIS DEL CATÁLOGO DE ESTACIONES ===\n")
    
    # Información general
    print(f"Total de estaciones: {len(df)}")
    
    # Distribución por departamento
    if 'departamento' in df.columns:
        print(f"\nEstaciones por departamento:")
        dept_count = df['departamento'].value_counts().head(10)
        print(dept_count)
    
    # Distribución por categoría
    if 'categoria' in df.columns:
        print(f"\nEstaciones por categoría:")
        cat_count = df['categoria'].value_counts()
        print(cat_count)
    
    # Distribución altitudinal
    if 'altitud' in df.columns:
        altitud_stats = df['altitud'].describe()
        print(f"\nDistribución altitudinal:")
        print(altitud_stats)
    
    # Estado operativo
    if 'estado' in df.columns:
        print(f"\nEstado operativo:")
        estado_count = df['estado'].value_counts()
        print(estado_count)

# Ejecutar análisis
if estaciones_df is not None:
    analizar_catalogo(estaciones_df)
```

### Visualización en Mapa Estático

```python
def crear_mapa_estatico(df):
    """
    Crea un mapa estático con la ubicación de las estaciones
    """
    fig = plt.figure(figsize=(12, 10))
    ax = plt.axes(projection=ccrs.PlateCarree())
    
    # Configurar extensión para Colombia
    ax.set_extent([-82, -66, -5, 15], crs=ccrs.PlateCarree())
    
    # Agregar características geográficas
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)
    ax.add_feature(cfeature.RIVERS, linewidth=0.3, alpha=0.7)
    ax.add_feature(cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.OCEAN, color='lightblue', alpha=0.5)
    ax.add_feature(cfeature.LAND, color='lightgray', alpha=0.3)
    
    # Plotear estaciones
    if 'latitud' in df.columns and 'longitud' in df.columns:
        scatter = ax.scatter(df['longitud'], df['latitud'], 
                           c=df['altitud'] if 'altitud' in df.columns else 'red',
                           cmap='viridis', s=8, alpha=0.7,
                           transform=ccrs.PlateCarree())
        
        # Barra de color para altitud
        if 'altitud' in df.columns:
            cbar = plt.colorbar(scatter, ax=ax, shrink=0.8, pad=0.05)
            cbar.set_label('Altitud (m.s.n.m.)', rotation=270, labelpad=15)
    
    # Agregar grillas y etiquetas
    ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
    
    plt.title('Red Nacional de Estaciones Hidrometeorológicas\nIDEAM - Colombia', 
              fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

# Crear mapa
if estaciones_df is not None:
    crear_mapa_estatico(estaciones_df)
```

### Mapa Interactivo con Folium

```python
def crear_mapa_interactivo(df):
    """
    Crea un mapa interactivo con información detallada de las estaciones
    """
    # Centro de Colombia
    centro_lat, centro_lon = 4.5709, -74.2973
    
    # Crear mapa base
    m = folium.Map(
        location=[centro_lat, centro_lon],
        zoom_start=6,
        tiles='OpenStreetMap'
    )
    
    # Agregar capas de tiles adicionales
    folium.TileLayer('Stamen Terrain').add_to(m)
    folium.TileLayer('cartodb positron').add_to(m)
    
    # Crear grupos de marcadores por categoría
    if 'categoria' in df.columns:
        categorias = df['categoria'].unique()
        grupos = {}
        
        for cat in categorias:
            if pd.notna(cat):
                grupos[cat] = folium.FeatureGroup(name=f'Estaciones {cat}')
    
    # Agregar marcadores de estaciones
    for idx, station in df.iterrows():
        if pd.notna(station['latitud']) and pd.notna(station['longitud']):
            
            # Información del popup
            popup_text = f"""
            <b>Código:</b> {station.get('codigo', 'N/A')}<br>
            <b>Nombre:</b> {station.get('nombre', 'N/A')}<br>
            <b>Departamento:</b> {station.get('departamento', 'N/A')}<br>
            <b>Municipio:</b> {station.get('municipio', 'N/A')}<br>
            <b>Categoría:</b> {station.get('categoria', 'N/A')}<br>
            <b>Estado:</b> {station.get('estado', 'N/A')}<br>
            <b>Altitud:</b> {station.get('altitud', 'N/A')} m.s.n.m.<br>
            <b>Latitud:</b> {station['latitud']:.4f}<br>
            <b>Longitud:</b> {station['longitud']:.4f}
            """
            
            # Color según categoría o estado
            color = 'blue'
            if 'estado' in station and pd.notna(station['estado']):
                if 'ACTIVA' in str(station['estado']).upper():
                    color = 'green'
                elif 'SUSPENDIDA' in str(station['estado']).upper():
                    color = 'red'
                else:
                    color = 'orange'
            
            marker = folium.CircleMarker(
                location=[station['latitud'], station['longitud']],
                radius=4,
                popup=folium.Popup(popup_text, max_width=300),
                color='white',
                weight=1,
                fillColor=color,
                fillOpacity=0.8
            )
            
            # Agregar a grupo correspondiente o al mapa principal
            categoria = station.get('categoria')
            if categoria in grupos:
                marker.add_to(grupos[categoria])
            else:
                marker.add_to(m)
    
    # Agregar grupos al mapa
    for grupo in grupos.values():
        grupo.add_to(m)
    
    # Agregar control de capas
    folium.LayerControl().add_to(m)
    
    # Plugin de pantalla completa
    plugins.Fullscreen().add_to(m)
    
    return m

# Crear mapa interactivo
if estaciones_df is not None:
    mapa_interactivo = crear_mapa_interactivo(estaciones_df)
    mapa_interactivo.save('mapa_estaciones_colombia.html')
    print("Mapa interactivo guardado como 'mapa_estaciones_colombia.html'")
```

## 2. Consulta de Datos Históricos

### Datos de Precipitación

```python
# Endpoint para datos de precipitación
precipitacion_endpoint = "s54a-sgyg.json"

def consultar_precipitacion(codigo_estacion=None, fecha_inicio=None, fecha_fin=None, limite=1000):
    """
    Consulta datos históricos de precipitación
    """
    url = f"{base_url}{precipitacion_endpoint}"
    params = {'$limit': limite}
    
    # Filtros opcionales
    if codigo_estacion:
        params['$where'] = f"codigoestacion='{codigo_estacion}'"
    
    if fecha_inicio and fecha_fin:
        where_clause = f"fechaobservacion between '{fecha_inicio}T00:00:00' and '{fecha_fin}T23:59:59'"
        if '$where' in params:
            params['$where'] += f" AND {where_clause}"
        else:
            params['$where'] = where_clause
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        df = pd.DataFrame(data)
        
        if not df.empty:
            # Conversión de tipos
            df['fechaobservacion'] = pd.to_datetime(df['fechaobservacion'])
            df['valorobservado'] = pd.to_numeric(df['valorobservado'], errors='coerce')
            
        return df
        
    except Exception as e:
        print(f"Error al consultar precipitación: {e}")
        return None

# Ejemplo de consulta
ejemplo_precipitacion = consultar_precipitacion(
    codigo_estacion='21205790',  # Estación ejemplo
    fecha_inicio='2020-01-01',
    fecha_fin='2020-12-31'
)

if ejemplo_precipitacion is not None and not ejemplo_precipitacion.empty:
    print(f"Datos de precipitación obtenidos: {len(ejemplo_precipitacion)} registros")
    print(ejemplo_precipitacion.head())
```

### Análisis de Series Temporales

```python
def analizar_serie_precipitacion(df):
    """
    Análisis estadístico de serie de precipitación
    """
    if df is None or df.empty:
        print("No hay datos para analizar")
        return
    
    # Estadísticas básicas
    print("=== ANÁLISIS DE PRECIPITACIÓN ===\n")
    print(f"Período: {df['fechaobservacion'].min()} - {df['fechaobservacion'].max()}")
    print(f"Total de registros: {len(df)}")
    print(f"Precipitación total: {df['valorobservado'].sum():.2f} mm")
    print(f"Precipitación promedio diaria: {df['valorobservado'].mean():.2f} mm")
    print(f"Precipitación máxima diaria: {df['valorobservado'].max():.2f} mm")
    
    # Análisis mensual
    df_monthly = df.set_index('fechaobservacion').resample('M')['valorobservado'].agg(['sum', 'mean', 'count'])
    
    # Gráfico de series temporales
    fig, axes = plt.subplots(2, 1, figsize=(14, 10))
    
    # Serie temporal diaria
    axes[0].plot(df['fechaobservacion'], df['valorobservado'], 'b-', alpha=0.7, linewidth=0.8)
    axes[0].set_title('Serie Temporal de Precipitación Diaria', fontweight='bold')
    axes[0].set_ylabel('Precipitación (mm)')
    axes[0].grid(True, alpha=0.3)
    
    # Serie temporal mensual
    axes[1].bar(df_monthly.index, df_monthly['sum'], alpha=0.7, color='steelblue')
    axes[1].set_title('Precipitación Mensual Acumulada', fontweight='bold')
    axes[1].set_ylabel('Precipitación (mm)')
    axes[1].set_xlabel('Fecha')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# Analizar datos de ejemplo
if ejemplo_precipitacion is not None:
    analizar_serie_precipitacion(ejemplo_precipitacion)
```

## 3. Datos en Tiempo Casi Real

### Consulta de Observaciones Recientes

```python
def consultar_datos_recientes(dias=7):
    """
    Consulta datos meteorológicos recientes (últimos N días)
    """
    fecha_fin = pd.Timestamp.now()
    fecha_inicio = fecha_fin - pd.Timedelta(days=dias)
    
    # Formatear fechas
    inicio_str = fecha_inicio.strftime('%Y-%m-%d')
    fin_str = fecha_fin.strftime('%Y-%m-%d')
    
    # Consultar precipitación reciente
    datos_recientes = consultar_precipitacion(
        fecha_inicio=inicio_str,
        fecha_fin=fin_str,
        limite=5000
    )
    
    return datos_recientes

# Obtener datos recientes
datos_recientes = consultar_datos_recientes(dias=30)

if datos_recientes is not None and not datos_recientes.empty:
    print(f"Datos recientes obtenidos: {len(datos_recientes)} registros")
    
    # Resumen por estación
    resumen_estaciones = datos_recientes.groupby('codigoestacion')['valorobservado'].agg([
        'count', 'sum', 'mean', 'max'
    ]).round(2)
    
    print("\nResumen por estación (últimos 30 días):")
    print(resumen_estaciones.head(10))
```

### Visualización Comparativa

```python
def comparar_estaciones(df, estaciones_seleccionadas):
    """
    Compara precipitación entre múltiples estaciones
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    
    colores = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
    
    for i, codigo in enumerate(estaciones_seleccionadas):
        datos_estacion = df[df['codigoestacion'] == codigo]
        
        if not datos_estacion.empty:
            # Serie temporal
            ax.plot(datos_estacion['fechaobservacion'], 
                   datos_estacion['valorobservado'],
                   color=colores[i % len(colores)],
                   label=f'Estación {codigo}',
                   alpha=0.8,
                   linewidth=1.5)
    
    ax.set_title('Comparación de Precipitación entre Estaciones', fontweight='bold')
    ax.set_ylabel('Precipitación (mm)')
    ax.set_xlabel('Fecha')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Ejemplo de comparación (seleccionar estaciones disponibles)
if datos_recientes is not None and not datos_recientes.empty:
    estaciones_disponibles = datos_recientes['codigoestacion'].unique()[:5]
    comparar_estaciones(datos_recientes, estaciones_disponibles)
```

## Conclusiones

Este cuaderno proporciona una guía completa para:

1. **Acceder programáticamente** al catálogo nacional de estaciones hidrometeorológicas del IDEAM
2. **Visualizar la distribución espacial** de la red de monitoreo usando mapas estáticos e interactivos
3. **Consultar y analizar datos históricos** de precipitación y otras variables meteorológicas
4. **Procesar información en tiempo casi real** para monitoreo continuo
5. **Realizar comparaciones** entre diferentes estaciones y períodos

### Aplicaciones Prácticas

- Análisis de tendencias climáticas regionales
- Estudios de variabilidad pluviométrica
- Planificación de recursos hídricos
- Evaluación de riesgos hidrometeorológicos
- Validación de modelos meteorológicos

### Próximos Pasos

- Integración con datos de modelos numéricos
- Análisis de eventos extremos
- Correlaciones espaciales y temporales
- Desarrollo de índices climáticos
- Implementación de sistemas de alerta temprana

## Referencias

- IDEAM - Instituto de Hidrología, Meteorología y Estudios Ambientales
- Datos Abiertos Colombia - Portal Nacional de Datos Abiertos
- Project Pythia - Geoscience Community Python Tutorials
- Pandas Documentation
- Cartopy Documentation
- Folium Documentation

---

*Adaptado del notebook original de Project Pythia para el análisis de estaciones hidrometeorológicas en Colombia*