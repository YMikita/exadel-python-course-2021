from tasks.task07.classes.good import Good
from tasks.task07.classes.order import Order
from tasks.task07.classes.repository_with_abstract import RepositoryWithAbstract
import uuid as UUID

mockup_client_id = UUID.uuid4()
mockup_sum = 1.12 + 2.12 + 3.12 + 4.12 + 5.12 + 5.12 + 6.12
mockup_goods = [
    Good("good1", 1.12),
    Good("good2", 2.12),
    Good("good3", 3.12),
    Good("good4", 4.12),
    Good("good5", 5.12),
    Good("good6", 5.12),
    Good("good7", 6.12)
]

# Test Good
good = Good("good0", 1.12)
assert isinstance(good, Good)
assert good.get_id() != ""
assert good.get_price() == 1.12
assert good.get_name() == "good0"

# Test Order
order = Order(mockup_client_id, mockup_goods)
order_id = order.get_id()
assert isinstance(order, Order)
assert order.get_id() != ""
assert order.get_client_id() == mockup_client_id
assert order.get_date() != ""
assert order.get_price() == mockup_sum
assert order.get_goods() == mockup_goods

# Test AbstractRepository
order_repository = RepositoryWithAbstract()
assert isinstance(order_repository, RepositoryWithAbstract)
order_repository.add(order)
assert order_repository.list() == [order]
assert order_repository.list(1) == [order]
assert order_repository.get(order_id) == order
order_repository.delete(order_id)
assert len(order_repository.list()) == 0

print("Tests passed")
