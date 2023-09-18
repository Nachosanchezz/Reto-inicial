def contar_movimientos_caballo(n):
    movimientos_caballo = {
        0: [6, 4], 
        1: [6, 8], 
        2: [7, 9], 
        3: [4, 8], 
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3], 
        9: [2, 4], 
    }
    
    dp = [[0] * 10 for _ in range(n + 1)]

    for i in range(10):
        dp[1][i] = 1

    for pasos in range(2, n + 1):
        for inicio in range(10):
            for siguiente in movimientos_caballo[inicio]:
                dp[pasos][inicio] += dp[pasos - 1][siguiente]

    total_caballo = sum(dp[n])
    return total_caballo

def contar_movimientos_tablero(tablero, n):
    movimientos_tablero = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]

    def contar_movimientos_desde(fila, columna, movimientos_restantes):
        if movimientos_restantes == 0:
            return 1

        movimientos_validos = 0
        for mov in movimientos_tablero:
            nueva_fila = fila + mov[0]
            nueva_columna = columna + mov[1]
            if 0 <= nueva_fila < len(tablero) and 0 <= nueva_columna < len(tablero[0]) and tablero[nueva_fila][nueva_columna] is not None:
                movimientos_validos += contar_movimientos_desde(nueva_fila, nueva_columna, movimientos_restantes - 1)

        return movimientos_validos

    total_movimientos_tablero = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            if tablero[fila][columna] is not None:
                total_movimientos_tablero += contar_movimientos_desde(fila, columna, n - 1)

    return total_movimientos_tablero

n_caballo = 500
total_movimientos_caballo = contar_movimientos_caballo(n_caballo)
print(f"Total movimientos para el caballo en {n_caballo} pasos: {total_movimientos_caballo}")

tablero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [None, 0, None]
]

n_tablero = 2  # Número de movimientos

total_movimientos_tablero = contar_movimientos_tablero(tablero, n_tablero)
print(f"Total de movimientos posibles en el tablero en {n_tablero} movimientos: {total_movimientos_tablero}")