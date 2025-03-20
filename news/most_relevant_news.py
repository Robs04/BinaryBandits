import requests #pip install requests
from newsapi import NewsApiClient # pip install newsapi-python
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
       response = get_response_asking_query("give me the 5 companies that had the most change in the last two days")
       final_response = get_final_answer(response)
       # expression to extract company names from text
       company_pattern = r"\*\*(.*?)\*\*"

       # Find all matches using the regex pattern
       companies = re.findall(company_pattern, final_response)

       return companies

def get_final_answer(response):
       return response['messages'][-1]['content'] # get final answer -> last content section

def get_headlines_by_keyword(keyword):
    newsapi = NewsApiClient(api_key='2aac7014a830484b9783715817fab03a')
    top_headlines = newsapi.get_top_headlines(q=keyword)
    
    # Extract titles, URLs, and image URLs as a dictionary
    title_data_map = prepare_news(top_headlines)
    return title_data_map  # Return the dictionary if needed elsewhere
              
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

# find most relevant news for customer:
# 1. find companies that have had most change in their stock price
# 2. check which stocks of these comps. are hold by the user
# 3. find news for these companies
# 4. prepare for html
print(get_top_changes())