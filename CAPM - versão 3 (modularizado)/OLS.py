import numpy as np
import statsmodels.api as sm
from main import CDI_l

# Descontando IBOV e USI pelo CDI

def subtraction(mk_var_result):

    IBOV_rd_descontado = np.subtract(mk_var_result, CDI_l)

    return IBOV_rd_descontado

def subtraction(tkr_var_result):

    USI_rd_descontado = np.subtract(tkr_var_result, CDI_l)

    return USI_rd_descontado

# Definindo variável dependente e independente

def CAPM_OLS(Y,X):
    Y_CAPM = Y

    X_CAPM = X
    X_CAPM_const = sm.tools.add_constant(X_CAPM)

    CAPM = sm.OLS(Y_CAPM,X_CAPM_const)
    CAPM_r = CAPM.fit()

    return CAPM_r
    return CAPM_r.resid
    return X_CAPM_const

def CAPM_Res(CAPM_proxy):

    CAPM_Res = CAPM_proxy.resid
    return CAPM_proxy.resid
