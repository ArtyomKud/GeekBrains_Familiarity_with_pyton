#Задача 4: Требуется вывести все целые степени двойки
#(т.е. числа вида 2k), не превосходящие числа N.
#Пример 10: 0, 1, 2, 3

print('Введите целое натуральное число: ')
inputNumber = int(input())

list1 = []
i = 0
while True:
    two = 2
    two **= i
    if two > inputNumber:
        break
    list1.append(i)
    i+=1
print(list1)



