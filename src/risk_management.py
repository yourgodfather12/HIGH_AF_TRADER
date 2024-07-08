import logging

logger = logging.getLogger(__name__)

class RiskManager:
    def __init__(self, max_position_size: int, max_risk: float):
        self.max_position_size = max_position_size
        self.max_risk = max_risk
        self.current_positions = {}
        self.account_balance = 1000000

    def can_place_order(self, symbol: str, quantity: int, price: float) -> bool:
        if symbol not in self.current_positions:
            self.current_positions[symbol] = 0
        potential_position_size = self.current_positions[symbol] + (quantity * price)
        if potential_position_size <= self.max_position_size and (potential_position_size / self.account_balance) <= self.max_risk:
            self.current_positions[symbol] += quantity * price
            return True
        return False
