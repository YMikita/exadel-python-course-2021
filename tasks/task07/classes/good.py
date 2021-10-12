import uuid as UUID


class Good:
    def __init__(self, name: str, price: float):
        self.__id = UUID.uuid4()
        self.__name = name
        self.__price = price

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price: float):
        self.__price = price
