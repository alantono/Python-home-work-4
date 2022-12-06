# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math
n = int(input('Задайте натуральное число: '))

while n % 2 == 0:
    print(2)
    n = n / 2
# print(n)
for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        print(i)
        n = n / i
if n > 2:
    print(n)
