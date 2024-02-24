'''
Натуральные числа.
Выводит на экран нечетные числа, содержащие четное количество цифр, превышающее К.
Список используемых цифр (прописью) и их количество выводится отдельно.

Использовать регулярные выражения
'''
import re
dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'} #Словарь цифр
k = int(input("Число К = ")) #Число К
with open("text.txt", 'r') as file:
    buffer = file.readline().replace('\n', '') #Баффер
    while buffer:
        if re.match("^[0-9]+$", buffer) and re.match("^[13579]+$", buffer[-1]) and (len(buffer) % 2 == 0) and (len(buffer) > k):
            print('\n', buffer, sep=' ')
            cifr = []
            for i in buffer:
                if i in dc_cifr:
                    cifr.append(i)
            cifr_propis = list(map(lambda x: dc_cifr[x], sorted(cifr, key=lambda x: int(x))))
            print(' Количество использованных цифр:\n', len(cifr), '\n', 'Использованные цифры:\n', *cifr_propis, sep=' ')
            buffer = file.readline().replace('\n', '')