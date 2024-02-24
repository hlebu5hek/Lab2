'''
Натуральные числа.
Выводит на экран нечетные числа, содержащие четное количество цифр, превышающее К.
Список используемых цифр (прописью) и их количество выводится отдельно.
'''

import re

#Проверка числа по условию через регулярные выражения
def check_num(gived_num, k):
    if not re.match("^[0-9]+$", gived_num):
        return False

    if not re.match("^[13579]+$", gived_num[-1]):
        return False

    if len(gived_num) % 2 != 0:
        return False

    if len(gived_num) <= k:
        return False

    return True

#Словарь цифр
dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}

#Лист для вывода
output_arr = []

#Число К
k = int(input('Число К: \n'))

#Баффер
gived_num = '1'

#Выбор способа ввода чисел
choice = input('Как вводятся лексемы:\n1) Вручную; \n2) Из файла; \n').lower()

#Ввод с клавиатуры
if choice in ['1', 'one', 'hand', 'вручную']:
    while gived_num:
        gived_num = input('Число из потока: \n')

        if gived_num in ['0', '000', 'exit', 'stop', 'cancel', 'out']:
            break

        if(check_num(gived_num, k)):
            output_arr.append(gived_num)

#Ввод из файла
elif choice in ['2', 'two', 'file', 'из файла']:
    file_name = input('Имя файла:\n')

    try:
        open(file_name, 'r')
    except:
        print('Файл отсутствует в директории проекта')
        exit()

    with open(file_name, 'r') as file:
        while 1:
            gived_num = file.readline().replace('\n', '')
            if not gived_num:
                #print('Файл закончился')
                break

            if (check_num(gived_num, k)):
                output_arr.append(gived_num)

#Вывод
for output_num in output_arr:
    print(output_num)

    cifr = []

    for i in output_num:
        if i not in cifr:
            cifr.append(i)

    cifr = sorted(cifr, key= lambda x: int(x))

    print('Количество использованных цифр:')
    print(len(cifr))

    cifr_propis = list(map(lambda x: dc_cifr[x], cifr))

    print('Использованные цифры:')
    print(*cifr_propis, sep=', ')

    print('___________________\n')
