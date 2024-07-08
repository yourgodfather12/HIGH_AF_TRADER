import requests
import logging
from abc import ABC, abstractmethod
from datetime import datetime

logger = logging.getLogger(__name__)

class Broker(ABC):
    @abstractmethod
    def place_order(self, symbol: str, quantity: int, order_type: str):
        pass

class RealBroker(Broker):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def place_order(self, symbol: str, quantity: int, order_type: str):
        order_data = {
            "symbol": symbol,
            "quantity": quantity,
            "order_type": order_type
        }
        response = requests.post("https://api.exchange.com/orders", json=order_data, headers={"Authorization": f"Bearer {self.api_key}"})
        if response.status_code == 200:
            logger.info(f"Order placed successfully: {order_data}")
        else:
            logger.error(f"Failed to place order: {response.json()}")

class SimulatedBroker(Broker):
    def __init__(self):
        self.orders = []

    def place_order(self, symbol: str, quantity: int, order_type: str):
        self.orders.append({
            "symbol": symbol,
            "quantity": quantity,
            "order_type": order_type,
            "timestamp": datetime.now()
        })
        logger.info(f"Simulated order placed: {self.orders[-1]}")
