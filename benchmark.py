from order_book import OrderBook
import time

def run_benchmark(n=100000):
    ob = OrderBook()

    print(f"Running benchmark with {n} orders...")
    start = time.perf_counter()

    for i in range(n):
        price = 100 + (i % 5)  # Prices: 100 to 104
        qty = 10
        side = 'buy' if i % 2 == 0 else 'sell'
        ob.add_order(side, price, qty)

    end = time.perf_counter()
    elapsed = end - start

    print(f"\n✅ Benchmark complete!")
    print(f"Processed {n} orders in {elapsed:.4f} seconds")
    print(f"Trades matched: {len(ob.trades)}")
    print(f"Average speed: {n / elapsed:.0f} orders/sec")

if __name__ == "__main__":
    run_benchmark()
