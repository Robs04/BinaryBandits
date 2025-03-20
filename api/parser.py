import json
import re
import pandas as pd

def extract_item_from_tool_response(json_data):
    if isinstance(json_data, str):
        json_data = json.loads(json_data)

    if "messages" not in json_data or not isinstance(json_data["messages"], list):
        return "Invalid JSON format: 'messages' field missing or not a list."

    # First, check if there's a tool response containing 'item'
    for message in json_data["messages"]:
        if message.get("type") == "tool" and "item" in message:
            return message["item"]  # Directly return the extracted item

    # If no direct tool response, check for function calls in 'ai' messages
    for message in json_data["messages"]:
        if message.get("type") == "ai" and "additional_kwargs" in message:
            tool_calls = message["additional_kwargs"].get("tool_calls", [])
            if isinstance(tool_calls, list):
                for call in tool_calls:
                    if call.get("type") == "function" and "function" in call:
                        try:
                            # Extract and parse function arguments
                            args = json.loads(call["function"].get("arguments", "{}"))
                            return args  # Return parsed arguments
                        except json.JSONDecodeError:
                            return "Invalid JSON format in function arguments."

    return "No valid 'item' or tool response found."

def process_financial_json(raw_json):
    parsed_json = json.loads(raw_json)
    nested_data = json.loads(parsed_json["data"])
    key = next(iter(nested_data))
    composite_data = nested_data[key]

    if isinstance(composite_data, str):
        composite_data = json.loads(composite_data)

    def extract_values(item):
        date, values = item
        return (
            date,
            values["open"],
            values["high"],
            values["low"],
            values["close"],
        )
    df = pd.DataFrame(map(extract_values, composite_data.items()))
    return df.to_json(orient="records", date_format="iso")