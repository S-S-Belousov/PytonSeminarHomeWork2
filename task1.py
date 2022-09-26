# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def getFloatNumSumm(num):
    summ = 0
    for i in str(num):
        if i != '.':
            summ += int(i)
    return summ


num = float(input('Введите число: '))
if num < 0:
    num *= -1

print(f'Сумма чисел равна: {getFloatNumSumm(num)}')
