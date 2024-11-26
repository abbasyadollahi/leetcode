from collections.abc import Iterable
from itertools import filterfalse, tee


class Order:
    def __init__(self, is_buy: bool, qty: int, price: float) -> None:
        self.is_buy = is_buy
        self.qty = qty
        self.price = price

    def __repr__(self) -> str:
        return "{} {}@${:.1f}".format("buy" if self.is_buy else "sell", self.qty, self.price)

    def __gt__(self, other: "Order") -> bool:
        return self.price > other.price


class OrderBook:
    def __init__(self) -> None:
        self._orders: list[Order] = []

    def __enter__(self) -> "OrderBook":
        return self

    def __exit__(self, *args) -> None:
        """
        Formats and prints the order book as the test cases expect.
        """
        buys, sells = self._split_into_buy_and_sell_orders()
        buys = sorted(buys)
        sells = sorted(sells)
        for o in [*buys, *sells]:
            print(o)

    def _split_into_buy_and_sell_orders(self) -> tuple[Iterable[Order], Iterable[Order]]:
        """
        Splits orders into buy and sell orders.
        Returns a pair of iterables:
            - First points to the buy orders.
            - Second points to the sell orders.
        """
        is_buy = lambda o: o.is_buy
        buys, sells = tee(self._orders)
        return filter(is_buy, buys), filterfalse(is_buy, sells)

    def add(self, order: Order) -> None:
        """
        Checks the opposing side's available orders.
        For a buy order, look at existing sell orders, and vice versa.
        If a trade is possible, update the order book accordingly.
        Otherwise, insert the order into the book.
        """
        while True:
            other = self._find_opposite_trade(order)
            if order.qty == 0:
                # If the order quantity is 0, no trades will be executed
                break
            elif other is None and order.qty > 0:
                # If there's no opposite match in the OB, add this order to the OB
                # When adding, check if there's an existing order with the same price
                # If so, increase that order's quantity, otherwise, add this as a new order
                match = next(
                    (_order for _order in self._orders if _order.price == order.price),
                    None,
                )
                if match is None:
                    self._orders.append(order)
                else:
                    match.qty += order.qty
                break
            elif other.qty < order.qty:
                # If the order quantity is larger than the other's quantity,
                # we will trade all the other's available shares and remove it from the OB
                order.qty -= other.qty
                self._orders.remove(other)
            elif other.qty > order.qty:
                # If the order quantity is smaller than the other's quantity,
                # we will execute the entire order and reduce the other's by its number of shares
                other.qty -= order.qty
                break
            else:
                # The order and other have equal quantities, so they will
                # both cancel each other out
                self._orders.remove(other)
                break

    def _find_opposite_trade(self, order: Order) -> Order | None:
        """
        Returns an order for the best "match" for a given order.
        For buy orders, this would be the lowest sell price.
        For sell orders,the highest buy price.
        If no orders meet the criteria, return None.
        """
        trade = None
        for _order in self._orders:
            if order.is_buy != _order.is_buy:
                if order.is_buy and order.price >= _order.price:
                    if trade is None or _order.price < trade.price:
                        trade = _order
                elif not order.is_buy and order.price <= _order.price:
                    if trade is None or _order.price > trade.price:
                        trade = _order
        return trade


def parse(order_book: OrderBook) -> None:
    while True:
        line = input().strip().split()
        if line[0] == "end":
            break

        action, qty, price = line
        order_book.add(Order(action == "buy", int(qty), float(price)))


with OrderBook() as order_book:
    parse(order_book)
    order_book.add(Order(True, 10, 11.0))
