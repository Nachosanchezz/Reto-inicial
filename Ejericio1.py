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

def contar_movimientos_caballo(n):
    
    dp = [[0] * 10 for_ in range(n + 1)]

    for i in range (10):
        dp[1][i] = 1

    for pasos in range(2, n + 1):
        for inicio in range(10):
            for siguiente in movimientos[inicio]:
                dp[pasos][inicio] += dp [pasos - 1][siguiente]

    total = sum(dp[n])
    return total

n = 500
total_movimientos = contar_movimientos_caballo(n)
print(f"Total movimientos para {n} pasos: {total_movimientos}")



