# Importing Packages

import pandas as pd
import numpy as np

# Functions for transforming (JSON to DataFrame) and cleaning Tickers and Market Return data

def Tickers_Cleaning(Tickers):

    Tickers_df1 = pd.DataFrame(Tickers['USIM5.SA']['prices'])
    Tickers_df2 = pd.concat([Tickers_df1['adjclose']], axis = 1)
    Tickers_df3 = Tickers_df2.fillna(method = "ffill")

    return Tickers_df3

def MarketReturn_Cleaning(MarketReturn):

    MR_df1 = pd.DataFrame(MarketReturn['^BVSP']['prices'])
    MR_df2 = pd.concat([MR_df1['adjclose']], axis = 1)
    MR_df3 = MR_df2.fillna(method = "ffill")

    return MR_df3

# Function for transforming (JSON to DataFrame) and cleaning Risk-Free Rate data

def RiskFree_Cleaning(RiskFree):

    RF_df1 = pd.DataFrame(RiskFree['VALOR'])
    RF_df2 = RF_df1.fillna(method = "ffill")

    addition = pd.DataFrame([0.024620]*12)

    RF_df3 = RF_df2['VALOR'].append(addition, ignore_index = True)

    return RF_df3

# Functions for calculating variations

def Tickers_Var(Array):

    TK_Ret = np.log(Array/Array.shift(1)).dropna()
    return TK_Ret

def MarketReturn_Var(Array):

    MR_Ret = np.log(Array/Array.shift(1)).dropna()
    return MR_Ret

def RiskFree_Var(Array):

    RF_Ret = np.log(Array/Array.shift(1)).dropna()
    return RF_Ret

# Function for subtracting

def Tickers_Sub(Tickers,RiskFree):

    Tickers_Sub = np.subtract(Tickers,RiskFree)
    return Tickers_Sub

def MarketReturn_Sub(MarketReturn,RiskFree):

    MR_Sub = np.subtract(MarketReturn,RiskFree)
    return MR_Sub
