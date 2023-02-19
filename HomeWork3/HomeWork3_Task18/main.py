'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5'''
print('Введите количество чисел в массиве: ')
numberOfNumberArray = int(input())
list1 = []
for i in range(numberOfNumberArray):
    print(f'Введите число натуральное число № {i+1}')
    list1.append(int(input()))
print('Введите проверяемое число:')
numberToCheck = int(input())
temp1 = int(list1[0])

for i in range(len(list1)):

    temp2 = int(list1[i])
    if temp2 == numberToCheck:
        temp1 = temp2
        break
    if temp1 < int(list1[i]) < numberToCheck:
        temp1 = temp2
    if numberToCheck < temp2 < temp1:
        temp1 = temp2

print(list1)
print(temp1)