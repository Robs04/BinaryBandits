class Person:
    def __init__(self, first_name, last_name, current_worth, trade_history, goals, positions):
        self.first_name = first_name
        self.last_name = last_name
        self.current_worth = current_worth
        self.trade_history = trade_history  # Instance of TradeHistory
        self.goals = goals  # Instance of Goals
        self.positions = positions  # Instance of Positions

class Trade:
    def __init__(self, date, asset, amount, price, trade_type, fees=0.0):
        self.date = date  # Trade date
        self.asset = asset  # Stock, crypto, forex, etc.
        self.amount = amount  # Number of shares/units
        self.price = price  # Price per unit
        self.trade_type = trade_type  # 'buy' or 'sell'
        self.fees = fees  # Transaction fees

class TradeHistory:
    def __init__(self, trades=None):
        self.trades = trades if trades else []  # List of Trade objects

    def add_trade(self, trade):
        self.trades.append(trade)

class Goals:
    def __init__(self, goals_list=None):
        self.goals_list = goals_list if goals_list else []  # List of goals

class Position:
    def __init__(self, company, ticker, amount, average_price, current_worth):
        self.company = company  # Company name
        self.ticker = ticker  # Stock symbol or asset identifier
        self.amount = amount  # Number of shares/units
        self.average_price = average_price  # Average buying price
        self.current_worth = current_worth  # Total worth of the position

class Positions:
    def __init__(self, holdings=None):
        self.holdings = holdings if holdings else []  # List of Position objects

    def add_position(self, position):
        self.holdings.append(position)
