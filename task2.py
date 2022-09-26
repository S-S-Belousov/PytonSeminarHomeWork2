# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def getFactorial(num):
    fact = 1
    strFact = ''
    for i in range(1, num+1):
        fact *= i
        strFact += str(fact)+' '
    return strFact


num = int(input('Введите число: '))
if num < 1:
    print('Число должно быть больше 0')
else:
    print(f'Факториал числа {num}: {getFactorial(num)}')
