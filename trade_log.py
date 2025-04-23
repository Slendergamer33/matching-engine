def log_trade(trade, filename="trades.csv"):
    with open(filename, "a") as f:
        f.write(f"{trade['timestamp']},{trade['price']},{trade['quantity']},{trade['buy_id']},{trade['sell_id']}\n")
