# Searchs
 The branch and dimension search strategy belongs to the uninformed and informed search strategies.

 En esta práctica hemos implementado a partir de un código base, dos estrategias de búsqueda nuevas. Por un lado
 , la ramificación y acotación con subestimación y  solamente ramificación  y  acotación. Para ello, hemos creado 
 dos nuevas clases en las que gestionaremos las listas. Por un lado priority() donde ordenaremos por el coste de la
 ruta. Por el otro como Subestimation(), donde ordenamos por el coste de la ruta y a parte por la heurística 
 desde el nodo actual hasta el nodo final.
 
 Ejemplo de ramificación y Acotación con Subestimación:
 Se hace uso de una función de coste total estimado acumulado para cada nodo intermedio n
 en el proceso de exploración:f*(n) = g(n) + h*(n)g(n)   .
 -->Coste real acumulado (determinista) desde el estado inicial al estado actual nh*(n).
 --> Estimación (heurística) del coste del estado actual al estado objetivo.

 Mediante el coste determinista y la estimación que nos proporciona el código, 
 podemos hallar la ruta óptima de O a T para el algoritmo ramificación  y  acotación  con  subestimación. A su vez, 
 nos encontramos con se expanden 4 nodos hasta llegar a la solución final.
 [Node T, Node A, Node Z, Node O] : 71 + 75 + 118 = 264

