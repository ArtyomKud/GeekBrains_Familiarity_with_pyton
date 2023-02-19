"""Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1"""

print('Введите количество чисел в массиве: ')
numberOfNumberArray = int(input())
list1 = []
for i in range(numberOfNumberArray):
    print(f'Введите число натуральное число № {i+1}')
    list1.append(int(input()))
print('Введите проверяемое число:')
numberToCheck = int(input())
count = 0
for i in range(len(list1)):
    if int(list1[i]) == numberToCheck:
        count+=1
        break
print(list1)
if count == 0:
    print('Число не найдено!')
else:
    print(count)



