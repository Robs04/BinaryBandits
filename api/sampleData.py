from models import *
from datetime import datetime

# Swiss stocks and options trades
trade1 = Trade(datetime(2024, 1, 10), "Nestle N", 20, 108.5, "buy", 1.5)
trade2 = Trade(datetime(2024, 2, 5), "Roche Hldg I", 10, 265.0, "buy", 2.0)
trade3 = Trade(datetime(2024, 3, 15), "Cicor Technologie N", 15, 55.2, "sell", 1.8)
trade4 = Trade(datetime(2024, 2, 28), "Sulzer N", 12, 80.0, "buy", 2.5)
trade5 = Trade(datetime(2024, 3, 12), "Basilea Pharmaceu N", 25, 39.8, "buy", 2.2)

# Sample options trades on Swiss stocks
option_trade1 = Trade(datetime(2024, 1, 20), "Nestle 110C", 2, 5.80, "buy", 0.9)  # Call Option
option_trade2 = Trade(datetime(2024, 2, 15), "Roche 250P", 1, 12.50, "buy", 1.1)  # Put Option
option_trade3 = Trade(datetime(2024, 3, 5), "Cicor 60C", 3, 3.75, "sell", 0.8)  # Call Option
option_trade4 = Trade(datetime(2024, 3, 10), "Sulzer 85P", 2, 4.30, "buy", 1.3)  # Put Option
option_trade5 = Trade(datetime(2024, 3, 18), "Basilea 45C", 1, 7.00, "sell", 0.7)  # Call Option

# Sample positions in Swiss stocks and options
position1 = Position("Nestle N", "NESN.SW", 20, 108.5, 2200.0)
position2 = Position("Roche Hldg I", "ROG.SW", 10, 265.0, 2700.0)
position3 = Position("Cicor Technologie N", "CICN.SW", 15, 55.2, 800.0)
position4 = Position("Sulzer N", "SUN.SW", 12, 80.0, 970.0)
position5 = Position("Basilea Pharmaceu N", "BSLN.SW", 25, 39.8, 1050.0)

option_position1 = Position("Nestle Call Option", "Nestle 110C", 2, 5.80, 1150.0)
option_position2 = Position("Roche Put Option", "Roche 250P", 1, 12.50, 1100.0)
option_position3 = Position("Cicor Call Option", "Cicor 60C", 3, 3.75, 850.0)
option_position4 = Position("Sulzer Put Option", "Sulzer 85P", 2, 4.30, 900.0)
option_position5 = Position("Basilea Call Option", "Basilea 45C", 1, 7.00, 780.0)

# Sample trade histories
trade_history1 = TradeHistory([trade1, trade3, option_trade1])
trade_history2 = TradeHistory([trade2, trade4, option_trade2])
trade_history3 = TradeHistory([trade5, trade1, option_trade3])
trade_history4 = TradeHistory([trade3, trade4, option_trade4])
trade_history5 = TradeHistory([trade2, trade5, option_trade5])

# Sample goals
goals1 = Goals(["Retire at 50", "Achieve CHF 1M portfolio"])
goals2 = Goals(["Generate passive income", "Invest in Swiss blue chips"])
goals3 = Goals(["Diversify holdings", "Trade Swiss stock options successfully"])
goals4 = Goals(["Trade full-time", "Invest in mid-cap Swiss companies"])
goals5 = Goals(["Build a long-term portfolio", "Grow net worth to CHF 500K"])

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
'''
for person in people:
    print(f"Name: {person.first_name} {person.last_name}")
    print(f"Net Worth: CHF {person.current_worth}")
    print("Trade History:")
    for trade in person.trade_history.trades:
        print(f"  {trade.date.date()} - {trade.trade_type.upper()} {trade.amount} {trade.asset} at CHF {trade.price}")
    print("Goals:", ", ".join(person.goals.goals_list))
    print("Positions:")
    for pos in person.positions.holdings:
        print(f"  {pos.company} ({pos.ticker}) - {pos.amount} units, Worth: CHF {pos.current_worth}")
    print("-" * 50)
'''
