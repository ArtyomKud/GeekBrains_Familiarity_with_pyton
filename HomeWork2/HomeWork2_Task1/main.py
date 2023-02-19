print('Введите количество арбузов: ')
numbersWatermelons = int(input())
massWatermelons = []
for i in range(numbersWatermelons):
    print(f'Введите массу арбуза № {i+1}')
    massWatermelons.append(int(input()))


def findingMinAndMaxWeight(list1):
    min = list1[0]
    max = list1[0]
    for i in range(len(list1)):
        if min > list1[i]:
            min = list1[i]
        if max < list1[i]:
            max = list1[i]
    print(f'арбуз для тещи весит {min} кг, арбуз для Ивана Васильевича весит {max} кг')

findingMinAndMaxWeight(massWatermelons)







