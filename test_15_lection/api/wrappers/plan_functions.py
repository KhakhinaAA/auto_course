from atf.api.base_api_ui import BaseApiUI
from test_15_lection.api.clients.work_plan import WorkPlan
from test_15_lection.api.clients.document import Document
from atf import *


class PlanFunctions(BaseApiUI):

    def delete_plan_by_mask(self, mask):
        """Поиск и удаление документа через api
                :param mask: строка для поиска документа"""

        log("Проверяем наличие маски для поиска")
        assert_that(mask, not_equal(""), "Нельзя передавать пустую строку")
        log("Получаем список документов")
        plan_list = WorkPlan(self.client).list_plans(mask)

        log("Удалям документы подходящие под маску навсегда (не в корзину)")
        for plan in plan_list:
            if mask in plan["Название"]:
                count = 2
                while count != 0:
                    Document(self.client).delete_documents(ido=plan["@Документ"])
                    count -= 1

