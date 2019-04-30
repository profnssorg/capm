#!/usr/bin/env python
# coding: utf-8

# # Implementação computacional de um CAPM (Sharpe, 1964)

# O primeiro passo para a implementação computacional do Capital Asset Pricing Model, de William F. Sharpe (1964), é a importação de uma série de pacotes que serão utilizados durante o processo. Importaremos os seguintes pacotes: Pandas, Matplotlib, NumPy, YahooFinancials (1.5) e o StatsModels.

# In[131]:


# Importação dos pacotes

import quandl as qd
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from yahoofinancials import YahooFinancials
import statsmodels.api as sm

##import quandl as qd


# Iremos inicialmente definir duas variáveis de nosso interesse: a ação desejada (em nosso caso, a USIM5.SA) e a Taxa de Retorno do Mercado (em nosso caso, a Ibovespa). Cada variável conterá o nome do seu respectivo ticker de acordo com a plataforma Yahoo Finance. Essas variáveis serão utilizadas posteriormente para a captura de suas respectivas séries históricas utilizando o YahooFinancials.

# In[132]:


# Definindo variáveis

USI = ['USIM5.SA']
IBOV = ['^BVSP']


# Definiremos agora três novas variáveis que funcionarão como parâmetros para a função de captura das séries históricas de nosso interesse. O primeiro parâmetro (start_date) é a data de início da série histórica desejada. Seguindo a lógica, o segundo parâmetro (end_date) marca a data final da série histórica. A última variável (period) marca a frequência desejada de captura de valores.

# In[133]:


# Definindo parâmetros

start_date = '2000-01-01'  
end_date = '2018-12-31' 
period = 'daily'  


# Agora utilizaremos propriamente o pacote YahooFinancials. Definiremos, em um primeiro momento, duas novas variáveis (IBOV_YF e USI_YF) que "chamarão" o pacote utilizando as variáveis definidas anteriormente. 
# 
# Na sequência, definiremos outras duas variáveis (IBOV_hist e USI_hist) que utilizarão uma função específica do pacote (get_historical_price_data) para realizar a captura dos preços históricos das nossas variáveis utilizando os parâmetros definidos anteriormente (start_date, end_date e period).

# In[134]:


# Definindo novas variáveis e capturando histórico de preços

IBOV_YF = YahooFinancials(IBOV)
USI_YF = YahooFinancials(USI)

IBOV_hist = IBOV_YF.get_historical_price_data(start_date, end_date, period)
USI_hist = USI_YF.get_historical_price_data(start_date, end_date, period)


# Temos agora, nessas duas novas variáveis, uma série de dados sobre os preços diários da USIM5.SA e da Ibovespa. Contudo, o pacote YahooFinancials provê essas informações no formato JSON. Para podermos trabalhar com os valores obtidos, teremos de transformar os dados de JSON para DataFrame. Para tanto, utilizaremos o pacote Pandas importado no início do processo.
# 
# Duas novas variáveis (IBOV_df1 e USI_df1) serão definidas a partir do recurso DataFrame do pacote Pandas e das variáveis IBOV_hist e USI_hist (estas que contém as variáveis que desejamos). 

# In[135]:


# Utilizando a função DataFrame do pacote Pandas

IBOV_df1 = pd.DataFrame(IBOV_hist['^BVSP']['prices'])
USI_df1 = pd.DataFrame(USI_hist['USIM5.SA']['prices'])


# Podemos verificar como nossas novas variáveis estão printando-as:

# In[136]:


# Printando as variáveis

print(IBOV_df1.head())
print(USI_df1.head())


# Agora iremos criar duas variáveis (IBOV_df2 e USI_df2) utilizando apenas a coluna de nosso interesse de ambas as variáveis: a coluna "adjclose". Utilizaremos a função Concat do Pandas para tanto. Ainda, definiremos o eixo em 1.

# In[137]:


# Utilizando o Pandas para definir novas variáveis contendo os preços de fechamento

IBOV_df2 = pd.concat([IBOV_df1['adjclose']], axis = 1)
USI_df2 = pd.concat([USI_df1['adjclose']], axis = 1)


# Novamente, podemos verificar nosso trabalho printando as novas variáveis:

# In[138]:


# Printando as variáveis 

print(IBOV_df2.head())
print(USI_df2.head())


# Até agora tudo está conforme gostaríamos.
# 
# O próximo passo é calcular a variação diária das variáveis. Utilizaremos a função "pct_change" do pacote Pandas para obtermos a variação diária de ambas as variáveis (variável "retorno_mensal") e excluiremos a primeira linha dessa variável utilizando o "dropna".
# 
# Também podemos printar ambas as variáveis para conferência.

# In[139]:


# Calculando a variação diária das variáveis

IBOV_retorno_diario = IBOV_df2.pct_change(1) 
IBOV_retorno_diario_l = IBOV_retorno_diario.dropna(axis=0)

USI_retorno_diario = USI_df2.pct_change(1) 
USI_retorno_diario_l = USI_retorno_diario.dropna(axis=0)

print(IBOV_retorno_diario_l.head())
print(USI_retorno_diario_l.head())


# Finalmente, poderemos realizar a regressão por MQO das variáveis visando encontrar o Beta de mercado utilizando o pacote StatsModels.
# 
# Definiremos os retornos diários da USIM5.S.A como Y_USI (variável dependente) e os retornos diários do Ibovespa como X_IBOV (variavel independente). Ainda, adicionaremos uma constante de regressão (Alfa de Jensen) à variável independente, que será estatisticamente testada.

# In[140]:


# Definindo variável dependente e independente

Y_USI = USI_retorno_diario_l
X_IBOV = IBOV_retorno_diario_l

Xa = sm.tools.add_constant(X_IBOV)


# Definiremos uma nova variável chamada CAPM. Essa variável será a responsável pela regressão por MQO entre a variável dependente e independente definidas anteriormente. A regressão será feita pela função OLS do pacote StatsModels. O resultado da regressão, bem como os principais testes, serão apresentados atráves do print da função Summary. 
# 
# 

# In[141]:


# Regredindo as variáveis

CAPM = sm.OLS(Y_USI,Xa)
CAPM_r = CAPM.fit()
print(CAPM_r.summary())


# O sumário da regressão apresenta alguns resultados importância sobre a significância estatística do modelo, tais como: R-quadrado padrão e ajustado, a estatística F e sua probabilidade, os valores de Alfa e Beta e seus respectivos desvios padrões e estatísticas t (além de seus p-valores)e os testes de Durbin-Watson e Jarque-Bera.
# 
# Contudo, alguns testes adicionais são bem-vindos para verificar a significância do modelo. Esses testes fazem uso dos resíduos da regressão, que podem ser obtidos através da função Resid do StatsModels. Definiremos então uma nova variável "Res" contendo os resíduos de interesse.

# In[142]:


# Obtendo os resíduos do modelo

Res = CAPM_r.resid


# O primeiro passo interessante é plotar um Autocorrelograma dos resíduos da regressão. Faremos isso utilizando o pacote Matplotlib:

# In[143]:


# Plotando um Autocorrelograma dos Resíduos da regressão

plot.acorr(Res, maxlags=9)

plot.title('Autocorrelação dos resíduos de Usiminas')
plot.xlabel('Lag')
plot.ylabel('Autocorrelação')

plot.show()


# Também podemos utilizar o pacote StatsModels para testarmos a autocorrelação dos resíduos da regressão obtida através do Teste de Ljung-Box. 

# In[144]:


# Teste Ljung-Box de Autocorrelação de Resíduos

LJ = sm.stats.diagnostic.acorr_ljungbox(Res)
print(LJ)


# Por fim, podemos detectar a presença de heteroscedasticidade no modelo através do Teste de Breusch-Pagan. O pacote StatsModels também permite realizar o teste:

# In[145]:


# Teste Breusch-Pagan de Heteroscedasticidade

BP = sm.stats.diagnostic.het_breuschpagan(Res,Xa)
print(BP)


# In[ ]:




