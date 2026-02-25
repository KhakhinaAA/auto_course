# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код

def list_words():
    j = ''
    c = ''
    z = []
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    # print(alphabet)
    for i in range(1, random.randint(2, 16)):
        j = f"{j}{random.choice(alphabet)}"
    # print(j)
    # print(type(j))
    for m in range(1, random.randint(2, 16)):
        c = f"{c}{random.choice(alphabet)}"
    n = f'{j} {c}'
    z.append(n)
    return z


def generate_random_name():
    while True:
        a = list_words()
        for n in a:
            yield n


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
