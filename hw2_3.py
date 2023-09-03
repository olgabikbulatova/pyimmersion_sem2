# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import fractions
import math

def mult_fraction(a, b):
    if math.gcd(b, a) > 1:
        a //= math.gcd(b, a)
        b //= math.gcd(b, a)
    return f'{a}/{b}'

def sum_fraction(a, b, c, d):
    num = (a * (math.lcm(b, d) // b)) + (c * (math.lcm(b, d) // d))
    den = math.lcm(b, d)
    return mult_fraction(num, den)

def comp_fraction(a, b, c, d):
    num = a * c
    den = b * d
    return mult_fraction(num, den)


fr1 = '1/2'
fr2 = '5/6'
# a = input('Веедите дробь: ')
# b = input('Веедите дробь: ')
a = int(fr1[:fr1.index('/')])
b = int(fr1[fr1.index('/')+1:])
c = int(fr2[:fr2.index('/')])
d = int(fr2[fr2.index('/')+1:])
f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(c, d)

print(f'Сумма дробей {fr1} и {fr2} равна {sum_fraction(a, b, c, d)}' )
print(f'Проверка модулем Fraction сумма: {f1 + f2}')
print(f'Произведение дробей {fr1} и {fr2} равно {comp_fraction(a, b, c, d)}' )
print(f'Проверка модулем Fraction произведение: {f1 * f2}')


