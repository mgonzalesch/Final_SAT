# Final_SAT
TP Final

Para el trabajo se planteó analizar una base de datos para ver qué tipo de posición y área de golpe es más conduciva a un Knockout/Technical Knockout, como respaldo se utilizarán las decisiones como la contraposición.
Como las métricas principales para ganar en una decisión son principalmente los golpes significativos, por lo tanto se las tomó en cuenta para el análisis. En cambio las misiones pueden ser conseguidas sin importar cualquier aspecto del stricking, por lo tanto no fueron consideradas.
Se planteó analizar las eficiencias de los golpes totales y los porcentajes de las 3 posiciones(Ground, Clinch y Distance), y las 3 áreas(Head, Body y Legs). 
Como en nuestros datos crudos se obtienen las estadísticas de cada pelea, lo que se realizó fue una sumatoria de todos los rounds de las categorías que corresponden a los golpes significativos de cada área y posición(en excepción de los golpes a distancia ya que todos son considerados significativos) del ganador de la pelea.



Analysis

1. Primeramente analizamos el nivel de eficiencia de los golpes totales contra la cantidad de golpes totales, diferenciando entre los peleas que finalizaron en knockout("KO/TKO") contra cuales terminaron en decisión("DEC"). Podemos observar que las que terminaron vía el knockout tienen mayores niveles de eficiencia, mientras que la cantidad de golpes totales no afecta significativamente.

2. Se analiza el porcentaje de golpes en una posición sobre el total de golpes realizados. Se utilizaron histogramas basados en cada una de las posiciones. Como se puede observar en el gráfico de Distance favorece a el knockout especialmente entre el 60% y 90% provienen de esa posición. Lo mismo ocurre con el Clinch y Ground entre un 5% y 25%> Por lo tanto podemos concluir que si realiza una mayor de golpes a la distancia es más probable que ocurra un knockout, esto puede ser explicado ya que el Clinch lleva generalmente a un derribo para terminar en el piso y estando en el piso, los golpes tienen menos poder y las sumisiones son la opción más efectiva.

3. Analizando del mismo modo que las posiciones lo hacemos con las áreas de los golpes y podemos observar la misma tendencia, donde los golpes a la cabeza son fuertemente favorecidos, con respecto a los cuales son al cuerpo, los cuales también son favorecidos contra los golpes a las piernas. Esto también puede ser explicado debido a la naturaleza contusiva de los knockouts.

4. Se analizó el PER(golpes cada 15 minutos), se puede observar que hay una gran diferencia entre los KO y DEC, siendo que la mayoría de los KO 's se encuentran en menos de 150 golpes. 

Recomendaciones Final: Se recomienda a base del punto
1. No concentrarse en tener un output de golpes muy alto, pero mantener la precisión de los mismos.
2. Enfocar mayoritariamente en golpes a distancia, y tener una cantidad baja de golpes desde el clinch y piso. Recomendando un split de 70/15/15.
3. Enfocar fuertemente en los golpes a la cabeza y una baja cantidad en los golpes al cuerpo y piernas. Recomendando un split de 80/10/10
3. Debido a que el PER óptimo es menor a 150, se recomienda tener una cantidad de 30 a 40 golpes por round.

Conclusiones:
El análisis permite establecer una mayoría de las presunciones iniciales, ya que de puede ver una relación entre los tipos y áreas de golpes con la cantidad de KO's, pero debido a la naturaleza del deporte y diferencia entre los luchadores no se puede establecer una diferencia muy significativa entre que conduce a un KO o decisión. 
Los próximos pasos serían tener un análisis más profundo de las mismas estadísticas pero en vez de peleas completas, ver cada round en particular, así estableciendo una mayor correlatividad entre los rounds decisivos.


