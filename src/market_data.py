import websocket
import json
import threading
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class MarketData(ABC):
    @abstractmethod
    def get_price(self, symbol: str) -> float:
        pass

class CryptoMarketData(MarketData):
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.price = 0.0
        self.ws_url = f"wss://api.exchange.com/ws/{symbol}"
        self.ws = None
        self.connect()

    def connect(self):
        self.ws = websocket.WebSocketApp(self.ws_url,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        thread = threading.Thread(target=self.ws.run_forever)
        thread.daemon = True
        thread.start()

    def on_message(self, ws, message: str):
        data = json.loads(message)
        self.price = float(data['price'])

    def on_error(self, ws, error):
        logger.error(f"WebSocket error: {error}")
        self.connect()

    def on_close(self, ws, close_status_code, close_msg):
        logger.info("WebSocket closed")
        self.connect()

    def get_price(self, symbol: str) -> float:
        return self.price
