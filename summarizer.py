import openai
import os

def set_api_key(key):
    openai.api_key = key

def summarize_stock(ticker, df):
    if df.empty:
        return "No data available for this ticker."

    text = f"Price summary for {ticker}:\n"
    for index, row in df.iterrows():
        date = index.strftime('%Y-%m-%d')
        text += f"- {date}: Open={row['Open']:.2f}, Close={row['Close']:.2f}, High={row['High']:.2f}, Low={row['Low']:.2f}\n"

    prompt = f"""
You are a financial analyst. Based on the following price data for stock '{ticker}' over the last week, summarize the overall price trend in a simple and clear way:
{text}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or use OpenRouter equivalent
        messages=[
            {"role": "system", "content": "You analyze stock price trends."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    return response['choices'][0]['message']['content']
