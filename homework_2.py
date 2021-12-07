# ---------------------------------------
# Program by la bella vita
# ---------------------------------------
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

for i in list_c:
    D = list_b[0] ** 2 - 4 * list_a[0] * i
    if D == 0:
        x = -list_b[0] / 2 * list_a[0]
        print(f"{list_a[0]}x^2 + {list_b[0]}x + {i} = 0 |   D = {D}, один корень    |   x = {round(x, 2)}")
    if D > 0:
        x1 = -list_b[0] + math.sqrt(D) / 2 * list_a[0]
        x2 = -list_b[0] - math.sqrt(D) / 2 * list_a[0]
        print(
            f"{list_a[0]}x^2 + {list_b[0]}x + {i} = 0 | D = {D}, два корня    |   x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
    if D < 0:
        print(f"{list_a[0]}x^2 + {list_b[0]}x + {i} = 0 |   D = {D}, D < 0  |   Не имеет решений")

for i in list_b:
    D = i ** 2 - 4 * list_a[0] * list_c[0]
    if D == 0:
        x = -i / 2 * list_a[0]
        print(f"{list_a[0]}x^2 + {i}x + {list_c[0]} = 0 |   D = {D}, один корень    |   x = {round(x, 2)}")
    if D > 0:
        x1 = -i + math.sqrt(D) / 2 * list_a[0]
        x2 = -i - math.sqrt(D) / 2 * list_a[0]
        print(
            f"{list_a[0]}x^2 + {i}x + {list_c[0]} = 0 |   D = {D}, два корня    | x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
    if D < 0:
        print(f"{list_a[0]}x^2 + {i}x + {list_c[0]} = 0 |   D = {D}, D < 0 |    Не имеет решений")

for i in list_a:
    D = list_b[0] ** 2 - 4 * i * list_c[0]
    if D == 0:
        x = -list_b[0] / 2 * list_a[0]
        print(f"{i}x^2 + {list_b[0]}x + {list_c[0]} = 0 |   D = {D}, один корень    |   x = {round(x, 2)}")
    if D > 0:
        x1 = -list_b[0] + math.sqrt(D) / 2 * i
        x2 = -list_b[0] - math.sqrt(D) / 2 * i
        print(
            f"{i}x^2 + {list_b[0]}x + {list_c[0]} = 0 |   D = {D}, два корня  | x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
    if D < 0:
        print(f"{i}x^2 + {list_b[0]}x + {list_c[0]} = 0 |   D = {D}, D < 0  |   Не имеет решений")

# def solution(list1=[], list2=[], list3=[]):
#     for i in list3:
#         D = list2[0] ** 2 - 4 * list1[0] * i
#         if D == 0:
#             x = -list2[0] / 2 * list1[0]
#             print(f"{list1[0]}x^2 + {list2[0]}x + {i} = 0 |   D = {D}, один корень  |   x = {round(x, 2)}")
#         elif D > 0:
#             x1 = -list2[0] + math.sqrt(D) / 2 * list1[0]
#             x2 = -list2[0] - math.sqrt(D) / 2 * list1[0]
#             print(
#                 f"{list1[0]}x^2 + {list2[0]}x + {i} = 0 |   D = {D}, два корня    |   x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
#         elif D < 0:
#             print(f"{list1[0]}x^2 + {list2[0]}x + {i} = 0 |   D = {D}, D < 0    |   Не имеет решений")
