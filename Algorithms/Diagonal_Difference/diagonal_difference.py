# Diagonal difference


def diagonal_diff(arr):
    diagonal_a = 0
    diagonal_b = 0
    i = 0
    while i < len(arr):
        diagonal_a=diagonal_a + arr[i][i]
        diagonal_b=diagonal_b + arr[i][-(i+1)]
        i+=1

    if diagonal_a<diagonal_b: return diagonal_b-diagonal_a 
    if diagonal_a>diagonal_b: return diagonal_a-diagonal_b
    if diagonal_a==diagonal_b: return diagonal_b-diagonal_a 


# a = [[11, 2, 4],[4, 5, 6], [190, 8, 2]]
a = [[1, 1, 1],[1, 1, 1], [1, 1, 1]]


dig = diagonal_diff(a)
print(dig)