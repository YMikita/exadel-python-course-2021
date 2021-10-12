from tasks.task07.classes.order import Order
from abc import ABC, abstractmethod
import uuid as UUID


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, order: Order, model: list):
        model.append(order)

    @abstractmethod
    def get(self, order_id: UUID, model: list):
        for order in model:
            if order.get_id() == order_id:
                return order

    @abstractmethod
    def list(self, n_latest, model: list):
        end = len(model)
        start = end - n_latest if n_latest else 0
        return model[start:end]

    @abstractmethod
    def delete(self, order_id: UUID, model: list):
        for order in model:
            if order.get_id() == order_id:
                model.remove(order)
                break
