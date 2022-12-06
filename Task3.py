# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]
from random import randint
_list = []
_list1 = []

for i in range(10):
    _list.append(randint(0, 10))

for i in _list:
    if i not in _list1:
        _list1.append(i)

print(f'Ввод:  {_list}\nВывод: {_list1}')
