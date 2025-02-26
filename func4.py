'''
Func4. Описать функцию RingS(R1, R2) вещественного типа, находящую площадь кольца, заключенного между двумя окружностями с общим центром и радиусами R1 и R2 (R1 и R2 — вещественные, R1 > R2). С ее помощью найти площади трех колец, для которых даны внешние и внутренние радиусы. Воспользоваться формулой площади круга радиуса R: S = π·R2. В качестве значения π использовать 3.14.
Решение: Анаркулова Б.Б, группа 309ИС, КМПО, 08.11.2024
'''

import math
def rings(r1, r2):
    s_out = math.pi * (r1 ** 2)
    s_inn = math.pi * (r2 ** 2)
    s_ring = s_out - s_inn
    return round(s_ring,2)

r1 = float(input())
r2 = float(input())
result = rings(r1, r2)
print(f"Площадь кольца: {result}")