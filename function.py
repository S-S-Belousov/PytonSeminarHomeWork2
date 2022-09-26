import random


def getRandomList(lenList, minList, maxList):
    randList = []
    for i in range(1, lenList+1):
        randList.append(random.randint(minList, maxList+1))
    return randList
