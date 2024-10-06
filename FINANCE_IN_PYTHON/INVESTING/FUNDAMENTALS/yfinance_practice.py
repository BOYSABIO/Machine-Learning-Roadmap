import yfinance as yf
import pandas as pd
import datetime
import os
import openai

openai.api_key = os.getenv('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')
openai.api_key = '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'
openai.Model.list()


# Summarizing function
def summarize(stock_data):
    text = stock_data.get('longBusinessSummary')

    try:
        response = openai.Completion.create(model = 'gpt-3.5-turbo', prompt = text, max_tokens = 50)
    except Exception as e:
        print(f"An error occured: {str(e)}")
        return None

get_facebook_data = yf.Ticker('META').info
# print(get_facebook_data)

summarized_content = summarize(get_facebook_data)
print("Summarized Content: ")
print(summarized_content)





print('Business Summary:')
print(get_facebook_data.get("longBusinessSummary"))
