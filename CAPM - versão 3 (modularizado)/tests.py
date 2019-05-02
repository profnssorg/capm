import matplotlib.pyplot as plot
import statsmodels.api as sm

# Plotando um Autocorrelograma dos Resíduos da regressão

def autocrr(residuals):
    plot.acorr(residuals, maxlags=9)

    plot.title('Autocorrelação dos resíduos de Usiminas')
    plot.xlabel('Lag')
    plot.ylabel('Autocorrelação')

    plot.show()

# Teste Ljung-Box de Autocorrelação de Resíduos

def ljung(residuals):
    LJ = sm.stats.diagnostic.acorr_ljungbox(residuals)
    print(LJ)

# Teste Breusch-Pagan de Heteroscedasticidade

def bp(residuals,x_const):
    x_c = sm.tools.add_constant(x_const)
    BP = sm.stats.diagnostic.het_breuschpagan(residuals,x_c)
    print(BP)
