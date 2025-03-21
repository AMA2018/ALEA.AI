# Alea-Bot [1.0.0]

Alea-Bot is a revolutionary AI-driven crypto trading bot that combines multiple trading strategies, advanced market intelligence, and automated execution to deliver precise and profitable trading. Leveraging cutting-edge technologies such as NewsScan, Sentiment Analysis, and AI Pattern Recognition, Alea-Bot empowers both novice and professional traders to optimize their performance in the volatile crypto market.

> **Alea-Bot is under active development** and continuously integrates the latest AI innovations to redefine crypto trading.

---

## Key Features

- **AI-Driven Market Analysis**  
  Uses machine learning for real-time trend detection, predictive modeling, and dynamic risk management.

- **NewsScan Bot**  
  Automatically scans global news sources and social media to detect market-moving events, keeping you ahead of the curve.

- **Sentiment Bot**  
  Aggregates market sentiment and whale alerts, providing an extra layer of intelligence to your trading strategy.

- **AI Pattern Recognition**  
  Identifies candlestick patterns, chart formations, and hidden correlations using deep learning for precise entry and exit signals.

- **Backtesting & Optimization**  
  Test, evaluate, and refine your strategies with historical data to ensure robust performance before going live.

- **Modular Strategy Framework**  
  Create, customize, and integrate your own trading strategies seamlessly.

- **Multi-Exchange Compatibility**  
  Connect effortlessly with major crypto exchanges and DeFi protocols for smooth execution across various markets.

- **24/7 Automated Trading**  
  Operates continuously with automated order placement, stop-loss, and take-profit management.

- **Web-Based User Interface (GUI)**  
  Launch a local web server to monitor live trading performance, view interactive charts, and manage strategies through an intuitive dashboard.

---

## Installation

> **Alea-Bot requires Python 3.10** or higher.

### Using pip:
```bash
python3 -m pip install wheel appdirs==1.4.4
python3 -m pip install alea-bot
```

### Or, clone and install locally:
```bash
git clone https://github.com/AMA2018/ALEA.AI.git
cd ALEA.AI
python3 -m pip install -r requirements.txt
```

---

## Quick Start: Backtesting Example

Below is a sample RSI-based backtesting strategy that demonstrates how to leverage Alea-Bot's capabilities. This example shows how to integrate technical analysis with additional sentiment and news data to generate trade signals.

```python
import asyncio
import tulipy  # Technical Analysis library
import alea_bot as alea

async def rsi_backtest():
    async def strategy(context):
        if run_data["entries"] is None:
            closes = await alea.Close(context, max_history=True)
            times = await alea.Time(context, max_history=True, use_close_time=True)
            rsi_values = tulipy.rsi(closes, period=context.config["period"])
            offset = len(closes) - len(rsi_values)
            
            # Define entry points when RSI falls below the threshold
            run_data["entries"] = {
                times[i + offset]
                for i, rsi_val in enumerate(rsi_values)
                if rsi_val < context.config["rsi_value_buy_threshold"]
            }
            
            # Optionally, plot the RSI indicator with entry points
            await alea.plot_indicator(context, "RSI", times[offset:], rsi_values, run_data["entries"])
        
        # Execute a market order if the current time matches an entry signal
        if alea.current_live_time(context) in run_data["entries"]:
            await alea.market(
                context,
                side="buy",
                amount="10%",
                stop_loss_offset="-15%",
                take_profit_offset="25%"
            )

    config = {
        "period": 14,
        "rsi_value_buy_threshold": 30
    }

    data = await alea.get_data("BTC/USDT", "1d", start_timestamp=1505606400)
    run_data = {"entries": None}

    results = await alea.run(data, strategy, config)
    print(results.describe())
    await results.plot(show=True)
    await data.stop()

asyncio.run(rsi_backtest())
```

### Extending Your Strategy

Enhance your trading logic by integrating:
- **Sentiment Analysis**: Retrieve real-time sentiment data with `await alea.get_sentiment(context)` to refine trade decisions.
- **NewsScan Integration**: Incorporate market news via `await alea.get_news(context)` to pause or adjust trading during high-impact events.

---

## Live Trading with GUI

Alea-Bot offers a comprehensive web-based dashboard to monitor live trading. To launch live trading with the GUI:

1. **Configure Exchange API Keys**  
   Add your API credentials (e.g., Binance, Coinbase) in `config.yaml` or set them as environment variables.

2. **Launch Live Mode with GUI**  
   ```bash
   alea run --live --strategy your_strategy.py --gui
   ```
   This command starts a local web server, and you can access the dashboard at [http://localhost:8080](http://localhost:8080).

3. **Monitor Your Bot**  
   The GUI displays live performance metrics, trade logs, and interactive charts for real-time monitoring and strategy management.

*(Embed screenshots of the GUI here to showcase its features.)*

---

## Community & Support

Join our community for discussions, updates, and support:
- **Telegram**: [Alea Bot Telegram Channel](https://t.me/alea_trading_bot)
- **Discord**: [Alea Bot Discord Server](https://discord.gg/alea)
- **Twitter**: [@AleaTradingBot](https://twitter.com/AleaTradingBot)

Feel free to open issues or submit pull requests for enhancements.

---

## Contributing

We welcome community contributions! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and ensure tests pass.
4. Submit a pull request with detailed explanations.

---

## License

Alea-Bot is released under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Disclaimer

Alea-Bot employs advanced AI for automated crypto trading; however, trading carries inherent risks. Past performance does not guarantee future results. Always perform thorough research and consult professional advice before trading.

---

**Experience the Future of Crypto Trading with Alea-Bot.**  
For more detailed documentation and tutorials, visit our [official website](https://www.alea-ai.com/) or our [Wiki](https://github.com/AMA2018/ALEA.AI/wiki).