# HUFEUR_TA

The aim of this project is to create a code which can do Trend Analysis on various FX Rate pairs by focusing on the weekly japanese candlestick patterns and in general, the price movements of a pair. 
The sole purpose of this is to provide a differentiation for my VAR analysis on the same dependent variable which is the HUF/EUR.

In theory the plan for this project is the following:


-Dataset of FX Rates in weekly time period from 2006.01.01 until 2023.06.31
  **The following pairs are needed : <br>HUF/USD	<br>CZK/USD	<br>PLN/USD	<br>DKK/USD	<br>SEK/USD	<br>CHF/USD	<br>EUR/USD**  . <br>These are the currencies of EU member states that are of course not within the Eurozone.
  
-After collecting the data, i should decide in what sort of analytics pattern will i look for. 

In theory, these are the most important indicators of Trend Analysis:
<br>**Moving Averages (SMA, EMA):** Identify trends and potential reversal points.
<br>**MACD:** Signal changes in the strength, direction, momentum, and duration of a trend.
<br>**RSI:** Identify overbought or oversold conditions.
<br>**Bollinger Bands:** Show volatility and potential reversal points.
<br>**ATR:** Measure volatility.
<br>**OBV:** Use volume to predict price changes.
<br>**Fibonacci Retracement:** Identify potential support and resistance levels.

With the indicators, i want to also check its occurence and the outcome of the bullsih/bearish indications. 

To give an importance for the japanese candlestick patterns, i would like to highlight the most famous japanese candlestick patterns which are:
<br>**Doji** : Indicates indecision in the market. The opening and closing prices are virtually equal.
<br>**Hammer:** Bullish reversal pattern that occurs at the bottom of a downtrend.
<br>**Hanging Man:** Bearish reversal pattern that occurs at the top of an uptrend.
<br>**Bullish Engulfing:** A small red candle followed by a larger green candle that engulfs the previous candle.
<br>**Bearish Engulfing:** A small green candle followed by a larger red candle that engulfs the previous candle.
<br>**Morning Star:** A three-candle pattern indicating a bullish reversal.
<br>**Evening Star:** A three-candle pattern indicating a bearish reversal.
<br>**Head and Shoulders Top:** A bearish reversal pattern.
<br>**Head and Shoulders Bottom (Inverse):** A bullish reversal pattern.
<br>**Double Top:** A bearish reversal pattern that forms after an uptrend.
<br>**Double Bottom:** A bullish reversal pattern that forms after a downtrend.

-So I have to go through the chart with the weekly candles and identify when does these patterns occour and create a different alert for all occurence.
It is very much important that the price movements before and after the pattern should have to be highlighted.

-I also would like to create a closeness variable but with the candlesticks.
