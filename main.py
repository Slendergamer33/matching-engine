from order_book import OrderBook

# Create the order book
ob = OrderBook()

# Add some test orders
ob.add_order('buy', 101, 10)    # Buy 10 @ 101
ob.add_order('sell', 100, 5)    # Sell 5 @ 100 — should match!
ob.add_order('sell', 101, 10)   # Sell 10 @ 101 — should match!
ob.add_order('buy', 102, 15)    # Buy 15 @ 102
ob.add_order('sell', 103, 20)   # Sell 20 @ 103 — should not match yet
ob.add_order('buy', 99, 5)     # Buy 5 @ 99 — should not match yet
ob.add_order('sell', 98, 10)    # Sell 10 @ 98 — should not match yet
ob.add_order('buy', 100, 5)     # Buy 5 @ 100 — should match with the sell order at 100
ob.add_order('sell', 102, 5)    # Sell 5 @ 102 — should match with the buy order at 102
ob.add_order('buy', 101, 5)     # Buy 5 @ 101 — should match with the sell order at 101
ob.add_order('sell', 100, 10)   # Sell 10 @ 100 — should match with the buy order at 100

# Print out the trades that happened
print("\nMatched Trades:")
for trade in ob.trades:
    print(trade)
