# Compilador-SSPTDL2
El programa realiza un análisis léxico y es capaz de distinguir un total de 24 símbolos léxicos, que podemos ver a continuación.
![Image text](https://github.com/JOrtegaM230/Compilador-SSPTDL2/blob/main/img/tokens.png) 
En la siguiente imagen podemos ver la entrada que recibe el programa como código fuente, el cual será sometido a un análisis léxico.  
![Image text](https://github.com/JOrtegaM230/Compilador-SSPTDL2/blob/main/img/entrada.png)  
A continuación se pueden ver los datos de salida dados por el analizador léxico.  
![Image text](https://github.com/JOrtegaM230/Compilador-SSPTDL2/blob/main/img/salida.png)


El analizador sintáctico recibe como entrada la cadena de código fuente y el conjunto de tokens que devolvió el analizador léxico, hace uso de una pila de elementos pila, en lugar de una pila de enteros para realizar el análisis sintáctico.
En la siguiente imagen podemos ver la entrada y los resultados del análisis léxico que van a ingresar al analizador sintáctico:
![Image text](https://github.com/JOrtegaM230/Compilador-SSPTDL2/blob/main/img/entrada2.png)
Posteriormente el analizador sintáctico va imprimiendo el estado en el que se encuentra la pila, así como el estado de la entrada y la salida que se produce con dicha entrada.
![Image text](https://github.com/JOrtegaM230/Compilador-SSPTDL2/blob/main/img/salida2.png)
Y por último, se muestra el resultado final del árbol sintáctico que se produjo con la entrada.
![Image text](https://github.com/JOrtegaM230/Compilador-SSPTDL2/blob/main/img/salida3.png)