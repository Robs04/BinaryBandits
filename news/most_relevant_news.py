import requests #pip install requests
from newsapi import NewsApiClient # pip install newsapi-python
import sys
import os

# Move one layer out and enter the 'api' folder
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))  # Move one level up
api_dir = os.path.join(parent_dir, "api")  # Enter 'api' folder

sys.path.append(api_dir)  # Add to system path

from sampleData import *
import re

def get_response_asking_query(query:str):
    url = ("https://idchat-api-containerapp01-dev.orangepebble-16234c4b."
           f"switzerlandnorth.azurecontainerapps.io//query?query={query}")

    response = requests.post(url)
    return response.json()

def get_response_asking_llm(query:str):
    url = ("https://idchat-api-containerapp01-dev.orangepebble-16234c4b."
           f"switzerlandnorth.azurecontainerapps.io/llm?query={query}")

    response = requests.post(url)
    return response.json()

def ask_for_company_information(company:str):
       response = get_response_asking_query(f"give me some information about {company}")
       ai_content = next((msg["content"] for msg in response["messages"] if msg["type"] == "ai" and msg["content"]), None)
       print(ai_content)
       
def ask_for_performance(company):
       response = get_response_asking_query(f"performance of {company} in last 2 days just give me a number")
       return get_final_answer(response) # get final answer -> last content section

def get_top_changes():
       response = get_response_asking_query("give me 30 large companies that had the most increase in the last 3 months")
       final_response = get_final_answer(response)
       # print(final_response)
       # Define a regex pattern to match the company names in the numbered list format
       pattern = r'\*\*([^*]+)\*\*'
    
       # Find all matches in the text
       companies = re.findall(pattern, final_response)

       return companies

def get_flop_changes():
       response = get_response_asking_query("give me 30 large companies that had the most loss in the last 3 months")
       final_response = get_final_answer(response)
       # print(final_response)
       # Define a regex pattern to match the company names in the numbered list format
       pattern = r'\*\*([^*]+)\*\*'
    
       # Find all matches in the text
       companies = re.findall(pattern, final_response)

       return companies

def get_final_answer(response):
       return response['messages'][-1]['content'] # get final answer -> last content section

def get_headlines_by_keyword(keyword):
    newsapi = NewsApiClient(api_key='2aac7014a830484b9783715817fab03a')
    top_headlines = newsapi.get_top_headlines(q=keyword)
    
    # Extract titles, URLs, and image URLs as a dictionary
    title_data_map = prepare_news(top_headlines)
    return title_data_map  # Return the dictionary
              
def get_everything_by_keyWord(keyword):
       newsapi = NewsApiClient(api_key='2aac7014a830484b9783715817fab03a')
       news = newsapi.get_everything(q=keyword)
       title_data_map = prepare_news(news)
       return title_data_map  # Return the dictionary if needed elsewhere
              
def prepare_news(news):
       return {
        article["title"]: {"url": article["url"], "image": article["urlToImage"]}
        for article in news["articles"]
        if "title" in article and "url" in article and "urlToImage" in article
       }

hardcode_news = ['Cicor Technologie N', 'ams-OSRAM Br', 'Helvetia Hldg Rg']


def find_most_relevant_news_for_list_of_stocks(stocks):
       max_changes = get_top_changes() + get_flop_changes()
       # 2. check which stocks of these comps. are hold by the user
       important_hold_by_customer = []
       for stock in stocks:
              if stock in max_changes:
                      # 3. check if there are some important news to filter out tiny companies
                     #if len(get_everything_by_keyWord(stock)) >= 1:
                     if stock in hardcode_news: # hardcode solution
                            important_hold_by_customer.append(stock)              
       # 4. prepare for html
       return important_hold_by_customer
#print(find_most_relevant_news_for_list_of_stocks(['Bellevue Group N', 'Swissquote Grp Hl N', 'DocMorris N', 'Ascom Hldg N', 'The Swatch Grp Rg', 'The Swatch Grp Br', 'medmix Rg', 'Daetwyler Hldg I', 'CieFinRichemont N', 'Leonteq N', 'Evolva Hldg Rg', 'Sw Steel Hldg Rg', 'HOCN N', 'PIERER Mobility Br', 'Meyer Burger Rg', 'RELIEF THER Hlg Rg', 'APG SGA N', 'Kudelski P', 'StarragTornosGr N', 'Carlo Gavazzi Rg']))
print(find_most_relevant_news_for_list_of_stocks(['HOCN N', 'Cicor Technologie N', 'ams-OSRAM Br', 'Sensirion H Rg-144A', 'Implenia N', 'Medartis Hl Rg-Unty', 'Adecco Group N', 'medmix Rg', 'Montana Aer Rg-Unty', 'V-ZUG Hldg Rg', 'mobilezone hldg N', 'Zwahlen et Mayr P', 'Santhera Pharm H Rg', 'Sulzer N', 'ARYZTA N', 'Roche Hldg I', 'Helvetia Hldg Rg', 'Roche Hldg DR', 'CieFinRichemont N', 'Nestle N', 'Evolva Hldg Rg', 'Cembra Money Bk N', 'Interroll Hldg N', 'Bucher Industries N', 'Medacta Grp Rg-Unty', 'OC Oerlikon N', 'Lindt&Spruengli PS', 'Lindt & Sp 2L PC Br', 'Basilea Pharmaceu N', 'ALSO Holding N']))