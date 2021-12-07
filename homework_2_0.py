"""1. Программа принимает от пользователя диапазоны для коэффициентов a, b, c квадратного уравнения: ax2 + bx + c = 0.
Перебирает все варианты целочисленных коэффициентов в указанных диапазонах,
определяет квадратные уравнения, которые имею решение"""

import math

try:
    a = input("Введите диапазон значений коэффициента A в формате 10 20: ").split(' ')
    list_a = [i for i in range(int(a[0]), int(a[1]), 1)]
    b = input("Введите диапазон значений коэффициента B в формате 10 20: ").split(' ')
    list_b = [i for i in range(int(b[0]), int(b[1]), 1)]
    c = input("Введите диапазон значений коэффициента C в формате 10 20: ").split(' ')
    list_c = [i for i in range(int(c[0]), int(c[1]), 1)]
except:
    print("[Info] Проверьте ввод коэффициентов в диапазоне !!!")
    exit()

for i in list_a:
    for j in list_b:
        for l in list_c:
            D = j ** 2 - 4 * i * l
            if D == 0:
                x = -j / 2 * i
                print(f"{i}x^2 + {j}x + {l} = 0 |   D = {D}, один корень    |   x = {round(x, 2)}")
            elif D > 0:
                x1 = -j + math.sqrt(D) / 2 * list_a[0]
                x2 = -j - math.sqrt(D) / 2 * list_a[0]
                print(
                    f"{i}x^2 + {j}x + {l} = 0 | D = {D}, два корня    |   x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
            elif D < 0:
                print(f"{i}x^2 + {j}x + {l} = 0 |   D = {D}, D < 0  |   Не имеет решений")
