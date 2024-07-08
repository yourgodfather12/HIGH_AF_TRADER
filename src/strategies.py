from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

class Strategy(ABC):
    @abstractmethod
    def generate_signal(self, market_data, symbol: str) -> str:
        pass

class MomentumStrategy(Strategy):
    def __init__(self):
        self.previous_price = None

    def generate_signal(self, market_data, symbol: str) -> str:
        current_price = market_data.get_price(symbol)
        signal = "HOLD"
        if self.previous_price:
            if current_price > self.previous_price:
                signal = "BUY"
            elif current_price < self.previous_price:
                signal = "SELL"
        self.previous_price = current_price
        logger.info(f"Generated signal: {signal} at price {current_price}")
        return signal
