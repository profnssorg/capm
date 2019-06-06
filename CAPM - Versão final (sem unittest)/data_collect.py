from sgs import SGS
from yahoofinancials import YahooFinancials

YFMarketReturn = ['^BVSP']
RiskFree = SGS()

# Collecting Tickers Historical Data

Period = 'daily'
Start_Date = '2000-01-01'
End_Date = '2019-03-01'

RF_Start_Date = '01/01/2000'
RF_End_Date = '01/03/2019'
RF_Code = 12

# Functions for collecting Tickers and Market Return data

def Get_Tickers(T):

    YF_Tickers = YahooFinancials(T)
    YF_Tickers_Hist = YF_Tickers.get_historical_price_data(Start_Date,End_Date,Period)

    return YF_Tickers_Hist  ## Returns a JSON file

def Get_MarketReturn(MR):

    YF_MarketReturn = YahooFinancials(MR)
    YF_MarketReturn_Hist = YF_MarketReturn.get_historical_price_data(Start_Date,End_Date,Period)

    return YF_MarketReturn_Hist ## Returns a JSON file

# Function for collecting Risk-Free Rate data

def Get_RiskFree():

    YF_RiskFree_Hist = RiskFree.get_valores_series(12,RF_Start_Date,RF_End_Date)

    return YF_RiskFree_Hist
