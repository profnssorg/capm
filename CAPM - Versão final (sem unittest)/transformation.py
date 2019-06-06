# Importing Packages

import pandas as pd
import numpy as np

# Functions for transforming (JSON to DataFrame) and cleaning Tickers and Market Return data


def Tickers_Cleaning(Tickers,Current):

    Tickers_df1 = pd.DataFrame(Tickers[Current]['prices'])

    Tickers_df1['formatted_date'] = pd.to_datetime(Tickers_df1['formatted_date'])
    Tickers_index = Tickers_df1.set_index('formatted_date')

    Tickers_df2 = Tickers_index['adjclose']
    Tickers_df3 = Tickers_df2.fillna(method = "ffill")

    return Tickers_df3

def MarketReturn_Cleaning(MarketReturn,Current2):

    MR_df1 = pd.DataFrame(MarketReturn[Current2]['prices'])

    MR_df1['formatted_date'] = pd.to_datetime(MR_df1['formatted_date'])
    MR_index = MR_df1.set_index('formatted_date')

    MR_df2 = MR_index['adjclose']
    MR_df3 = MR_df2.fillna(method = "ffill")

    return MR_df3

# Function for transforming (JSON to DataFrame) and cleaning Risk-Free Rate data

def RiskFree_Cleaning(RiskFree):

    RF_index = RiskFree.set_index('DATA')
    RF_df2 = RF_index.fillna(method = "ffill")

    return RF_df2

# Function for creating DataFrames

def ExcessTicker_DF(Tickers,RiskFree):

    ExcessTicker_df = pd.concat([Tickers,RiskFree],axis=1).dropna()
    return ExcessTicker_df

def ExcessMarket_DF(MarketReturn,RiskFree):

    ExcessMarket_df = pd.concat([MarketReturn,RiskFree],axis=1).dropna()
    return ExcessMarket_df

# Functions for calculating variations

def Tickers_Var(DataFrame):

    TK_Ret = np.log(DataFrame) - np.log(DataFrame.shift(1))
    TK_Ret = TK_Ret.dropna()
    return TK_Ret

def MarketReturn_Var(DataFrame):

    MR_Ret =  np.log(DataFrame) - np.log(DataFrame.shift(1))
    MR_Ret = MR_Ret.dropna()
    return MR_Ret

def Tickers_Sub(DataFrame):

    DataFrame['ExcessReturnTicker'] = DataFrame['adjclose'] - DataFrame['VALOR']
    ET_DF = DataFrame['ExcessReturnTicker']

    return ET_DF


def MarketReturn_Sub(DataFrame2):

    DataFrame2['ExcessReturnMarket'] = DataFrame2['adjclose'] - DataFrame2['VALOR']
    EMK_DF = DataFrame2['ExcessReturnMarket']

    return EMK_DF

def Master(ExcessTicker,ExcessReturn):

    ExcessTicker = pd.DataFrame(ExcessTicker)
    DataMaster = pd.concat([ExcessTicker,ExcessReturn],axis=1).dropna()
    return DataMaster

#Functions for unit test

def Get_Index(arg2):

    arg2['formatted_date'] = pd.to_datetime(arg2['formatted_date'])
    result = arg2['formatted_date']

    return result
