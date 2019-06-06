
############ PACKAGES IMPORTATION ###########


import data_collect as dc
import transformation as tr
import capm as cp
import pandas as pd
from sgs import SGS


########### DATA INPUT ##############


# Defining Tickers, Market Return and Risk-Free Rate for usage

Tickers = input("Enter the desired ticker (format: TICKER.SA): ")
MarketReturn = ['^BVSP']
RiskFree = SGS()

Current = Tickers
Current2 = MarketReturn[0]

# Defining Tickers, Market Return and Risk Free Rate parameters

Period = 'daily'
Start_Date = '2000-01-01'
End_Date = '2019-03-01'

RF_Start_Date = '01/01/2000'
RF_End_Date = '01/03/2019'
RF_Code = 12


########## DATA PROCESSING ##########


# Collecting Tickers, Market Return and Risk Free Rate data

Tickers = dc.Get_Tickers(Tickers)
MarketReturn = dc.Get_MarketReturn(MarketReturn)
RiskFree = dc.Get_RiskFree()

# Transforming and cleaning data

Tickers_DF = tr.Tickers_Cleaning(Tickers,Current)
MarketReturn_DF = tr.MarketReturn_Cleaning(MarketReturn,Current2)
RiskFree_DF = tr.RiskFree_Cleaning(RiskFree)

# Creating DataFrames

ExcessTicker_DF = tr.ExcessTicker_DF(Tickers_DF,RiskFree_DF)
ExcessMarket_DF = tr.ExcessMarket_DF(MarketReturn_DF,RiskFree_DF)

# Calculating daily returns

Tickers_Return = tr.Tickers_Var(ExcessTicker_DF)
MarketReturn_Return = tr.MarketReturn_Var(ExcessMarket_DF)

#  Subtracting Risk-Free Rate from both variables

Tickers_Subtracted = tr.Tickers_Sub(Tickers_Return)
MarketReturn_Subtracted = tr.MarketReturn_Sub(MarketReturn_Return)

Tickers_Subtracted = pd.DataFrame(Tickers_Subtracted)
MarketReturn_Subtracted = pd.DataFrame(MarketReturn_Subtracted)

DataMaster = tr.Master(Tickers_Subtracted,MarketReturn_Subtracted)

X = DataMaster['ExcessReturnTicker']
Y = DataMaster['ExcessReturnMarket']

# Calculating CAPM by OLS and showing results

CAPM_Result = cp.CAPM_OLS(X,Y)

########## DATA OUTPUT ###########

print(CAPM_Result.summary())

CAPM_Residuals = cp.CAPM_Residuals(CAPM_Result)

# Calculating additional tests and showing results

CAPM_LjungBox = cp.LjungBox(CAPM_Residuals)
print(CAPM_LjungBox)

#CAPM_BreuschPagan = cp.BreuschPagan(CAPM_Residuals, MarketReturn_Subtracted)
#print(CAPM_BreuschPagan)
