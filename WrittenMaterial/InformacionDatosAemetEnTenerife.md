# Información acerca de los datos meteorológicos que ofrece AEMET

La Agencia Estatal de Meteorología (AEMET), a través de [AEMET OpenData](https://opendata.aemet.es/centrodedescargas/inicio), provee al público de una _API REST_ para descargar gratuitamente datos meteorológicos y climatológicos y otros productos como gráficas elaborados por AEMET. Entre estos datos se pueden encontrar observaciones meteorológicas diarias de potencial interés para su uso en el presente trabajo como horas de sol, temperatura media, velocidad media del viento, etc.

## Localización de las estaciones

| Estación              | Identificador | Latitud        | Longitud       | Altitud (m) |
| --------------------- | ------------- | -------------- | -------------- | ----------- |
| STA. CRUZ DE TENERIFE | C449C         | 28º 27' 48'' N | 16º 15' 19'' W | 35          |
| AEROPUERTO NORTE      | C447A         | 28º 28' 39'' N | 16º 19' 46'' W | 632         |
| AEROPUERTO SUR        | C429I         | 28º 02' 51'' N | 16º 33' 39'' W | 64          |
| IZAÑA                 | C430E         | 28º 18' 32'' N | 16º 29' 58'' W | 2371        |
| GÜÍMAR                | C439J         | 28º 19' 06'' N | 16º 22' 56'' W | 115         |
| PUERTO DE LA CRUZ     | C459Z         | 28º 25' 05'' N | 16º 32' 53'' W | 25          |

Fuentes:

- [https://datosclima.es/Aemet2013/LocalizacionEstaciones.php](https://datosclima.es/Aemet2013/LocalizacionEstaciones.php)
- [https://opendata.aemet.es/centrodedescargas/productosAEMET](https://opendata.aemet.es/centrodedescargas/productosAEMET) (Apartado "Valores Climatológicos")

## Metadatos

A continuación se muestra la descripción sobre los datos meteorológicos diarios que provee AEMET

```json
{
  "unidad_generadora": "Servicio del Banco de Datos Nacional de Climatología",
  "periodicidad": "1 vez al día, con un retardo de 4 días",
  "descripcion": "Climatologías diarías",
  "formato": "application/json",
  "copyright": "© AEMET. Autorizado el uso de la información y su reproducción citando a AEMET como autora de la misma.",
  "notaLegal": "http://www.aemet.es/es/nota_legal",
  "campos": [
    {
      "id": "fecha",
      "descripcion": "fecha del dia (AAAA-MM-DD)",
      "tipo_datos": "string",
      "requerido": true
    },
    {
      "id": "indicativo",
      "descripcion": "indicativo climatológico",
      "tipo_datos": "string",
      "requerido": true
    },
    {
      "id": "nombre",
      "descripcion": "nombre (ubicación) de la estación",
      "tipo_datos": "string",
      "requerido": true
    },
    {
      "id": "provincia",
      "descripcion": "provincia de la estación",
      "tipo_datos": "string",
      "requerido": true
    },
    {
      "id": "altitud",
      "descripcion": "altitud de la estación en m sobre el nivel del mar",
      "tipo_datos": "float",
      "unidad": "m",
      "requerido": true
    },
    {
      "id": "tmed",
      "descripcion": "Temperatura media diaria",
      "tipo_datos": "float",
      "unidad": "grados celsius",
      "requerido": false
    },
    {
      "id": "prec",
      "descripcion": "Precipitación diaria de 07 a 07",
      "tipo_datos": "float",
      "unidad": "mm",
      "requerido": false
    },
    {
      "id": "tmin",
      "descripcion": "Temperatura Mínima del día",
      "tipo_datos": "float",
      "unidad": "ºC",
      "requerido": false
    },
    {
      "id": "horatmin",
      "descripcion": "Hora y minuto de la temperatura mínima",
      "tipo_datos": "string",
      "unidad": "UTC",
      "requerido": false
    },
    {
      "id": "tmax",
      "descripcion": "Temperatura Máxima del día",
      "tipo_datos": "float",
      "unidad": "ºC",
      "requerido": false
    },
    {
      "id": "horatmax",
      "descripcion": "Hora y minuto de la temperatura máxima",
      "tipo_datos": "string",
      "unidad": "UTC",
      "requerido": false
    },
    {
      "id": "dir",
      "descripcion": "Dirección de la racha máxima",
      "tipo_datos": "float",
      "unidad": "decenas de grado",
      "requerido": false
    },
    {
      "id": "velmedia",
      "descripcion": "Velocidad media del viento",
      "tipo_datos": "float",
      "unidad": "m/s",
      "requerido": false
    },
    {
      "id": "racha",
      "descripcion": "Racha máxima del viento",
      "tipo_datos": "float",
      "unidad": "m/s",
      "requerido": false
    },
    {
      "id": "horaracha",
      "descripcion": "Hora y minuto de la racha máxima",
      "tipo_datos": "float",
      "unidad": "UTC",
      "requerido": false
    },
    {
      "id": "sol",
      "descripcion": "Insolación",
      "tipo_datos": "float",
      "unidad": "horas",
      "requerido": false
    },
    {
      "id": "presmax",
      "descripcion": "Presión máxima al nivel de referencia de la estación",
      "tipo_datos": "float",
      "unidad": "hPa",
      "requerido": false
    },
    {
      "id": "horapresmax",
      "descripcion": "Hora de la presión máxima (redondeada a la hora entera más próxima)",
      "tipo_datos": "float",
      "unidad": "hora entera",
      "requerido": false
    },
    {
      "id": "presmin",
      "descripcion": "Presión mínima al nivel de referencia de la estación",
      "tipo_datos": "float",
      "unidad": "hPa",
      "requerido": false
    },
    {
      "id": "horapresmin",
      "descripcion": "Hora de la presión mínima (redondeada a la hora entera más próxima)",
      "tipo_datos": "float",
      "unidad": "hora entera",
      "requerido": false
    }
  ]
}
```

## Fuentes adicionales

Meteorología y climatología. ¿En qué se diferencian?. Emilio Rey. Última actualización: 18 de febrero de 2017. Recogido el día 13 de diciembre de 2018 de [https://www.solucionesintegralesendesa.com/blog/meteorologia/meteorologia-y-climatologia/](https://www.solucionesintegralesendesa.com/blog/meteorologia/meteorologia-y-climatologia/)
