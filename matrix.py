def matrix_sum(data):
    sum_main = 0
    # по умолчанию предпологаем что матрица квадратная
    for i in range(len(data)):
        sum_main += data[i][i]
    return sum_main

data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35],
]

for row in data:
    print(row)

print(matrix_sum(data))

