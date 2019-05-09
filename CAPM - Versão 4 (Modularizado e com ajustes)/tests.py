
# Importação de pacotes

import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from yahoofinancials import YahooFinancials
import statsmodels.api as sm
from sgs import SGS

# Defining Tickers, Market Return and Risk-Free Rate for usage

Tickers = ['USIM5.SA']
MarketReturn = ['^BVSP']
RiskFree = SGS()

# Collecting Tickers Historical Data

Period = 'daily'
Start_Date = '2000-01-01'
End_Date = '2019-03-01'

RF_Start_Date = '01/01/2000'
RF_End_Date = '01/03/2019'
RF_Code = 12

from transformation import RiskFree_Cleaning

Result = RiskFree_Cleaning()
print(Result)
