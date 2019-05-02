from yahoofinancials import YahooFinancials

# Importando variáveis

def tickers_hist_price():
    USI = ['USIM5.SA']
    IBOV = ['^BVSP']

    start_date = '2000-01-01'
    end_date = '2018-12-31'
    period = 'daily'

    IBOV_YF = YahooFinancials(IBOV)
    USI_YF = YahooFinancials(USI)

    IBOV_hist = IBOV_YF.get_historical_price_data(start_date, end_date, period)
    USI_hist = USI_YF.get_historical_price_data(start_date, end_date, period)


# Definindo parâmetros

def parameters():
    start_date = '2000-01-01'
    end_date = '2018-12-31'
    period = 'daily'

# Definindo novas variáveis e capturando histórico de preços

def historical_price():
    IBOV_YF = YahooFinancials(IBOV)
    USI_YF = YahooFinancials(USI)

    IBOV_hist = IBOV_YF.get_historical_price_data(start_date, end_date, period)
    USI_hist = USI_YF.get_historical_price_data(start_date, end_date, period)
