from datetime import datetime
from models import *

# Sample trades (stocks and options)
trade1 = Trade(datetime(2024, 1, 10), "AAPL", 10, 150.0, "buy", 2.5)
trade2 = Trade(datetime(2024, 2, 5), "TSLA", 5, 800.0, "buy", 5.0)
trade3 = Trade(datetime(2024, 3, 15), "MSFT", 8, 280.0, "sell", 3.0)
trade4 = Trade(datetime(2024, 2, 28), "GOOGL", 15, 140.0, "buy", 4.0)
trade5 = Trade(datetime(2024, 3, 12), "AMZN", 7, 3300.0, "buy", 8.0)

# Sample options trades
option_trade1 = Trade(datetime(2024, 1, 20), "AAPL 150C", 2, 5.50, "buy", 1.0)  # AAPL Call Option
option_trade2 = Trade(datetime(2024, 2, 15), "TSLA 750P", 1, 20.00, "buy", 2.0)  # TSLA Put Option
option_trade3 = Trade(datetime(2024, 3, 5), "MSFT 290C", 3, 7.25, "sell", 1.5)  # MSFT Call Option
option_trade4 = Trade(datetime(2024, 3, 10), "GOOGL 145P", 2, 6.80, "buy", 1.2)  # GOOGL Put Option
option_trade5 = Trade(datetime(2024, 3, 18), "AMZN 3400C", 1, 15.00, "sell", 2.0)  # AMZN Call Option

# Sample positions (stocks & options)
position1 = Position("Apple Inc.", "AAPL", 10, 150.0, 1550.0)
position2 = Position("Tesla Inc.", "TSLA", 5, 800.0, 4200.0)
position3 = Position("Microsoft Corp.", "MSFT", 8, 280.0, 2300.0)
position4 = Position("Alphabet Inc.", "GOOGL", 15, 140.0, 2200.0)
position5 = Position("Amazon.com Inc.", "AMZN", 7, 3300.0, 24000.0)

option_position1 = Position("Apple Call Option", "AAPL 150C", 2, 5.50, 1100.0)
option_position2 = Position("Tesla Put Option", "TSLA 750P", 1, 20.00, 1800.0)
option_position3 = Position("Microsoft Call Option", "MSFT 290C", 3, 7.25, 2100.0)
option_position4 = Position("Alphabet Put Option", "GOOGL 145P", 2, 6.80, 1300.0)
option_position5 = Position("Amazon Call Option", "AMZN 3400C", 1, 15.00, 1500.0)

# Sample trade histories
trade_history1 = TradeHistory([trade1, trade3, option_trade1])
trade_history2 = TradeHistory([trade2, trade4, option_trade2])
trade_history3 = TradeHistory([trade5, trade1, option_trade3])
trade_history4 = TradeHistory([trade3, trade4, option_trade4])
trade_history5 = TradeHistory([trade2, trade5, option_trade5])

# Sample goals
goals1 = Goals(["Retire at 50", "Achieve $1M portfolio"])
goals2 = Goals(["Generate passive income", "Invest in tech stocks"])
goals3 = Goals(["Diversify holdings", "Trade options successfully"])
goals4 = Goals(["Trade full-time", "Invest in dividend stocks"])
goals5 = Goals(["Build a long-term portfolio", "Grow net worth to $500K"])

# Sample positions
positions1 = Positions([position1, position2, option_position1])
positions2 = Positions([position3, position4, option_position2])
positions3 = Positions([position5, position1, option_position3])
positions4 = Positions([position2, position3, option_position4])
positions5 = Positions([position4, position5, option_position5])

# Creating Person instances
person1 = Person("John", "Doe", 250000, trade_history1, goals1, positions1)
person2 = Person("Alice", "Smith", 150000, trade_history2, goals2, positions2)
person3 = Person("Bob", "Johnson", 500000, trade_history3, goals3, positions3)
person4 = Person("Emma", "Brown", 300000, trade_history4, goals4, positions4)
person5 = Person("Charlie", "Davis", 200000, trade_history5, goals5, positions5)

# Store persons in a list
people = [person1, person2, person3, person4, person5]

# Print sample data
for person in people:
    print(f"Name: {person.first_name} {person.last_name}")
    print(f"Net Worth: ${person.current_worth}")
    print("Trade History:")
    for trade in person.trade_history.trades:
        print(f"  {trade.date.date()} - {trade.trade_type.upper()} {trade.amount} {trade.asset} at ${trade.price}")
    print("Goals:", ", ".join(person.goals.goals_list))
    print("Positions:")
    for pos in person.positions.holdings:
        print(f"  {pos.company} ({pos.ticker}) - {pos.amount} units, Worth: ${pos.current_worth}")
    print("-" * 50)
