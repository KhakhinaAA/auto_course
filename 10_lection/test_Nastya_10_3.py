# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0][0]
    print(f'{division} division')
    for i in arg1[0][1:]:
        print(f'{i} i')
        division /= i
    return division


@pytest.mark.parametrize('a', [
    pytest.param((1, 2, 3, 4, 5, 6, 2), marks=pytest.mark.smoke),
    pytest.param((0, 0, 0, 0), marks=pytest.mark.skip('bad test')),
    pytest.param((36, 9, 0.5, 0.1)),
    pytest.param((75, 50, 26, 2))
])
def test_1(a):
    assert all_division(a)


@pytest.mark.skip('bad test')
def test_4():
    with pytest.raises(ZeroDivisionError):
        all_division(36, 9, 0.5, 0)
