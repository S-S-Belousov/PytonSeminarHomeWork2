# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число
from random import randint
from function import getRandomList
from os import path


def genPositions(lenList):
    with open('file.txt', 'w') as txtFile:
        newlenList = []
        lenPositions = randint(1, lenList)
        for i in range(lenPositions):
            line = str(randint(0, lenList))
            txtFile.write(line+'\n')
            newlenList.append(line)
    return newlenList


def multiplicationNumList(multiplicationList, randomList):
    res = 1
    for i in range(len(multiplicationList)):
        res *= int(randomList[int(multiplicationList[i])])
    return res


lenList = int(input('Введите количество элементов списка: '))
randomList = getRandomList(lenList, -lenList, lenList)
print(f'Сгенерированный список элементов: {randomList}')
listPositions = []
if (path.exists('file.txt')):
    if input('Найден файл "file.txt". Загрузить позиции для нахождения произведения элементов? (Y - Да, N - сгенерировать новые позиции): ') == 'Y':
        with open('file.txt', 'r') as txtFile:
            listPositions = txtFile.read().splitlines()
            for i in range(len(listPositions)+1):
                if len(listPositions) > lenList:
                    print(
                        f'В файле "file.txt" есть позиции превышающие введенное количество позиций. Программа будет завершена.')
                    quit()
    else:
        listPositions = genPositions(lenList)
else:
    listPositions = genPositions(lenList)

print(
    f'Произведение чисел на позициях {listPositions}: {multiplicationNumList(listPositions, randomList)}')
