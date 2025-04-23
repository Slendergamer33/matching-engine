import time

class Order:
    def __init__(self, order_id, side, price, quantity, timestamp=None):
        self.id = order_id
        self.side = side
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp or time.time()

        def __repr__(self):
            return f"<Order {self.side.upper()} {self.quantity} @ {self.price} (ID: {self.id})>"