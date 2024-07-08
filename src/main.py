from market_data import CryptoMarketData
from strategies import MomentumStrategy
from broker import RealBroker, SimulatedBroker
from risk_management import RiskManager
from monitoring import Monitoring
from trading_bot import TradingBot
import logging
import time

def main():
    logging.basicConfig(level=logging.INFO)
    market_data = CryptoMarketData("BTC-USD")
    strategy = MomentumStrategy()
    # Use RealBroker for real trading, SimulatedBroker for testing
    broker = RealBroker(api_key="your_real_api_key_here")
    # broker = SimulatedBroker()
    risk_manager = RiskManager(max_position_size=50000, max_risk=0.1)
    monitor = Monitoring()

    bot = TradingBot(market_data, strategy, broker, risk_manager, monitor)

    while True:
        bot.run("BTC-USD", 1)
        time.sleep(1)

if __name__ == "__main__":
    main()
