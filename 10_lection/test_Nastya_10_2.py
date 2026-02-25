# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного.
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты.

import pytest


def all_division(*arg1):
    division = arg1[0]
    print(f'{division}division')
    print(f'проверяю что есть {arg1}')
    for i in arg1[1:]:
        print(i)
        if i == 0:
            raise ZeroDivisionError()
        else:
            division /= i
    print(f'{division}division на выходе')
    return division


@pytest.mark.smoke
def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(0, 0, 0, 0)


@pytest.mark.acceptance
def test_1():
    assert all_division(1, 2, 3, 4, 5, 6, 2)


@pytest.mark.smoke
def test_2():
    assert all_division(36, 9, 0.5, 0.1)


def test_3():
    assert all_division(75, 50, 26, 2)


def test_4():
    with pytest.raises(ZeroDivisionError):
        all_division(36, 9, 0.5, 0)

# вызов всех тестов в папке: pytest -v
# вызов тестов в файлике: pytest test_Nastya_10_2.py -v
# вызвать все тесты содержащие слово и не содержащие данное слово:  pytest -k 'not star'-v  и  pytest -k 'star'-v
# вызвала конкретный тест с выводом print: pytest  --capture=no test_Nastya_10_2.py::test_2
# вызов по маркеру:  pytest -m smoke

# все возможности вызова: pytest -h
