# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


@pytest.mark.usefixtures("log_test_duration_1")
class TestMy:

    def test(self):
        pass

    def test_1(self):
        pass

    def test_2(self, log_test_duration):
        pass


# TestMy()
