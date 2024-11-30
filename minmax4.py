'''
Minmax4°. Дано целое число N и набор из N чисел. Найти номер минимального элемента из данного набора.
Решение: Анаркулова Б.Б, группа 309ИС, КМПО, 08.11.2024
'''

n = int(input())
min = 1
max = 0
for i in range(n):
    num = float(input())
    if num < min:
        min = num
    elif num > max:
        max = num
print(f"min: {int(min)}")
print(f"max: {int(max)}")