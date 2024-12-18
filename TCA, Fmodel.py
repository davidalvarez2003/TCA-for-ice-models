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

def mostrar_cuadricula(cuadricula):
    """
    Muestra la cuadrícula utilizando matplotlib, donde cada número tiene un color distinto.
    También incluye una leyenda que explica qué número corresponde a qué color.
    """
    # Convertir la cuadrícula a una matriz de numpy para poder trabajar con matplotlib
    cuadricula_np = np.array(cuadricula)

    # Asignar colores a los números (1, 2, 3)
    cmap = plt.get_cmap("tab20c")  # Elegimos una paleta de colores

    # Crear la imagen
    plt.imshow(cuadricula_np, cmap=cmap, interpolation='nearest')

    # Añadir una leyenda personalizada
    plt.legend([plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=cmap(0.1), markersize=10),
                plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=cmap(0.3), markersize=10),
                plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=cmap(0.5), markersize=10)],
               ['Número 1', 'Número 2', 'Número 3'],
               loc='upper right')

    # Añadir etiquetas a los ejes
    plt.title("Cuadrícula con números entre 1 y 3")
    plt.xlabel("Columnas")
    plt.ylabel("Filas")

    # Mostrar la cuadrícula
    plt.show()

# Definir las dimensiones de la cuadrícula
n = 8  # Número de filas
m = 10  # Número de columnas

# Crear la cuadrícula
cuadricula = llenar_cuadricula(n, m)

# Mostrar la cuadrícula usando matplotlib
mostrar_cuadricula(cuadricula)

# Calcular la polarización (número de flechas hacia arriba)
polarizacion = calcular_polarizacion(cuadricula, n, m)

# Mostrar el resultado de la polarización
print(f"Energia total del sistema = {polarizacion}")

