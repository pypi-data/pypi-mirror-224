#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
  @Author: uyplayer
  @Date: 2023/7/28 16:56
  @Email: uyplayer@qq.com
  @File: RSI-MFI Machine LearningV1.py
  @Software: PyCharm
  @Dir: ft_userdata / analysis/tradingview
  @Project_Name: ft_userdata
  @Description: tradingview pine script
  @ https://in.tradingview.com/script/jrjOQDgc-RSI-MFI-Machine-Learning-Manhattan-distance/
"""

# import necessary package
import pandas as pd
from pandas import DataFrame
import mplfinance as mpf
import numpy as np
import talib.abstract as ta
import math
# import test package
import pytest
import unittest

# pandas style
pd.set_option('display.width', None)
pd.options.mode.chained_assignment = None
# statistic
from scipy.spatial.distance import cdist


class RSI_MFI_ML:
    def __init__(self, timeframe, symbol, Short_Period, Long_Period, Neighbours, RegLine_size, Max_high_windows_siz,
                 Max_low_windows_siz, prediction_multiplayer, csv_file, start_time: str = "", end_time: str = ""):
        self.start_time = start_time
        self.end_time = end_time
        self.Long_Period = Long_Period
        self.Short_Period = Short_Period
        self.csv_file = csv_file
        self.prediction_multiplayer = prediction_multiplayer
        self.Max_high_windows_siz = Max_high_windows_siz
        self.Max_low_windows_siz = Max_low_windows_siz
        self.RegLine_size = RegLine_size
        self.symbol = symbol
        self.timeframe = timeframe
        self.Neighbours = Neighbours
        # data
        self.data = pd.DataFrame()
        self.df = pd.DataFrame()

    def load_data(self):
        self.data = pd.read_csv(self.csv_file)
        self.data['time'] = pd.DatetimeIndex(self.data['time'])
        self.data.set_index("time", inplace=True)
        # copy data
        columns = ['open', 'high', 'low', 'close', 'volume']
        self.df = self.data[columns].copy(deep=True)

    def __regression_calculate(self, length: int, offset: int) -> DataFrame:
        """
        regression_calculate
        :param df: dataframe
        :param length:  length
        :param offset: offset
        :return: linreg = intercept + slope * (length - 1 - offset)
        """
        # regression line
        return ta.LINEARREG_INTERCEPT(self.df['close']) + ta.LINEARREG_SLOPE(self.df['close']) * (length - 1 - offset)

    def regression_line(self):
        """
        regression line calculation
        :param df: dataframe
        :param window_size: window size
        :return: dataframe
        """
        # rolling
        data_rolling = self.df['close'].rolling(window=self.RegLine_size)
        # mean price of rolling
        avg_close = data_rolling.mean()
        x = avg_close - (self.__regression_calculate(self.RegLine_size, 0) -
                         self.__regression_calculate(self.RegLine_size, 1)) * math.floor(
            self.RegLine_size / 2) + 0.5 * (
                    self.__regression_calculate(self.RegLine_size, 0) - self.__regression_calculate(
                self.RegLine_size, 1))
        y = (avg_close - (self.__regression_calculate(self.RegLine_size, 0) -
                          self.__regression_calculate(self.RegLine_size, 1)) * math.floor(
            self.RegLine_size / 2)) + (
                    self.__regression_calculate(self.RegLine_size, 0) - self.__regression_calculate(
                self.RegLine_size, 1)) * (
                    self.RegLine_size - 1)
        # check length
        assert len(self.df) == len(x), " x data has wrong length "
        assert len(self.df) == len(y), " y data has wrong length "
        self.df['x'] = x
        self.df['y'] = y
        self.df['reg_line'] = (x + y) / 2.0

    def __trend(self):
        """
        close[4] < close[0] ? -1 : close[4] > close[0] ? 1 : 0
        current trend
        :param df:
        :return:
        """
        close = self.df['close']
        classes = np.where(close.shift(4) < close, -1, np.where(close.shift(4) > close, 1, 0))
        # check length
        assert len(self.df) == len(classes), " classes data has wrong length "
        self.df['class'] = classes


    def __mfi(self, timeperiod: int):
        """
        calculate mfi  data
        :param timeperiod: mfi length
        :param df: dataframe
        :return: dataframe
        """
        volume = self.df['volume']
        hlc3 = (self.df['high'] + self.df['low'] + self.df['close']) / 3
        rsi_a = ta.RSI(hlc3, timeperiod=timeperiod + 4)
        rsi_b = ta.RSI(hlc3, timeperiod=timeperiod + 2)
        rsi_c = ta.RSI(hlc3, timeperiod=timeperiod + 4)
        rsi_d = ta.RSI(hlc3, timeperiod=timeperiod + 5)
        mfi_a = ta.MFI(rsi_a, rsi_a, rsi_a, volume, timeperiod=timeperiod)
        mfi_b = ta.MFI(rsi_b, rsi_b, rsi_b, volume, timeperiod=timeperiod)
        mfi_c = ta.MFI(rsi_c, rsi_c, rsi_c, volume, timeperiod=timeperiod)
        mfi_d = ta.MFI(rsi_d, rsi_d, rsi_d, volume, timeperiod=timeperiod)
        avg = (mfi_a + mfi_b + mfi_c + mfi_d) / 4.0
        # check length
        assert len(self.df) == len(avg), " mfi_data data has wrong length "
        return avg

    def calculate_distance(self):
        Neighbours = math.floor(math.sqrt(self.Neighbours))
        self.df['LongData'] = self.__mfi(self.Long_Period)
        self.df['ShortData'] = self.__mfi(self.Short_Period)
        manhattan_distances = cdist(self.df[['LongData', 'ShortData']], self.df[['LongData', 'ShortData']], metric='cityblock')
        # get trend
        self.__trend()
        self.df['prediction'] = 0
        size = self.df.shape[0]
        dust = np.array([-999.0] * size)
        indices = self.df.index
        self.predictions = []
        for index in range(size):
            ManD = manhattan_distances[index][:index]
            for i in range(len(ManD)):
                if abs(ManD[i]) > dust[index]:
                    print(index, i, ManD[i], dust[index])
                    dust[index] = abs(ManD[i])
                    if len(self.predictions) > Neighbours: self.predictions.pop(0)
                    self.predictions.append(self.df['class'][indices[i]])
            self.df.at[indices[i], 'prediction'] = sum(self.predictions) * 5
        self.df['dust'] = dust
                
            # indices_greater_than_dust = np.where(ManD > dust)[0]
            # top_indices = indices_greater_than_dust[np.argsort(ManD[indices_greater_than_dust])[-Neighbours:]]
            # selected_predictions = self.df.iloc[top_indices]['class']
            # self.df.at[i, 'prediction'] = sum(selected_predictions) * 5
            # index += 1
            # dust = np.array([-999.0] * size)

    def calculate_distance1(self):
        Neighbours = math.floor(math.sqrt(self.Neighbours))
        self.df['LongData'] = self.__mfi(self.Long_Period)
        self.df['ShortData'] = self.__mfi(self.Short_Period)
        manhattan_distances = cdist(self.df[['LongData', 'ShortData']], self.df[['LongData', 'ShortData']],
                                    metric='cityblock')
        self.__trend()
        self.df['prediction'] = 0
        for i, _ in self.df.iterrows():
            ManD = manhattan_distances[i]
            predictions = []
            dust = -999.0
            for distance in ManD:
                if distance > dust:
                    dust = distance
                    if len(predictions) >= Neighbours:
                        predictions.pop(0)
                    predictions.append(self.df.iloc[i]['class'])
            self.df.at[i, 'prediction'] = sum(predictions) * 5

    def signal(self):
        self.df['signal'] = 0
        # Calculate 'C' based on prediction values
        C = ~(self.df['prediction'] > 0) & ~(self.df['prediction'] < 0)
        # Initialize 'signal' column to 0
        self.df['signal'] = 0
        # Set 'signal' to 1 if prediction is greater than 0
        self.df.loc[self.df['prediction'] > 0, 'signal'] = 1
        # Set 'signal' to -1 if prediction is less than 0
        self.df.loc[self.df['prediction'] < 0, 'signal'] = -1
        # Set 'signal' to 0 if 'C' is True
        self.df.loc[C, 'signal'] = 0

    def changed(self):
        self.df['changed'] = self.df['signal'].diff()

    def start_long_short(self):
        self.df['startLongTrade'] = self.df['changed'].astype(bool) & (self.df['signal'] == 1)
        self.df['startShortTrade'] = self.df['changed'].astype(bool) & (self.df['signal'] == -1)

    def llongsshort(self):
        self.df['LLong'] = self.df['startLongTrade'] & (self.df['close'] > self.df['reg_line'])
        self.df['SShort'] = self.df['startShortTrade'] & (self.df['close'] < self.df['reg_line'])

    def longCon_shortCon(self):
        self.df['LLong_shifted'] = self.df['LLong'].shift(1).fillna(False)
        self.df['SShort_shifted'] = self.df['SShort'].shift(1).fillna(False)
        self.df['LongCon'] = (self.df['LLong'] & ~self.df['LLong_shifted']) & (
                self.df['close'] > self.df['open'])
        self.df['ShortCon'] = (self.df['SShort'] & ~self.df['SShort_shifted']) & (
                self.df['close'] < self.df['open'])
        # delete this
        self.df.drop(['LLong_shifted', 'SShort_shifted'], axis=1, inplace=True)
        self.df['Buy'] = np.where(self.df['LongCon'], self.df['close'], np.nan)
        self.df['Sell'] = np.where(self.df['ShortCon'], self.df['close'], np.nan)

    def combine(self):
        self.df["Buy_tv"] = self.data['Buy']
        self.df["Sell_tv"] = self.data['Sell']
        self.df['reg_line_tv'] = self.data['Regline']
        self.df['LongData_tv'] = self.data['LongData']
        self.df['ShortData_tv'] = self.data['ShortData']
        self.df['class_tv'] = self.data['Class']
        self.df['prediction_tv'] = self.data['prediction']
        self.df['signal_tv'] = self.data['signal']
        self.df['signal_tv'] = self.data['signal']
        self.df['changed_tv'] = self.data['changed']
        self.df['startLongTrade_tv'] = self.data['startLongTrade']
        self.df['startShortTrade_tv'] = self.data['startShortTrade']

    def check_reg_line(self):
        reg_line = pd.DataFrame()
        reg_line['reg_line'] = self.df['reg_line']
        reg_line['reg_line_tv'] = self.df['reg_line_tv']
        reg_line['err'] = abs(reg_line['reg_line'] - reg_line['reg_line_tv'])
        print(" reg_line err : ", reg_line['err'].sum())
        print(" reg_line err mean : ", reg_line['err'].mean())
        reg_line.to_csv("data/reg_line.csv")

    def check_long_short(self):
        long_short = pd.DataFrame()
        long_short['LongData'] = self.df['LongData']
        long_short['LongData_tv'] = self.df['LongData_tv']
        long_short['LongData_err'] = abs(long_short['LongData'] - long_short['LongData_tv'])
        long_short['ShortData'] = self.df['ShortData']
        long_short['ShortData_tv'] = self.df['ShortData_tv']
        long_short['ShortData_err'] = abs(long_short['ShortData'] - long_short['ShortData_tv'])
        print(" LongData_err : ", long_short['LongData_err'].sum())
        print(" LongData_err mean : ", long_short['LongData_err'].mean())
        print(" ShortData_err : ", long_short['ShortData_err'].sum())
        print(" ShortData_err mean : ", long_short['ShortData_err'].mean())
        long_short.to_csv("data/start_long_short.csv")

    def check_class(self):
        clases = pd.DataFrame()
        clases['class'] = self.df['class']
        clases['class_tv'] = self.df['class_tv']
        clases['is_same'] = clases['class'] == clases['class_tv']
        value_counts = clases['is_same'].value_counts()
        print(" clases  error count :", value_counts[False])
        print(" clases error index : ", clases.loc[clases['is_same'] == False].index.tolist())
        clases.to_csv("data/clases.csv")

    def check_prediction(self):
        prediction = pd.DataFrame()
        prediction['prediction'] = self.df['prediction']
        prediction['prediction_tv'] = self.df['prediction_tv']
        prediction['is_same'] = prediction['prediction'] == prediction['prediction_tv']
        value_counts = prediction['is_same'].value_counts()
        print(" prediction error count :", value_counts[False])
        print(" prediction error index : ", prediction.loc[prediction['is_same'] == False].index.tolist())
        prediction.to_csv("data/prediction.csv")

    def check_signal(self):
        signal = pd.DataFrame()
        signal['signal'] = self.df['signal']
        signal['signal_tv'] = self.df['signal_tv']
        signal.to_csv("data/signal.csv")

    def check_changed(self):
        changed = pd.DataFrame()
        changed['changed'] = self.df['changed']
        changed['changed_tv'] = self.df['changed_tv']
        changed.to_csv("data/changed.csv")

    def check_start_long_short(self):
        start_long_short = pd.DataFrame()
        start_long_short['startLongTrade'] = self.df['startLongTrade']
        start_long_short['startLongTrade_tv'] = self.df['startLongTrade_tv']
        start_long_short['startShortTrade'] = self.df['startShortTrade']
        start_long_short['startShortTrade_tv'] = self.df['startShortTrade_tv']
        start_long_short.to_csv("data/start_long_short.csv")

    def plot(self):
        """
        plot
        :param dataframe:
        :return:
        """
        dataframe = self.df[(self.df['time'] >= self.start_time) & (self.df['time'] <= self.end_time)]
        dataframe = dataframe.set_index('time')
        sub_plot = [
            mpf.make_addplot((dataframe['reg_line']), color='blue', panel=0, ylabel='regression line',
                             secondary_y=False),
            mpf.make_addplot(dataframe['Buy'], color='green', type='scatter',
                             markersize=50, marker='^'),
            mpf.make_addplot(dataframe['Sell'], color='red', type='scatter',
                             markersize=50, marker='v'),
        ]
        added_plots = {"Regression line": mpf.make_addplot((dataframe['reg_line']), color='blue', panel=0),
                       "Buy": mpf.make_addplot(dataframe['Buy'], color='green', type='scatter',
                                               markersize=50, marker='^', secondary_y=False, panel=0),
                       "Sell": mpf.make_addplot(dataframe['Sell'], color='red', type='scatter',
                                                markersize=50, marker='v', secondary_y=False, panel=0),
                       }
        fig, axes = mpf.plot(dataframe,  # the dataframe containing the OHLC (Open, High, Low and Close) data
                             type='candle',  # use candlesticks
                             volume=True,  # also show the volume
                             figratio=(10, 4),  # set the ratio of the figure
                             figscale=2,
                             style='binance',  # choose the yahoo style
                             title=f'{self.timeframe} {self.symbol} Price Data and Trades',
                             addplot=list(added_plots.values()),
                             returnfig=True
                             )
        axes[0].legend([None] * (len(added_plots) + 2))
        legend_handles = axes[0].get_legend().legend_handles
        axes[0].legend(handles=legend_handles[2:], labels=list(added_plots.keys()), loc='upper left', fontsize='15')
        mpf.show()


if __name__ == "__main__":
    # short period for RSI Data Calculation
    Short_Period = 26
    # long period for RSI Data Calculation
    Long_Period = 14
    # number of neighbours for predictions
    Neighbours = 8
    # regression line calculation
    RegLine_size = 25
    # max high for highest high value
    Max_high_windows_siz = 20
    # min low for lowest low value
    Max_low_windows_siz = 20
    # predictions multiplayer
    prediction_multiplayer = 5
    # data file
    csv_file = "./advanced_ta/ManhattanDistance/BINANCE_ETHUSDT_60.csv"
    # timeframe
    timeframe = "1h"
    # symbol
    symbol = "ETHUSDT"
    start_date = '2023-07-20'
    end_date = '2023-07-30 04:30'
    rsi_mfi = RSI_MFI_ML(timeframe=timeframe, symbol=symbol, Short_Period=Short_Period, Long_Period=Long_Period,
                         Neighbours=Neighbours, RegLine_size=RegLine_size, Max_high_windows_siz=Max_high_windows_siz,
                         Max_low_windows_siz=Max_low_windows_siz, prediction_multiplayer=prediction_multiplayer,
                         csv_file=csv_file, start_time=start_date, end_time=end_date)
    rsi_mfi.load_data()
    # indicator
    rsi_mfi.regression_line()
    rsi_mfi.calculate_distance()
    rsi_mfi.signal()
    rsi_mfi.changed()
    rsi_mfi.start_long_short()
    rsi_mfi.llongsshort()
    rsi_mfi.longCon_shortCon()
    # check
    # rsi_mfi.combine()
    # rsi_mfi.check_reg_line()
    # rsi_mfi.check_long_short()
    # rsi_mfi.check_class()
    # rsi_mfi.check_prediction()
    # rsi_mfi.check_signal()
    # rsi_mfi.check_changed()
    # rsi_mfi.check_start_long_short()
    # print(rsi_mfi.df)
    rsi_mfi.df.to_csv("./advanced_ta/ManhattanDistance/rsimfi_out.csv")
    # rsi_mfi.plot()
