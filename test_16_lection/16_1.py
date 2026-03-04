from atf.ui import *
from atf.api.json_rpc import JsonRpcClient
from api.wrappers.dialog_function import DialogsFunctions

class TestMessage(TestCase):

    client = None
    autotest_mask = "autotest"

    @classmethod
    def setUpClass(cls):

        cls.client = JsonRpcClient(url="https://fix-online.sbis.ru/")
        cls.client.auth(login="khakhinaNastya", password="khakhinaNastya123", verbose_log=2)

        DialogsFunctions(cls.client).delete_message_by_mask(cls.autotest_mask)
        DialogsFunctions(cls.client).delete_message_by_mask("")

    def test_01_send_message(self):
        pass

    @classmethod
    def tearDownClass(cls):
        DialogsFunctions(cls.client).delete_message_by_mask(cls.autotest_mask)