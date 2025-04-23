import heapq
from trade_log import log_trade
import time  # Make sure this is also imported
from order import Order

class OrderBook:
    # creating orderbook brain when we start up the machine
    def __init__(self):
        self.bids = []
        self.asks = []
        self.trades = []
        self.order_id = 0

    def add_order(self, side, price, qty):
        self.order_id += 1
        order = Order(self.order_id, side, price, qty)
        if side == 'buy':
        # we will use -price for buy orders so the person offering the most money gets matched first
            heapq.heappush(self.bids, (-price, order.timestamp, order))
        else:
            heapq.heappush(self.asks, (price, order.timestamp, order))
        self.match_orders()
    # matching logic here, checking for deals
    def match_orders(self):
    # While there are both buy and sell orders and a match is possible
        while self.bids and self.asks and -self.bids[0][0] >= self.asks[0][0]:
        # Get the best (highest) buy and best (lowest) sell
            _, _, buy = heapq.heappop(self.bids)
            _, _, sell = heapq.heappop(self.asks)

        # Determine how much can be traded
            trade_qty = min(buy.quantity, sell.quantity)

        # Create the trade record
            trade = {
                'timestamp': time.time(),
                'price': sell.price,  # Trade occurs at seller's price
                'quantity': trade_qty,
                'buy_id': buy.id,
                'sell_id': sell.id
            }

        # Add the trade to the list
            self.trades.append(trade)

        # Optional: Save to file
            log_trade(trade)

        # If the buyer had more to buy, put the rest back in bids
            if buy.quantity > trade_qty:
                buy.quantity -= trade_qty
                heapq.heappush(self.bids, (-buy.price, buy.timestamp, buy))

        # If the seller had more to sell, put the rest back in asks
            if sell.quantity > trade_qty:
                sell.quantity -= trade_qty
                heapq.heappush(self.asks, (sell.price, sell.timestamp, sell))
