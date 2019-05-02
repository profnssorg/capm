import pandas as pd

def cleaning_mk(hist_mk):

    from main import IBOV_hist

    IBOV_df1 = pd.DataFrame(hist_mk['^BVSP']['prices'])
    IBOV_df2 = pd.concat([IBOV_df1['adjclose']], axis = 1)
    IBOV_df3 = IBOV_df2.fillna(method = "ffill")

    return IBOV_df3


def cleaning_tkr(hist_tkr):

    from main import USI_hist

    USI_df1 = pd.DataFrame(hist_tkr['USIM5.SA']['prices'])
    USI_df2 = pd.concat([USI_df1['adjclose']], axis = 1)
    USI_df3 = USI_df2.fillna(method = "ffill")

    return USI_df3
