'''
Text4°. Дан текстовый файл. Вывести количество содержащихся в нем символов и строк (маркеры концов строк EOLN и конца файла EOF при подсчете количества символов не учитывать).
Решение: Анаркулова Б.Б, группа 309ИС, КМПО, 08.11.2024
'''


filename = 'file.txt'

with open(filename, 'r') as file:
  text = file.read()
sym_count = len(text)
line_count = text.count('\n') + 1

print(f"Количество символов: {symbol_count}")
print(f"Количество строк: {line_count}")