import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd

def plot_stock_chart(dates, opens, closes, highs, lows, title="Stock Price Chart"):
    """
    Plots a candlestick chart for a stock over multiple days.
    Automatically scales based on the time range.

    Parameters:
        dates (list): List of dates in 'YYYY-MM-DD' format.
        opens (list): List of opening prices.
        closes (list): List of closing prices.
        highs (list): List of high prices.
        lows (list): List of low prices.
        title (str): Title of the chart.
    """
    # Convert dates to pandas datetime
    data = pd.DataFrame({
        'Date': pd.to_datetime(dates),
        'Open': opens,
        'Close': closes,
        'High': highs,
        'Low': lows
    })
    
    data.set_index('Date', inplace=True)
    
    # Determine the time range
    num_days = (data.index[-1] - data.index[0]).days

    # Define scaling options
    if num_days <= 7:
        # Very short period -> Show each day with detailed candlesticks
        style = 'charles'
        fig_size = (8, 4)
        interval = 1  # Show all labels
    elif num_days <= 30:
        # Up to one month -> Medium zoom
        style = 'yahoo'
        fig_size = (10, 5)
        interval = 2  # Show every second day
    elif num_days <= 90:
        # Up to three months -> More compact
        style = 'blueskies'
        fig_size = (12, 6)
        interval = 5  # Show every 5th day
    else:
        # 3 to 6 months -> Wide chart, fewer labels
        style = 'classic'
        fig_size = (14, 7)
        interval = 10  # Show every 10th day

    # Plot the candlestick chart
    mpf.plot(data, type='candle', style=style, figsize=fig_size, title=title, ylabel='Price')

# Example usage
'''
dates = pd.date_range(start="2024-10-01", periods=45).strftime('%Y-%m-%d').tolist()
opens = [100 + i * 0.5 for i in range(45)]
closes = [o + (1 if i % 2 == 0 else -1) for i, o in enumerate(opens)]
highs = [c + 1.5 for c in closes]
lows = [o - 1.5 for o in opens]

plot_stock_chart(dates, opens, closes, highs, lows)
'''
