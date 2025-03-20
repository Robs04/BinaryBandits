from models import *
from datetime import datetime

from datetime import datetime

# Define stock sectors with Swiss stocks
SECTORS = {
    "Technology": ["ams-OSRAM Br", "Cicor Technologie N", "Sensirion H Rg-144A", "ALSO Holding N"],
    "Healthcare": ["Roche Hldg I", "Basilea Pharmaceu N", "Santhera Pharm H Rg", "Medacta Grp Rg-Unty"],
    "Financials": ["Cembra Money Bk N", "Helvetia Hldg Rg", "Adecco Group N"],
    "Industrials": ["Interroll Hldg N", "Bucher Industries N", "OC Oerlikon N", "Sulzer N", "Implenia N"],
    "Consumer Goods": ["Nestle N", "Lindt&Spruengli PS", "Lindt & Sp 2L PC Br", "CieFinRichemont N", "V-ZUG Hldg Rg"],
}

# Generate trades for each sector
def generate_trades(person_name, num_trades=20):
    trades = []
    for sector, stocks in SECTORS.items():
        for i, stock in enumerate(stocks):
            if len(trades) >= num_trades:
                break
            trade = Trade(
                date=datetime(2024, 1, i + 5),
                asset=stock,
                amount=round(50 + i * 10),  # Random amount per stock
                price=round(50 + i * 5 + (100 if sector == "Consumer Goods" else 0), 2),
                trade_type="buy" if i % 2 == 0 else "sell",
                fees=round(1 + i * 0.5, 2),
            )
            trades.append(trade)
    return trades

# Generate positions for each sector
def generate_positions():
    positions = []
    for sector, stocks in SECTORS.items():
        for i, stock in enumerate(stocks):
            position = Position(
                company=stock,
                ticker=f"{stock[:3].upper()}.SW",
                amount=round(500 + i * 20),
                average_price=round(100 + i * 10, 2),
                current_worth=round(1000000 + i * 50000, 2),
            )
            positions.append(position)
    return positions

# Create high-net-worth individuals
person1 = Person(
    "Hans", "Müller", 75_000_000,
    trade_history=TradeHistory(generate_trades("Hans")),
    goals=Goals(["Maintain capital growth", "Expand into European markets"]),
    positions=Positions(generate_positions())
)

person2 = Person(
    "Sophie", "Dupont", 62_500_000,
    trade_history=TradeHistory(generate_trades("Sophie")),
    goals=Goals(["Long-term dividend investing", "Philanthropic investments"]),
    positions=Positions(generate_positions())
)

person3 = Person(
    "Luca", "Rossi", 54_800_000,
    trade_history=TradeHistory(generate_trades("Luca")),
    goals=Goals(["Growth stocks & aggressive trading", "Sector diversification"]),
    positions=Positions(generate_positions())
)

# Store persons in a list
people = [person1, person2, person3]

# Print sample data
'''
for person in people:
    print(f"Name: {person.first_name} {person.last_name}")
    print(f"Net Worth: CHF {person.current_worth:,}")
    print("Trade History:")
    for trade in person.trade_history.trades:
        print(f"  {trade.date.date()} - {trade.trade_type.upper()} {trade.amount} {trade.asset} at CHF {trade.price}")
    print("Goals:", ", ".join(person.goals.goals_list))
    print("Positions:")
    for pos in person.positions.holdings:
        print(f"  {pos.company} ({pos.ticker}) - {pos.amount} units, Worth: CHF {pos.current_worth:,}")
    print("-" * 50)
'''
