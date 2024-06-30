# Ya_Ganaste_PT
Este proyecto está diseñado para realizar la extracción, limpieza y conciliación de datos transaccionales utilizando Python. El proyecto consta de dos paquetes principales: scraping y cleaning, así como dos archivos ejecutables: main y daily_conciliation.
## Estructura del Proyecto

Aquí tienes el fragmento de la estructura de carpetas en formato Markdown:

markdown
Copiar código
.
├── scraping/
│ ├── init.py
│ └── download.py
├── cleaning/
│ ├── init.py
│ └── transform.py
├── main.py
├── daily_conciliation.py
├── BAT FILE/
│ ├── task.txt
│ ├── task.bat
│ └── task.xml
├── CHROME/
│ └── chromedriver.exe
├── FILES/
├── PRESENTACION/
│ ├── presentacion.pbix
│ └── presentacion.pdf
└── VIDEO EXTRACCION/
├── video_extraccion_1.mp4
└── video_extraccion_2.mp4


## Paquetes

### scraping

El paquete `scraping` contiene un archivo `download.py` con tres funciones principales:

1.  **driver**: Crea la instancia del navegador utilizando Selenium WebDriver para la extracción web.
2.  **downloads**: Extrae los archivos de interés para la prueba.
3.  **conciliation**: Maneja el hecho de que los nombres de los archivos cambian y realiza la misma función que `downloads`, pero ajustando las URLs de descarga.

Importaciones utilizadas:

    import os
    import time
    import selenium.common.exceptions
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
### cleaning

El paquete `cleaning` sirve para preparar los archivos para el análisis y la visualización. Contiene un archivo `transform.py` con una función `files`:

1.  **files**: Lee los archivos utilizando pandas y aplica las siguientes configuraciones: `encoding=x`, `skiprows=x`, `index_col=x`, `delimiter=x`, `parse_dates=x`. Estas configuraciones no se aplican a todos los archivos, pero son las más utilizadas.

## Archivos Ejecutables

### main.py

Este archivo llama a las funciones `downloads` y `files` para realizar la extracción y limpieza de datos.

### daily_conciliation.py

Este archivo llama a las funciones `conciliation` y `files` para manejar las descargas y la limpieza de datos en caso de cambios en los nombres de los archivos.

## Carpetas

-   **BAT FILE**: Contiene un `.txt`, un `.bat` y un archivo `.xml`. Los dos primeros apuntan a `daily_conciliation` para automatizar su ejecución mediante el Task Scheduler de Windows. El `.xml` es el archivo exportado de esta tarea programada.
-   **CHROME**: Contiene el driver de Chrome que utiliza Selenium.
-   **FILES**: Carpeta donde se almacenan los archivos descargados y procesados.
-   **PRESENTACION**: Contiene un archivo de Power BI (`.pbix`) y una presentación (`.pdf`). Estos archivos muestran los resultados de la conciliación y algunas operaciones adicionales.
-   **VIDEO EXTRACCION**: Contiene dos videos que demuestran el funcionamiento del programa, incluyendo la extracción de datos.

## Instrucciones para Ejecutar el Proyecto

1.  **Instalar Dependencias**: Asegúrate de tener las siguientes librerías instaladas:

    ` pip install pandas selenium`


2.    **Configurar el Driver de Chrome**: Coloca el `chromedriver.exe` en la carpeta `CHROME`.
3.  **Ejecutar el Script Principal**:

   ` python main.py`

4. **Automatización con Task Scheduler**: Importa el archivo `task.xml` en el Task Scheduler de Windows para automatizar la ejecución diaria.
## Videos

Para ver cómo funciona el programa, consulta los videos en la carpeta `VIDEO EXTRACCION`.
