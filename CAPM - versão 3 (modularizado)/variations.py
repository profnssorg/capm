import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from yahoofinancials import YahooFinancials
import statsmodels.api as sm

# Calculando a variação diária das variáveis

def mk_change(hist_mk_c):

    from main import mk_result

    IBOV_retorno_diario = hist_mk_c.pct_change(1)
    IBOV_retorno_diario_l = IBOV_retorno_diario.dropna(axis=0)

    return IBOV_retorno_diario_l

def tkr_change(hist_tkr_c):

    from main import tkr_result

    USI_retorno_diario = hist_tkr_c.pct_change(1)
    USI_retorno_diario_l = USI_retorno_diario.dropna(axis=0)

    return USI_retorno_diario_l
