# Importação de pacotes

import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from yahoofinancials import YahooFinancials
import statsmodels.api as sm

# Obtendo dados do CDI, Ibovespa e Usiminas

CDI_l = pd.read_csv('CDI.csv')

USI = ['USIM5.SA']
IBOV = ['^BVSP']

start_date = '2000-01-01'
end_date = '2018-12-31'
period = 'daily'

IBOV_YF = YahooFinancials(IBOV)
USI_YF = YahooFinancials(USI)

IBOV_hist = IBOV_YF.get_historical_price_data(start_date, end_date, period)
USI_hist = USI_YF.get_historical_price_data(start_date, end_date, period)

# Transformando dados JSON em DataFrame & realizando limpeza de dados

import dataframe

mk_result = dataframe.cleaning_mk(IBOV_hist)
tkr_result = dataframe.cleaning_tkr(USI_hist)

# Calculando variações diárias

import variations

mk_var_result = variations.mk_change(mk_result)
tkr_var_result = variations.tkr_change(tkr_result)

# Descontando CDI e calculando CAPM por tools

import OLS

mk_subtraction = OLS.subtraction(mk_var_result)
tkr_subtraction = OLS.subtraction(tkr_var_result)

CAPM_result = OLS.CAPM_OLS(tkr_subtraction,mk_subtraction)
print(CAPM_result.summary())

#Calculando testes adicionais

CAPM_residuals = OLS.CAPM_Res(CAPM_result)

import tests

CAPM_acorr = tests.autocrr(CAPM_residuals)
print(CAPM_acorr)

CAPM_ljung = tests.ljung(CAPM_residuals)
print(CAPM_ljung)

CAPM_bp = tests.bp(CAPM_residuals,mk_var_result)
print(CAPM_bp)
