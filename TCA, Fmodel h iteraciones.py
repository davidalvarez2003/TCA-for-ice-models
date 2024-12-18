import random
import matplotlib.pyplot as plt
import numpy as np

def es_valido(cuadricula, fila, col, n, m):
    """
    Verifica si es válido colocar un número en la posición (fila, col) de la cuadrícula.     
    """
    # Verificar arriba
    if fila > 0 and cuadricula[fila-1][col] == cuadricula[fila][col]:
        return False
    # Verificar abajo
    if fila < n-1 and cuadricula[fila+1][col] == cuadricula[fila][col]:
        return False
    # Verificar izquierda
    if col > 0 and cuadricula[fila][col-1] == cuadricula[fila][col]:
        return False
    # Verificar derecha
    if col < m-1 and cuadricula[fila][col+1] == cuadricula[fila][col]:
        return False
    
    return True

def llenar_cuadricula(n, m):
    # Crear la cuadrícula inicial vacía
    cuadricula = [[0] * m for _ in range(n)]
    
    # Llenar la cuadrícula
    for fila in range(n):
        for col in range(m):
            # Intentamos asignar un número válido en cada celda
            numeros_posibles = [1, 2, 3]
            random.shuffle(numeros_posibles)  # Mezclamos para evitar patrones

            for num in numeros_posibles:
                cuadricula[fila][col] = num
                if es_valido(cuadricula, fila, col, n, m):
                    break  # Si es válido, nos movemos a la siguiente celda
                cuadricula[fila][col] = 0  # Si no es válido, volvemos a intentarlo
                
    return cuadricula

def calcular_polarizacion(cuadricula, n, m):
    polarizacion = 0
    
    # Recorremos toda la cuadrícula
    for fila in range(n):
        for col in range(m):
            valor_actual = cuadricula[fila][col]
            
            # Comparamos con los vecinos (arriba, abajo, izquierda, derecha)
            flecha = 0  # Si no hay flecha hacia arriba, será 0 por defecto
            # Arriba
            if fila > 0 and cuadricula[fila-1][col] > valor_actual:
                flecha = -1
            # Abajo
            elif fila < n-1 and cuadricula[fila+1][col] > valor_actual:   #Para adaptar esto a un modelo de Rys en el que se favorecen interacciones 5 y 6 se cambia < por >
                flecha = -1
            # Izquierda
            elif col > 0 and cuadricula[fila][col-1] > valor_actual:
                flecha = -1
            # Derecha
            elif col < m-1 and cuadricula[fila][col+1] > valor_actual:
                flecha = -1
            
            # Sumamos las flechas que apuntan hacia arriba (flecha == 1)
            polarizacion += flecha
    
    return polarizacion

# Definir las dimensiones de la cuadrícula y número de iteraciones
n = 8  # Número de filas
m = 8  # Número de columnas
h = 60  # Número de iteraciones

# Lista para almacenar las polarizaciones de cada iteración
polarizaciones = []

# Realizar h iteraciones y calcular la polarización en cada una
for i in range(h):
    # Crear la cuadrícula
    cuadricula = llenar_cuadricula(n, m)
    
    # Calcular la polarización
    polarizacion = calcular_polarizacion(cuadricula, n, m)
    
    # Guardar el valor de polarización
    polarizaciones.append(polarizacion)

# Calcular la media y varianza de la polarización
media_polarizacion = np.mean(polarizaciones)
varianza_polarizacion = np.var(polarizaciones)

# Mostrar la media y varianza
print(f"Media de la polarización: {media_polarizacion}")
print(f"Varianza de la polarización: {varianza_polarizacion}")

# Graficar la polarización por iteración
plt.plot(range(h), polarizaciones, marker='o', color='b', linestyle='-', markersize=5)
plt.xlabel("Número de Iteración")
plt.ylabel("Polarización")
plt.title("Polarización por Iteración")
plt.grid(True)
plt.show()

