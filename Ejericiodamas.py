def es_seguro(tablero, fila, columna):
    # Verifica si es seguro colocar una reina en la fila y columna dadas.
    # Comprobamos la fila y las diagonales superiores izquierda y derecha.
    n = len(tablero)
    
    # Verificar la fila horizontal
    for i in range(columna):
        if tablero[fila][i] == 1:
            return False

    # Verificar diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verificar diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(columna, n)):
        if tablero[i][j] == 1:
            return False

    return True

def encontrar_soluciones_n_reinas(n):
    def backtrack(tablero, columna):
        if columna == n:
            # Todas las reinas se han colocado con éxito, se encontró una solución
            soluciones.append([fila[:] for fila in tablero])
            return

        for fila in range(n):
            if es_seguro(tablero, fila, columna):
                tablero[fila][columna] = 1
                backtrack(tablero, columna + 1)
                tablero[fila][columna] = 0

    tablero = [[0] * n for _ in range(n)]
    soluciones = []
    backtrack(tablero, 0)
    return soluciones

N = 8  # Número de reinas y tamaño del tablero
soluciones = encontrar_soluciones_n_reinas(N)

print(f'Para n={N}, hay {len(soluciones)} soluciones:')
for i, solucion in enumerate(soluciones, start=1):
    print(f'Solución {i}:')
    for fila in solucion:
        print(' '.join(['Q' if c == 1 else '.' for c in fila]))
    print()



