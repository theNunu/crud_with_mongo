def filtrar_pares(salida: 'list' = []) -> 'list':
    return [i for i in salida if i%2 == 0]

print(filtrar_pares([1, 2, 3, 4, 5, 6]))
# Salida: [2, 4, 6]