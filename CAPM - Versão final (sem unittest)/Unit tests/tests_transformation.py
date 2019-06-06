import unittest
import transformation as tr
import data_collect as dc
import pandas as pd
from yahoofinancials import YahooFinancials

# Expected returns

Formatted_Dates = pd.to_datetime(['2019-02-18','2019-02-19','2019-02-20','2019-02-21','2019-02-22','2019-02-25','2019-02-26','2019-02-27','2019-02-28'])

Expected_Ticker = pd.DataFrame([-0.002985072592,0.02290457064,-0.01249553235,0.01322566986,-0.009902845455,-0.01597647292,-0.004504580995,0.01863638714,-0.0007388428201])
Expected_Ticker = Expected_Ticker.set_index(Formatted_Dates)
Expected_Ticker.columns = ["ExcessReturnTicker"]

Expected_MarketReturn = pd.DataFrame([-0.0104723792,0.01183518906,-0.01147259808,0.004000480844,0.009793834508,-0.006621386798,0.003726081204,-0.003037301601,-0.01786548702])
Expected_MarketReturn = Expected_MarketReturn.set_index(Formatted_Dates)
Expected_MarketReturn.columns = ["ExcessReturnMarket"]

# Program config

Ticker_Asset = 'PETR4.SA'
Ticker_MR = '^BVSP'
Ticker_RF = 12

Current = Ticker_Asset
Current2 = Ticker_MR

Period = 'daily'
Start_Date = '2019-02-15'
End_Date = '2019-03-01'

Asset =  dc.Get_Tickers(Ticker_Asset)
Market = dc.Get_MarketReturn(Ticker_MR)
RiskFree = dc.Get_RiskFree()

Tickers_DF = tr.Tickers_Cleaning(Asset,Current)
MarketReturn_DF = tr.MarketReturn_Cleaning(Market,Current2)
RiskFree_DF = tr.RiskFree_Cleaning(RiskFree)

ExcessTicker_DF = tr.ExcessTicker_DF(Tickers_DF,RiskFree_DF)
ExcessMarket_DF = tr.ExcessMarket_DF(MarketReturn_DF,RiskFree_DF)

Tickers_Return = tr.Tickers_Var(ExcessTicker_DF)
MarketReturn_Return = tr.MarketReturn_Var(ExcessMarket_DF)

Tickers_Subtracted = tr.Tickers_Sub(Tickers_Return) #retorna Series / float64
MarketReturn_Subtracted = tr.MarketReturn_Sub(MarketReturn_Return) #retorna Series / float64

class TestCalculateReturns(unittest.TestCase):

    def test_calculate_returns(self):

        Tickers_Subtracted_pd = pd.DataFrame(Tickers_Subtracted) #DataFrame
        MarketReturn_Subtracted_pd = pd.DataFrame(MarketReturn_Subtracted) #DataFrame

        self.assertEqual(Tickers_Subtracted_pd.columns[0],Expected_Ticker.columns[0])
        self.assertEqual(MarketReturn_Subtracted_pd.columns[0],Expected_MarketReturn.columns[0])

        self.assertEqual(Tickers_Subtracted_pd.dtypes[0], Expected_Ticker.dtypes[0])
        self.assertEqual(MarketReturn_Subtracted_pd.dtypes[0], MarketReturn_Subtracted.dtypes[0])



#self.assertEqual(Tickers_Subtracted,Expected_Ticker)

#self.assertGreaterEqual(stock_series_return.shape[0], 76)
        #self.assertEqual(sum([round(i-j,12) for i,j in zip(stock_series_return['PETR3'],
                                                           #expected_stock_series_returns)]), 0)
        #self.assertEqual(stock_series_return.columns[0], 'PETR3')
        #self.assertEqual(stock_series_return.index[0], '1º trimestre 2000')
        #self.assertEqual(stock_series_return.dtypes[0], 'float64')
