import json
import re
import pandas as pd

def extract_item_from_tool_response(json_data):
    """
    Extracts the 'item' field from the AI response in the 'messages' list.
    
    Args:
        json_data (dict or str): The JSON data as a dictionary or string.
    
    Returns:
        dict or str: Extracted 'item' field if found, else an error message.
    """
    # Ensure JSON is properly loaded
    if isinstance(json_data, str):
        json_data = json.loads(json_data)

    if "messages" not in json_data or not isinstance(json_data["messages"], list):
        return "Invalid JSON format: 'messages' field missing or not a list."

    # Look for a tool response message that contains "item"
    for message in json_data["messages"]:
        if message.get("type") == "tool" and "item" in message:
            return message["item"]  # Directly return the extracted item

    return "No 'item' field found in any tool response."

def process_financial_json(raw_json):
    parsed_json = json.loads(raw_json)
    nested_data = json.loads(parsed_json["data"])
    key = next(iter(nested_data))
    composite_data = json.loads(nested_data[key]) if isinstance(nested_data[key], str) else nested_data[key]
    
    return pd.DataFrame([
        {
            "Date": date,
            "Open": values["open"],
            "High": values["high"],
            "Low": values["low"],
            "Close": values["close"],
            "Total Return (%)": float(values["Total return"].strip('%')),
            "Annualized Return (%)": float(values["Anualized return"].strip('%'))
        }
        for date, values in composite_data.items()
    ])