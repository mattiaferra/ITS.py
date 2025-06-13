# Somma della diagonale primaria (da in alto a sinistra a in basso a destra)

def sum_primary_diagonal(matrix: list[list[int]]) -> int:

    somma = 0

    for i in range(len(matrix)):

        somma += matrix[i][i]

    return somma

# Somma della diagonale secondaria (da in alto a destra a in basso a sinistra)

def sum_secondary_diagonal(matrix: list[list[int]]) -> int:

    somma = 0
    n = len(matrix)

    for i in range(n):

        somma += matrix[i][n - 1 - i]
        
    return somma
