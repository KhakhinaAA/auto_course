from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class WorkPlan(BaseApiUI):
    """Метод поиска в реестре Планов - ПланРабот.СписокПланов"""

    def list_plans(self, search):
        """Возвращает список планов по маске json
        :param search: маска в строке поиска в реестре планов
        """

        params = generate_record_list(ФильтрПоМаске=search)

        return self.client.call_rrecordset(method="ПланРабот.СписокПланов", **params).result
