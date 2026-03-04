from atf.api.base_api_ui import BaseApiUI
from test_14_lection.api.clients.document import Document
from test_14_lection.api.clients.wtd import WTD
from atf import *


class WTDFunctions(BaseApiUI):

    def delete_wtd_forever(self, mask):
        """Поиск и удаление документа через api
        :param mask: строка для поиска документа"""

        log("Проверяем наличие маски для поиска")
        assert_that(mask, not_equal(""), "Нельзя передавать пустую строку")
        log("Получаем список документов")
        wtd_list = WTD(self.client).list(mask)

        log("Удалям документы подходящие под маску навсегда (не в корзину)")
        for wtd in wtd_list:
            if mask in wtd["EmployeeFIOList"]:
                count = 2
                while count != 0:
                    Document(self.client).delete_documents(ido=wtd["DocID"])
                    count -= 1