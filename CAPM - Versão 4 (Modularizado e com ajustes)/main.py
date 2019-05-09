# Packages importation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import statsmodels.api as sm
from yahoofinancials import YahooFinancials
from sgs import SGS

# Defining Tickers, Market Return and Risk-Free Rate for usage

Tickers = ['USIM5.SA']
MarketReturn = ['^BVSP']
RiskFree = SGS()

# Defining Tickers, Market Return and Risk Free Rate parameters

Period = 'daily'
Start_Date = '2000-01-01'
End_Date = '2019-03-01'

RF_Start_Date = '01/01/2000'
RF_End_Date = '01/03/2019'
RF_Code = 12

# Collecting Tickers, Market Return and Risk Free Rate data

from data_collect import Get_Tickers
from data_collect import Get_MarketReturn
from data_collect import Get_RiskFree

Tickers = Get_Tickers(Tickers)
MarketReturn = Get_MarketReturn(MarketReturn)
RiskFree = Get_RiskFree()

# Transforming and cleaning data

from transformation import Tickers_Cleaning
from transformation import MarketReturn_Cleaning
from transformation import RiskFree_Cleaning

Tickers_Array = Tickers_Cleaning(Tickers)
MarketReturn_Array = MarketReturn_Cleaning(MarketReturn)
RiskFree_Array = RiskFree_Cleaning(RiskFree)

# Calculating daily returns

from transformation import Tickers_Var
from transformation import MarketReturn_Var

Tickers_Return = Tickers_Var(Tickers_Array)
MarketReturn_Return = MarketReturn_Var(MarketReturn_Array)

#  Subtracting Risk-Free Rate from both variables

from transformation import Tickers_Sub
from transformation import MarketReturn_Sub

Tickers_Subtracted = Tickers_Sub(Tickers_Return,RiskFree_Array)
MarketReturn_Subtracted = MarketReturn_Sub(MarketReturn_Return,RiskFree_Array)

# Calculating CAPM by OLS and showing results

from capm import CAPM_OLS
from capm import CAPM_Residuals

CAPM_Result = CAPM_OLS(Tickers_Subtracted,MarketReturn_Subtracted)
print(CAPM_Result.summary())

CAPM_Residuals = CAPM_Residuals(CAPM_Result)

# Calculating additional tests and showing results

from capm import Autocrr
from capm import LjungBox
from capm import BreuschPagan

CAPM_Autocorrelogram = Autocrr(CAPM_Residuals)
print(CAPM_Autocorrelogram)

CAPM_LjungBox = LjungBox(CAPM_Residuals)
print(CAPM_LjungBox)

CAPM_BreuschPagan = BreuschPagan(CAPM_Residuals, MarketReturn_Subtracted)
print(CAPM_BreuschPagan)
