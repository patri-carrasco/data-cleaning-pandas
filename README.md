# Introducción

En este proyecto analizo la base de datos de [Shark attacks](https://www.kaggle.com/teajay/global-shark-attacks/version/1) 
obtenido de la página web de Kaggle.

## Hipótises

Quiero saber si hay mas muertos por ataques de tiburones en USA o en Asutralia.

Para ello separo el data set en dos :
  1.- USA
  2.- Australia.

Para cada nuevo data set:

  1º Analizo si la columna de Year, los años esta bien, ya que he detectado varios error.

  2º Le aplico una función llamada date_year que contiene un regex para comparar los datos de la columna Date con la de Year
  3º Genero una nueva columna Year con los datos devueltos por la funcion data_year.

He encotrado valores que han dado error, como son pocos los elimino del data set correspondiente 

Creo unos nuevos datas con solo los muertos por ataques de tiburones.

Hago las gŕaficas donde se de muesta que en Australia hay más muerto que en Usa.

## Links & Resources
(https://www.kaggle.com/teajay/global-shark-attacks/version/1)

