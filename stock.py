import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


class Stock:
    def stock_Price(self):
        ticker = yf.Ticker('INFY.NS').info
        market_price = ticker['regularMarketPrice']
        previous_close_price = ticker['regularMarketPreviousClose']
        print("Ticker : INFY.NS")
        print('Market Price:', market_price)
        print('Previous Close Price:', previous_close_price)

    def stock_Price_Mul(self):
        start_date = '2022-09-01'
        end_date = '2022-10-10'

        # Add multiple space separated tickers here
        ticker = 'INFY.NS'
        data = yf.download(ticker, start_date, end_date)
        print(data.tail())

        # Export data to a CSV file
        data.to_csv("Infosys.csv")

    def graph_Stock(self):
        data = pd.read_csv('Infosys.csv', delimiter=',')
        volume = data['Open']
        date = data['Date']
        plt.bar(date, volume, color='g', label="Stock")
        plt.xticks(rotation=25)
        plt.xlabel('DATE')
        plt.ylabel('STOCK')
        plt.title('INFOSYS STOCK')
        plt.legend()
        plt.show()


obj1 = Stock()
obj1.stock_Price_Mul()
obj1.graph_Stock()
