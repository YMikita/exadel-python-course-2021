from tasks.task07.classes.repository import Repository
from tasks.task07.classes.abstract_repository import AbstractRepository
from tasks.task07.classes.order import Order
from tasks.task07.classes.abstract_repository import AbstractRepository
import uuid as UUID


class RepositoryWithAbstract(Repository, AbstractRepository):
    def __init__(self):
        super().__init__()
        self.__storage = super().get_items()

    def add(self, order: Order):
        super().add(order, self.__storage)

    def get(self, order_id: UUID):
        return super().get(order_id, self.__storage)

    def list(self, n_latest: int = 0):
        return super().list(n_latest, self.__storage)

    def delete(self, order_id: UUID):
        super().delete(order_id, self.__storage)
