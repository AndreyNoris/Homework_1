"""2. Дана матрица целых чисел 10x10.
Вводится число. Выяснить, какие строки и столбцы матрицы содержат данное число.
(либо рандом либо чтение из файла (input.txt))
READ FILE:"""
data = []
with open('input.txt') as f:
    for line in f:
        data.append([int(x) for x in line.split()])

rows_list = []
columns_list = []

for m in data:
    print(m)

var = int(input("Input your number in range(0-100): "))

for i, j in enumerate(data):
    if var in j:
        rows_list.append(i)
        columns_list.append(j.index(var))

print("Columns(index):", *columns_list)
print("Rows(index):", *rows_list)
