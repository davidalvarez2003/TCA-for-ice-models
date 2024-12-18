# TCA-for-ice-models
Este repositorio contiene dos codigos que utilizan el algoritmo de tres colores para recrear configuraciones de estructuras de hielo permitidas por las reglas de hielo.

El primer codigo hace una sola iteracion creando una cuadricula con colores aleatorios y asignando un numero del 1 al 3 a cada cuadrado. Se debe cumplir que cuadrados adyacentes no deben tener el mismo numero. El sistema asigna flechas entre cada cuadrado que tienen una direccion especifica. Si el cuadrado adyacente tiene un numero mayor, entonces la direccion de la flecha es hacia la izquierda y a la derecha si tiene un numero menor. La configuracion resultante de flechas es una que respeta las reglas de hielo propuestas por Brenan y Fowler en 1933. 

