# Реализуйте алгоритм перемешивания списка.
import random
import function

lenList = int(input('Введите количество элементов списка: '))
minList = int(input('Введите минимальный элемент списка: '))
maxList = int(input('Введите максимальный элемент списка: '))
randList = function.getRandomList(lenList, minList, maxList)
print(f'Изначальный список: {randList}')
random.shuffle(randList)
print(f'Перемешанный список: {randList}')
