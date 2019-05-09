# Packages importation

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plot
import statsmodels.api as sm

# Function for calculating OLS

def CAPM_OLS(Y,X):

    Y_Tickers = Y

    X_MarketReturn = X
    X_MarketReturn_const = sm.tools.add_constant(X_MarketReturn)

    CAPM = sm.OLS(Y_Tickers,X_MarketReturn_const)
    CAPM_r = CAPM.fit()

    return CAPM_r
    return CAPM_r.resid
    return X_MarketReturn_const

# Function for getting residuals

def CAPM_Residuals(CAPM):

    CAPM_Res = CAPM.resid
    return CAPM.resid

# Functions for testing the residuals

# Correlogram

def Autocrr(residuals):

    plot.acorr(residuals, maxlags=9)

    plot.title('Autocorrelação dos resíduos do Ticker')
    plot.xlabel('Lag')
    plot.ylabel('Autocorrelação')

    plot.show()

# Ljung-Box

def LjungBox(residuals):

    LJ = sm.stats.diagnostic.acorr_ljungbox(residuals)
    print(LJ)

# Breusch-Pagan

def BreuschPagan(residuals,x_const):

    x_c = sm.tools.add_constant(x_const)
    BP = sm.stats.diagnostic.het_breuschpagan(residuals,x_c)
    print(BP)
