import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class Monitoring:
    def log_trade(self, symbol: str, quantity: int, order_type: str, price: float):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.info(f"{timestamp} - {order_type} {quantity} {symbol} @ {price}")
