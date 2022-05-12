L = input('Введите целые числа через пробел: ')

a = int(input('Введите любое целое число a: '))
list_of_str = L.split()
list_of_num = list(map(int, list_of_str))
print('Получаем список: ', list_of_num)

import collections
dq = collections.deque(list_of_num)
dq.appendleft(a)
list_of_num = list(dq)
print('Добавляем в список элемент a: ', list_of_num)

for i in range(1, len(list_of_num)):
    x = list_of_num[i]
    idx = i
    while idx > 0 and list_of_num[idx-1] > x:
        list_of_num[idx] = list_of_num[idx-1]
        idx -= 1
    list_of_num[idx] = x
print('Сортируем новый список: ', list_of_num)

def find(list_of_num, a):
    for i, b in enumerate(list_of_num):
        if b == a:
            return i
    return False
c = a - 1
d = a + 1

print('Кол-во элементов в списке: ', len(list_of_num))
print('Номер позиции элемента a:', find(list_of_num, a))
print('Номер позиции элемента,стоящего перед a:', find(list_of_num, c))
print('Номер позиции элемента,стоящего после a:', find(list_of_num, d))
