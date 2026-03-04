from atf.api.base_api_ui import BaseApiUI


class Document(BaseApiUI):
    """Метод удаления документа - Документ.УдалитьДокументы """
    def delete_documents(self, ido):
        """Вызов метода удаления документа
        :param ido: ИДО документа в методе Документ.УдалитьДокументы
        """

        params = {"ИдО": ido}

        self.client.call_rrecord(method="Документ.УдалитьДокументы", **params)
