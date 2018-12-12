# Contaminación atmosférica

La presencia de materia intrusa en la atmósfera puede resultar dañina para los seres vivos. Por ejemplo, cuando una persona inhala partículas de monóxido de carbono (CO), al llegar a la sangre se unen a la hemoglobina y, como esta unión es mucho más fuerte que con el oxígeno, se disminuye la capacidad del cuerpo de transportar oxígeno [1]. En caso de estar expuesto a una fuente continua puede producir la muerte en minutos. Otro ejemplo son las partículas en suspensión que pueden perforar el sistema respiratorio y cardiovascular siendo responsable de 7 millones de muertes al año según la Organización Mundial de la Salud (OMS) [2].

También hay materia que al ser introducida en la atmósfera no es dañina para los seres vivos pero altera el entorno en que viven pudiendo resultar dañina indirectamente. Por ejemplo, la emisión de gases de efecto invernadero como el dióxido de carbono (CO<sub>2</sub>). Los gases de efecto invernadero contribuyen a que no haya un cambio brusco de temperatura entre el día y la noche. Esto es gracias a que estos gases pueden absorber y luego emitir ciertas radiaciones de calor, de manera que parte del calor emitido por la Tierra como consecuencia de la radiación solar se queda siendo absorbido y reemitido por estos gases [3]. Sin embargo, un exceso de estos gases en la atmósfera provocaría que menos calor salga al espacio y, por tanto, que suba la temperatura media del planeta pudiendo afectar a la vida si ocurre de manera brusca (considerando brusco un período de tiempo que no dé tiempo a las especies a adaptarse).

La materia contaminante puede ser formada directamente en la atmósfera como producto de reacciones entre contaminantes ya presentes como es el caso del ozono troposférico. Puede ser emitida a la atmósfera como resultado de procesos naturales como la erupción de un volcán o un incendio forestal. O pueden ser producidos por actividades humanas como la quema de combustible [4]. De entre estas fuentes de contaminantes, las de origen humano son las que tienen un mayor impacto debido a su frecuente y extendido uso. Por lo que, con el objetivo de reducir el negativo impacto en la salud pública, se han desarrollado estándares de calidad del aire (nivel de contaminación): un tipo de estándares se usan para regular los niveles de concentración de contamintantes en la atmósfera como los [_National Ambient Air Quality Standards_](https://www.epa.gov/criteria-air-pollutants) de Estados Unidos. Y se puede distinguir otro tipo de estándares que se usan para informar a la población sobre la calidad del aire como el [_Air Quality Health Index_](https://www.canada.ca/en/environment-climate-change/services/air-quality-health-index/overview.html) de Canadá.

Aunque las legislaciones difieran entre países, la contaminación de la atmósfera es un peligro para todos porque, una vez en la atmósfera, los contaminantes pueden viajar por acción del viento a otras regiones. Por ello, la OMS provee unas directrices generales acerca de los límites de concentración de contamintantes clave en el riesgo de la salud pública [5]. Actualmente los contaminantes propuestos por la OMS son los siguientes:

- **Partículas en suspensión**: son una mezcla de pequeñas partículas en estado sólido o líquido como hollín, polvo o agua que se encuentran suspendidas en el aire. En concreto se tienen en cuenta como contaminantes las partículas de 10µm o menos (PM<sub>10</sub>) que suponen un peligro al poder penetrar los pulmones al ser inhaladas y las partículas de 2.5µm o menos (PM<sub>2.5</sub>) que pueden incluso entrar en el sistema sanguíneo. Según la OMS existe una estrecha relación entre la exposición a estas partículas y el aumento de la mortalidad y morbilidad [5].
- **Ozono troposférico (O<sub>3</sub>)**: a partir de reacciones involucrando a la luz solar y contaminantes ya presentes en el aire (óxidos de nitrógeno e hidrocarburos) se forma ozono troposférico. El ozono junto a los otros contaminantes en la atmósfera forman el esmog fotoquímico [6] cuya exposición puede causar problemas respiratorios, provocar o empeorar el asma, etc [7].
- **Dióxido de nitrógeno (NO<sub>2</sub>)**: es un gas tóxico que, al ser inhalado, irrita las vias respiratorias y, en la atmósfera, supone una de las causas de la formación de ozono troposférico y de la formación de la lluvia ácida junto al dióxido de azufre [8][9].
- **Dióxido de azufre (SO<sub>2</sub>)**: al igual que el NO<sub>2</sub> es un gas que al ser inhalado irrita las vias respiratorias dificultando la respiración y supone una de las principales causas de la formación de la lluvia ácida [9][10].

Para asegurarse que las concentraciones de los contaminantes en la atmósfera no superan los límites legales se usan datos de sensores que miden estas concentraciones para llevar a cabo procesos de control y de mitigación si fuera necesario. Por tanto, **poder predecir las concentraciones de los contaminantes supondría poder reaccionar antes de que la calidad del aire sea peligrosa**.

El presente trabajo tiene como objetivo la predicción del nivel de concentración de los anteriores contaminantes en Tenerife en un período de 24 horas. Para ello se va a hacer uso de datos históricos de concentración de contaminación además de datos meteorológicos pues, como se ha mencionado previamente, variables como la fuerza y dirección del viento o luz solar tienen un impacto directo en la dispersión y formación de contaminantes.

La naturaleza de los datos cumple con las características principales para considerarlos _Big Data_:

- Gran volumen
- Frecuencia de llegada relativamente alta (se añaden datos al menos una vez al día)
- Estructura variable debido al uso de distintas fuentes de datos con distintos formatos (TODO: escribir sobre los datos de AEMET si definitivamente se hace el trabajo sobre Tenerife y posiblemente datos relativos al calendario para saber los días de fiesta)

## Referencias

[1] What is the chemical reaction that occurs in the body when carbon monoxide is inhaled? (Sep 24, 2008). Retrieved December 3, 2018 from [http://scienceline.ucsb.edu/getkey.php?key=1856](http://scienceline.ucsb.edu/getkey.php?key=1856)

[2] Nueve de cada diez personas de todo el mundo respiran aire contaminado. Organización Mundial de la Salud. Última actualización el día 2 de mayo de 2018, recogido el día 5 de diciembre de 2018 de [http://www.who.int/es/news-room/detail/02-05-2018-9-out-of-10-people-worldwide-breathe-polluted-air-but-more-countries-are-taking-action](http://www.who.int/es/news-room/detail/02-05-2018-9-out-of-10-people-worldwide-breathe-polluted-air-but-more-countries-are-taking-action)

[3] Julia Layton & Ed Grabianowski "What is the greenhouse effect?" 26 May 2005. HowStuffWorks.com. <https://science.howstuffworks.com/environmental/green-science/question746.htm> 4 December 2018

[4] Ambient air pollution: Pollutants. World Health Organization. Retrieved December 4, 2018 from [http://www.who.int/airpollution/ambient/pollutants/en/](http://www.who.int/airpollution/ambient/pollutants/en/)

[5] Calidad del aire y salud. Organización Mundial de la Salud. Última actualización el 2 de mayo de 2018. Recogido el 6 de diciembre de 2018 de [https://www.who.int/es/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health](<https://www.who.int/es/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health>)

[6] Photochemical smog reactions. California State University, Northridge. Retrieved December 8, 2018 from [https://www.csun.edu/~vchsc006/356b/reactions.html](https://www.csun.edu/~vchsc006/356b/reactions.html)

[7] Ground-level Ozone Pollution. United States Environmental Protection Agency
. Retrieved December 8, 2018 from [https://www.epa.gov/ground-level-ozone-pollution/health-effects-ozone-pollution](https://www.epa.gov/ground-level-ozone-pollution/health-effects-ozone-pollution)

[8] Nitrogen Dioxide (NO2) Pollution. United States Environmental Protection Agency
. Retrieved December 8, 2018 from [https://www.epa.gov/no2-pollution/basic-information-about-no2](https://www.epa.gov/no2-pollution/basic-information-about-no2)

[9] What is Acid Rain?. United States Environmental Protection Agency
. Retrieved December 8, 2018 from [https://www.epa.gov/acidrain/what-acid-rain](https://www.epa.gov/acidrain/what-acid-rain)

[10] Sulfur Dioxide (SO2) Pollution. United States Environmental Protection Agency
. Retrieved December 8, 2018 from [https://www.epa.gov/so2-pollution/sulfur-dioxide-basics](https://www.epa.gov/so2-pollution/sulfur-dioxide-basics)
