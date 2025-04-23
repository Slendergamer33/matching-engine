# 🏛️ Matching Engine: A Low-Latency Order Book Simulator

This project simulates a simplified, high-performance exchange-style order book with real-time matching of buy and sell orders. It includes benchmarking, trade logging, and a modular matching engine.

## Features
- ⚡ Limit order matching using price-time priority
- ⏱️ Benchmarking: Processes 100k+ orders in seconds
- 📈 Trade logging to CSV
- 🔬 Simple heap-based order book logic
- 📦 Clean modular Python architecture

## File Overview

| File              | Purpose                          |
|-------------------|----------------------------------|
| `order.py`        | Defines order structure          |
| `order_book.py`   | Core matching engine logic       |
| `trade_log.py`    | Logs trades to file              |
| `benchmark.py`    | Performance test tool            |
| `main.py`         | Test runner / usage example      |

## Benchmark Example

```bash
python benchmark.py
