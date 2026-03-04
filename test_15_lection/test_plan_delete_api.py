from atf import *
from atf.api.json_rpc import JsonRpcClient
from api.wrappers.plan_functions import PlanFunctions


class TestPlanDelete(TestCase):
    client = None
    autotest_mask = "Палм-Спрингс / ДЗ"

    @classmethod
    def setUpClass(cls):
        cls.client = JsonRpcClient(url="https://fix-online.sbis.ru/", verbose_log=2)
        cls.client.auth(login='khakhinaNastya', password="khakhinaNastya123")

        PlanFunctions(cls.client).delete_plan_by_mask(cls.autotest_mask)

    def test_01(self):
        pass

    @classmethod
    def tearDownClass(cls):
        PlanFunctions(cls.client).delete_plan_by_mask(cls.autotest_mask)
    