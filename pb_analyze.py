# -*- coding: utf-8 -*-
import time
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts

if __name__ == '__main__':
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    #overall data
    df = ts.get_stock_basics()

    overal_pb = df.pb.describe()
    overal_pe = df.pe.describe()

    df_tmp_pb_pe = df[['pb', 'pe']]

    #中证500
    df_500 = ts.get_zz500s()
    df_500.index = df_500.code
    df_new500 = pd.concat([df_500, df_tmp_pb_pe], axis=1, join='inner')

    zz500_pb = df_new500.pb.describe()
    zz500_pe = df_new500.pe.describe()

    #沪深300
    df_300 = ts.get_hs300s()
    df_300.index = df_300.code
    df_new300 = pd.concat([df_300, df_tmp_pb_pe], axis=1, join='inner')

    hs300_pb = df_new300.pb.describe()
    hs300_pe = df_new300.pe.describe()

    #上证50
    sz_50 = ts.get_sz50s()
    sz_50.index = sz_50.code
    df_new50 = pd.concat([sz_50, df_tmp_pb_pe], axis=1, join='inner')

    sz50_pb = df_new50.pb.describe()
    sz50_pe = df_new50.pe.describe()



