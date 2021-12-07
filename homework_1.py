import random

matrix = [[random.randint(0, 100) for n in range(10)] for m in range(10)]

rows_list = []
columns_list = []

for m in matrix:
    print(m)

var = int(input("Input your number in range(0-100): "))

for i, j in enumerate(matrix):
    if var in j:
        rows_list.append(i)
        columns_list.append(j.index(var))

print("Columns(index):", *columns_list)
print("Rows(index):", *rows_list)
