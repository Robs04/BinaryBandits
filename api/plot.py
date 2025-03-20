import io
import base64
import pandas as pd
import mplfinance as mpf
from flask import Flask, jsonify
from flask_socketio import SocketIO

def generate_stock_plot(dates, opens, closes, highs, lows):
    """ Generates a stock price chart and returns it as a base64 string. """
    data = pd.DataFrame({
        'Date': pd.to_datetime(dates),
        'Open': opens,
        'Close': closes,
        'High': highs,
        'Low': lows
    })
    data.set_index('Date', inplace=True)

    fig, ax = mpf.plot(data, type='candle', style='charles', returnfig=True)
    
    img_io = io.BytesIO()
    fig.savefig(img_io, format='png', bbox_inches="tight")
    img_io.seek(0)
    
    encoded_img = base64.b64encode(img_io.read()).decode('utf-8')
    return encoded_img

# Example usage
'''
dates = pd.date_range(start="2024-10-01", periods=45).strftime('%Y-%m-%d').tolist()
opens = [100 + i * 0.5 for i in range(45)]
closes = [o + (1 if i % 2 == 0 else -1) for i, o in enumerate(opens)]
highs = [c + 1.5 for c in closes]
lows = [o - 1.5 for o in opens]

plot_stock_chart(dates, opens, closes, highs, lows)
'''
