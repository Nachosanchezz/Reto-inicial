def movimientos_validos(cantidad_movimientos):
    movimientos_caballo = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    
    def calcular_movimientos(posicion, movimientos_restantes):
        if movimientos_restantes == 0:
            return 1
        
        movimientos_validos = 0
        
        for siguiente_posicion in movimientos_caballo[posicion]:
            movimientos_validos += calcular_movimientos(siguiente_posicion, movimientos_restantes - 1)
        
        return movimientos_validos
    
    total_movimientos_validos = 0
    
    for cantidad_movimientos in range(1, 33):
        total_movimientos_validos = calcular_movimientos(0, cantidad_movimientos)
        print(f"{cantidad_movimientos}\t{total_movimientos_validos}")

movimientos_validos(32)
