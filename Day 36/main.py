import os
import requests
from datetime import datetime, timedelta
from twilio.rest import  Client
STOCK_NAME = "PFE"
COMPANY_NAME = "Pfizer"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "HC03PLRC05KPUWYZ"
NEWS_API = "f7f00b52dc9e4ddabfce0c8e8135f3b6"


OWM=  os.environ.get("API") 
api_key = os.environ.get("API_KEY") 
account_sid = os.environ.get("") 
auth_token = os.environ.get("AUTH_TOKEN") 

client = Client(account_sid, auth_token)


news_parameters = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME
}

stock_parameters = {
   "function":"TIME_SERIES_DAILY",
    "symbol" :STOCK_NAME,
    "apikey" : STOCK_API
}

stock_request = requests.get(STOCK_ENDPOINT, stock_parameters) #why not the api key? instead
stock_data = stock_request.json()["Time Series (Daily)"] # in order to acces a particular reguster it is useful to specify after the json 

#turn the dictionary into a list thanks to list comprehension keyword

data_list = [ value for (key,value) in stock_data.items()]


yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data["4. close"]


difference = abs(float(yesterday_closing_price) - float(before_yesterday_closing_price))


diff_percentage =(difference / float(yesterday_closing_price)) * 100

if diff_percentage > 0  :
    print ("get news")

    request_news = requests.get(NEWS_ENDPOINT, news_parameters)
    articles = request_news.json()["articles"]
    

    three_articles = articles[:3]

    for article in three_articles:
        message = client.messages.create(
            body=f"Headline: {article['title']}\nSummary: {article['description']}",
            from_= "+19785950566" ,
            to="+524499903223"
        )



print(yesterday_closing_price, before_yesterday_closing_price, difference)



    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this:  NO I DONT WANT TO THANKS 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

