'''
Matrix4. Даны целые положительные числа M, N и набор из N чисел. Сформировать матрицу размера M × N, у которой в каждой строке содержатся все числа из исходного набора (в том же порядке).
Решение: Анаркулова Б.Б, группа 309ИС, КМПО, 08.11.2024
'''

m = int(input())
n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

matrix = []
for _ in range(m):
    matrix.append(nums.copy())

print("Матрица:")
for row in matrix:
    print(row)