#pip install rake_nltk
#pip instal rapidfuzz
#pip install spacy
#pip install fuzzywuzzy
#pip install pandas
#pip install ace_tools


import spacy
import time
import re
from rake_nltk import Rake
import fuzzywuzzy
from rapidfuzz import process,fuzz
import requests
import pandas as pd
from parser import *
import plot



nlp = spacy.load("en_core_web_sm")
assets = {
    "nasdaq": "Nasdaq-100 ETF (QQQ)",
    "technology sector": "Technology Select Sector SPDR Fund (XLK)",
    "tech market": "Technology Select Sector SPDR Fund (XLK)",
    "energy sector": "Energy Select Sector SPDR Fund (XLE)",
    "healthcare sector": "Health Care Select Sector SPDR Fund (XLV)",
    "s&p 500": "SPDR S&P 500 ETF Trust (SPY)",
    "growth stocks": "Vanguard Growth ETF (VUG)",
    "value stocks": "Vanguard Value ETF (VTV)",
    "top tech": "APPL NVDA MSFT AVGO",
    "apple": "AAPL",
    "tesla": "TSLA",
    "nvidia": "NVDA",
    "corporate bonds": "Corporate Bonds",
    "municipal bonds": "Municipal Bonds",
    "market trends": "Market Trend Analysis"
}
low_priority_words = {"the", "market", "fund", "index", "etf", "stocks", "sector", "performance", "bonds", "review"}

time_pattern = re.compile(r"(\b\d+\s*(?:months?|years?|quarters?|days?)\b|\bq[1-4]\s\d{4}\b|\b\d{4}\b)", re.IGNORECASE)
def transform (sentence):
    doc = nlp(sentence)
    mentioned_companies = {token.text for token in doc if token.pos_ == "PROPN"}
    mentioned_context = {token.text for token in doc if token.pos_ == "ADJ"}
    mentioned_action = {token.text for token in doc if token.pos_ == "VERB"}
    mentioned_noun = {token.text for token in doc if token.pos_ == "NOUN"}
    return set.union(mentioned_action, mentioned_context, mentioned_companies,mentioned_noun)

def rake_transform(sentence):
    rake = Rake()
    rake.extract_keywords_from_text(sentence)
    keywords = rake.get_ranked_phrases()
    sorted_keywords = sorted(keywords, key= lambda phrase: sentence.index(phrase))
    print(sorted_keywords)
    
def assosciate(sentence):
    best_match, score, _  = process.extractOne(sentence, assets.keys())
    return assets[best_match] if score > 70 else "No matching index fund found"

def extract_noun_phrases(text):
    doc = nlp(text)
    noun_phrases = [
        chunk.text for chunk in doc.noun_chunks
        if chunk.root.pos_ not in {"PRON", "DET", "ADV", "INTJ"}  
    ]

    return(noun_phrases)

def extract_timestamp(text):
   
    match = time_pattern.search(text)
    if not match:
        return None, None

    time_string = match.group(0).lower()  # Normalize case

    # Extract numeric quantity and unit (e.g., "12 months" → 12, "months")
    match = re.match(r"(\d+)\s*(months?|years?|days?)", time_string)
    if match:
        quantity = int(match.group(1))
        unit = match.group(2)
        return quantity, unit

    # If it's just a year, treat it as a "year" unit
    if re.match(r"\b\d{4}\b", time_string):
        return time_string, "year"

    return None, None  

def adjust_score(match_phrase, query_phrase, base_score):
    
    match_words = set(match_phrase.lower().split())
    query_words = set(query_phrase.lower().split())

    # Count low-priority words in both match & query
    low_priority_count_match = len(match_words.intersection(low_priority_words))
    low_priority_count_query = len(query_words.intersection(low_priority_words))

    # Reduce score if generic words dominate
    adjusted_score = base_score - ((low_priority_count_match + low_priority_count_query) * 5)

    return adjusted_score

def get_best_match(phrase):
    
    # Extract timestamp and remove it from phrase
    time_quantity, time_unit = extract_timestamp(phrase)
    if not time_quantity:
        time_quantity, time_unit = 6, "Months"

    best_match = None
    best_score = 0

    # Perform fuzzy matching
    all_matches = process.extract(phrase, assets.keys(), scorer=fuzz.token_sort_ratio, limit=3)

    for match_phrase, score, _ in all_matches:
        adjusted_score = adjust_score(match_phrase, phrase, score)

        # If two matches are close, use the original score instead
        if abs(best_score - adjusted_score) < 5:
            adjusted_score = score  # Ignore penalty

        if adjusted_score > best_score:
            best_match = match_phrase
            best_score = adjusted_score

    # Get the asset name
    result = assets.get(best_match, "No relevant match found")


    # Return time component separately if found
    if time_quantity:
        return f"{result} {time_quantity} {time_unit}"

    return result

def prompt(keywords):
    match = re.search(r"(\d+)", keywords)  
    word = ""
    time_stamp = ""
    if match:
        index = match.start()
        word = keywords[:index]
        time_stamp = keywords[index:]

    prompt_string = "get" + word + "from the last" + time_stamp
    url = ("https://idchat-api-containerapp01-dev.orangepebble-16234c4b."
           f"switzerlandnorth.azurecontainerapps.io//query?query={prompt_string}")

    response = requests.post(url)
    return response.json()

def process_text(text, socketio):
    important_nouns = extract_noun_phrases(text)
    match = [(item, best) for item in important_nouns if (best := get_best_match(item)) is not None]
    for item in match: 
        if 1: #ask if you want the data
            print(item[0])
            #print(item[1])
            unlcean_json = prompt(item[1])
<<<<<<< HEAD
            clean_json = process_financial_json(extract_item_from_tool_response(unlcean_json))
            print(clean_json)
            socketio.emit('update_data', {'data': clean_json})
            #give data to front end


process_text("Tesla stock, google stock")
=======
            #print(unlcean_json)
            return  process_financial_json(extract_item_from_tool_response(unlcean_json))
>>>>>>> f49efc7dce38504226c14be3e8160c96201a9158

df = process_text("tesla")
plot.plot_stock_chart(
    df["Date"].tolist(), 
    df["Open"].tolist(), 
    df["Close"].tolist(), 
    df["High"].tolist(), 
    df["Low"].tolist()
)
