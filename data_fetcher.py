import yfinance as yf
import datetime

def get_last_week_data(ticker):
    end_date = datetime.datetime.today()
    start_date = end_date - datetime.timedelta(days=7)
    df = yf.download(ticker, start=start_date, end=end_date)
    return df.tail(7)  # Return recent 7 rows
