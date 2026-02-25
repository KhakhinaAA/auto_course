# Напишите функцию, которая принимает кортеж num_tuple из 10 цифр num_tuple,
# и возвращает строку этих чисел в виде номера телефона str_phone.
# Например (Ввод --> Вывод) :
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  => "(123) 456-7890"

def create_phone_number(num_tuple):
    """
    Возвращает строку в виде номера телефона str_phone
    :param num_tuple: кортеж из 10 цифр
    """
    import re
    str_phone_1 = str(num_tuple)
    str_phone_2 = re.split(r'[,)(" ]', str_phone_1)
    print(str_phone_2, '1')
    while '' in str_phone_2:
        str_phone_2.remove('')
    print(str_phone_2, '2')
    a = ''.join(str_phone_2[:3])
    c = ''.join(str_phone_2[6:])
    b = ''.join(str_phone_2[3:6:1])
    str_phone = "({0}) {1}-{2}".format(a, b, c)
    print(str_phone)
    return str_phone

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 2, 3, 0, 5, 6, 0, 8, 9, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
]

test_data = [
    "(123) 456-7890", "(111) 111-1111", "(023) 056-0890", "(000) 000-0000"
]


for i, d in enumerate(data):
    assert create_phone_number(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
