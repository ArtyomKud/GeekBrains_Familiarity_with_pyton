#Задача 1. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
#Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
#Input: 5 -> 5 1 6 5 9
#Output: 1 9

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







