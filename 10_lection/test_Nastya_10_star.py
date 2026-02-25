# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test(request):
    marks = request.node.get_closest_marker('id_check')
    ids = marks.args
    print(f'Это переданные id: {ids}')
    assert len(ids) > 0, "нет переданных id"
    # Здесь пишем код
    pass
