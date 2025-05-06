# 🧠 Trading Engine: A Multi-Strategy Backtesting and Simulation Framework

This Python project simulates a full-featured trading engine with built-in backtesting, real-time strategy evaluation, portfolio tracking, and a customizable dashboard. Designed for flexibility, it's ideal for building and testing algorithmic strategies including Bollinger Bands, Mean Reversion, Momentum Breakdown, RSI-SMA, and SMA Crossover.

---

## 🚀 Key Features

- 📊 **Multiple Built-in Strategies**: Bollinger Bands, Mean Reversion, Momentum Breakdown, RSI-SMA, and SMA Crossover  
- 🧠 **Modular Strategy Engine**: Easily plug in and test new strategies  
- 📈 **Graph Plotting**: Visualize signals, indicators, and trades on historical charts  
- 📉 **Backtesting Framework**: Simulates performance across custom timeframes  
- 💼 **Portfolio Tracker**: Monitor capital, positions, returns, and trade history  
- 🌐 **Dashboard**: Interactive interface to test and visualize strategy performance  
- ⬇️ **Data Downloader**: Fetch historical OHLCV data automatically  
- 🔄 **Strategy Comparison**: Run multiple strategies and compare side-by-side  
- 🏗️ **Clean Architecture**: Organized and extensible Python codebase  

---

## 📁 File Overview

| File/Folder        | Purpose                                                   |
|--------------------|-----------------------------------------------------------|
| `strategies/`      | Contains individual strategy implementations              |
| `engine/`          | Core logic for backtesting, matching, and trade execution |
| `dashboard.py`     | Launches an interactive dashboard (e.g., Streamlit)       |
| `plot.py`          | Handles chart plotting with indicators and trades         |
| `portfolio.py`     | Tracks equity curve, trades, and capital                  |
| `download_data.py` | Fetches historical market data from APIs                  |
| `app.py`           | Main application to run strategies and view results       |
| `main.py`          | CLI runner for tests and experiments                      |

---

## ⚡ Example Usage

```bash
# Run backtest with a selected strategy
python app.py --strategy sma_crossover --ticker BTC-USD --start 2021-01-01 --end 2023-01-01
