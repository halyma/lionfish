# -*- coding: utf-8 -*-
import pandas as pd
import os
import matplotlib.pyplot as plt
import tushare as ts
from jaqs.data import DataApi

if __name__ == '__main__':
    _start_date = '2014-01-01'
    _end_date = '2018-02-02'

    phone = '13706519134'
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVfdGltZSI6IjE1MTM0ODE2NTM4MTAiLCJpc3MiOiJhdXRoMCIsImlkIjoiMTM3MDY1MTkxMzQifQ.6wOPdEDGnSBwMzb3dDVp_8LPBT0UbHqnFFvCc15bL_U'

    api = DataApi("tcp://data.tushare.org:8910")
    df, msg = api.login(phone, token)

    #获取融资余额
    df1 = ts.sh_margins(start=_start_date, end=_end_date)
    df1.index = pd.to_datetime(df1.opDate)
    df1.sort_index(inplace=True)

    #获取上证日收盘价
    df_sh, msg = api.daily(symbol='000001.SH', start_date=_start_date, end_date = _end_date, fields = '', freq = '1d')
    df_sh.trade_date = pd.Series(df_sh.trade_date, index=df_sh.index, dtype=str)
    df_sh.index = pd.to_datetime(df_sh.trade_date)
    df_sh.sort_index(inplace=True)

    df_a = df1['rzye']/100000000
    df_b = df_sh['close']

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_xlabel('Daily')
    ax1.set_ylabel('Amount(^9)')
    ax1.set_title('SH RZYE & SH Index')
    ax1.plot(df_a, label='RZYE', c='r')
    ax1.legend()

    ax2 = ax1.twinx()
    ax2.set_ylabel('Price')
    ax2.plot(df_b, label='SH Index', c='b')
    plt.grid(True)
    plt.show()

