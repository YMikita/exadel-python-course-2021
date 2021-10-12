import uuid as UUID
import datetime
from tasks.task07.classes.good import Good


class Order:
    def __init__(self, client_id: UUID, goods: list[Good]):
        self.__id = UUID.uuid4()
        self.__date = datetime.date.today()
        self.__client_id = client_id
        self.__goods = goods or []

    def get_id(self):
        return self.__id

    def get_date(self):
        return self.__date

    def get_client_id(self):
        return self.__client_id

    def get_goods(self):
        return self.__goods

    def get_price(self):
        price = 0
        for good in self.__goods:
            price += good.get_price()
        return price
