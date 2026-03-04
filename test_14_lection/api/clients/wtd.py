from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class WTD(BaseApiUI):
    """Метод поиска в реестре - WTD.List"""

    def list(self, search):
        """Возвращает список отгулов по маске json
        :param search: маска в строке поиска в реестре отгулов
        """
        params = generate_record_list(ФильтрПоиска=search, ФильтрДатаС=(None, "Строка"), ФильтрДатаП=(None, "Строка"))

        return self.client.call_rrecordset(method='WTD.List', **params).result
