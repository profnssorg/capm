#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Importando Pandas, Statsmodels, Matplotlib e NumPy

import pandas as pd
import statsmodels.api as sm
import matplotlib as mt
import matplotlib.pyplot as plot
import numpy as np


# In[24]:


# Inicialização #modificar

IBOVESPA = float(0)
USI = float(0)
preco_mensal = float(0)
retorno_mensal = float(0)
retorno_mensal_l = float(0)
Y_BB = float(0)
X_IBOV = float(0)
Xa = float(0)
CAPM = float(0)
CAPM_r = float(0)


# In[25]:


# Lendo dados

IBOVESPA = pd.read_csv('^BVSP.csv', parse_dates = True, index_col = 'Date')
USI = pd.read_csv('USIM5.SA.csv',parse_dates = True, index_col = 'Date')
print(IBOVESPA.head())


# In[26]:


# Preços de fechamento 

preco_mensal = pd.concat([USI['Close'], IBOVESPA['Close']], axis=1)
preco_mensal.columns = ['USIMINAS', 'IBOVESPA']
print(preco_mensal.head())


# In[27]:


# Retornos mensais

retorno_mensal = preco_mensal.pct_change(1) #ver log em numpy
retorno_mensal_l = retorno_mensal.dropna(axis=0)
print(retorno_mensal_l.head())


# In[28]:


# Definindo variáveis

Y_USI = retorno_mensal_l['USIMINAS']
X_IBOV = retorno_mensal_l['IBOVESPA']
print(Y_USI.head(),X_IBOV.head())

Xa = sm.tools.add_constant(X_IBOV)


# In[29]:


# Modelo

CAPM = sm.OLS(Y_USI,Xa)
CAPM_r = CAPM.fit()
print(CAPM_r.summary())

Res = CAPM_r.resid


# In[36]:


# Autocorrelograma 

plot.acorr(Res, maxlags=9)

plot.title('Autocorrelação dos resíduos de Usiminas')
plot.xlabel('Lag')
plot.ylabel('Autocorrelação')

plot.show()


# In[30]:


# Teste Ljung-Box de Autocorrelação de Resíduos

LJ = sm.stats.diagnostic.acorr_ljungbox(Res)
print(LJ)


# In[31]:


# Teste Breusch-Pagan de Heteroscedasticidade

BP = sm.stats.diagnostic.het_breuschpagan(Res,Xa)
print(BP)

