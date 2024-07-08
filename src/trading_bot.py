import logging

logger = logging.getLogger(__name__)

class TradingBot:
    def __init__(self, market_data, strategy, broker, risk_manager, monitor):
        self.market_data = market_data
        self.strategy = strategy
        self.broker = broker
        self.risk_manager = risk_manager
        self.monitor = monitor

    def run(self, symbol: str, quantity: int):
        price = self.market_data.get_price(symbol)
        signal = self.strategy.generate_signal(self.market_data, symbol)
        if signal != "HOLD" and self.risk_manager.can_place_order(symbol, quantity, price):
            self.broker.place_order(symbol, quantity, signal)
            self.monitor.log_trade(symbol, quantity, signal, price)
        else:
            logger.warning(f"Cannot place order for {symbol}, risk limits exceeded or HOLD signal")
