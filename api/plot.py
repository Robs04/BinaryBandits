import json
import pandas as pd
import mplfinance as mpf
import io
import base64

def generate_stock_plot_from_json(json_text,socketio,title):
    """Takes a JSON string with numbered keys, maps them to meaningful names, generates a stock price chart, and returns it as a base64-encoded image."""
    
    # Parse the JSON text
    stock_data = json.loads(json_text)

    # Define the correct column mapping
    column_mapping = {
        "0": "Date",   # Timestamp
        "1": "Open",   # Opening price
        "2": "Close",  # Closing price
        "3": "High",   # Highest price
        "4": "Low"     # Lowest price
    }

    # Convert list of numbered dicts into DataFrame with correct column names
    df = pd.DataFrame(stock_data)
    df.rename(columns=column_mapping, inplace=True)

    # Ensure 'Date' column is in datetime format
    df["Date"] = pd.to_datetime(df["Date"])

    # Set 'Date' as the index for mplfinance
    df.set_index("Date", inplace=True)

    # Debugging: Print column names and first few rows
    print(title, df.columns)
    print(df.head())
    # Generate the candlestick chart
    fig, ax = mpf.plot(df, type='candle', style='charles', returnfig=True)
    ax[0].set_title(title)

    # Save the plot to a BytesIO buffer
    img_io = io.BytesIO()
    fig.savefig(img_io, format="png", bbox_inches="tight")
    img_io.seek(0)

    # Convert image to base64 string
    encoded_img = base64.b64encode(img_io.read()).decode("utf-8")
    socketio.emit('update_data', {'data': encoded_img})
    return encoded_img
