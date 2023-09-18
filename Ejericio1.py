tablero = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9],
    [None, 0, None]
]

n = 2

def contar_movimientos(tablero, n):

movimientos = {
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

