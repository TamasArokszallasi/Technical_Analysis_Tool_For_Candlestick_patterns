# HUFEUR_TA

The aim of this project is to create a code which can do Trend Analysis on various FX Rate pairs by focusing on the **weekly** japanese candlestick patterns and in general, the price movements of a pair. 
The sole purpose of this is to provide a differentiation for my VAR analysis on the same dependent variable which is the HUF/EUR.

What we need before start coding?

**1) DATA COLLECTION**
<br> Database of FX Rates in weekly time period from 2006.01.01 until 2023.06.31
**The following pairs are needed : <br>HUF/USD	<br>CZK/USD	<br>PLN/USD	<br>DKK/USD	<br>SEK/USD	<br>CHF/USD	<br>EUR/USD**  . <br>These are the currencies of EU member states that are of course not within the Eurozone.
For this purpose i will use the YFINANCE library, that is pretty good for this i assume
  
**2) DECIDING ANALYTICAL METHODS;   INDICATORS&PATTERNS**
We need the following **indicators:**
I can use: Pandas_Ta and Ta-Lib for the below mentioned indicators.
<br>**Moving Averages (SMA, EMA):** Identify trends and potential reversal points.
<br>**MACD:** Signal changes in the strength, direction, momentum, and duration of a trend.
<br>**RSI:** Identify overbought or oversold conditions.
<br>**Bollinger Bands:** Show volatility and potential reversal points.
<br>**ATR:** Measure volatility.
<br>**OBV:** Use volume to predict price changes.

Fibonacci Retracement must have to be calculated manually :( I think i will create some sort of reusable code for this one
<br>**Fibonacci Retracement:** Identify potential support and resistance levels.

**Japanese candlestick patterns:**
Here also we can use the Pandas_ta or Ta-lib
<br>**Doji** : Indicates indecision in the market. The opening and closing prices are virtually equal.
<br>**Hammer:** Bullish reversal pattern that occurs at the bottom of a downtrend.
<br>**Hanging Man:** Bearish reversal pattern that occurs at the top of an uptrend.
<br>**Bullish Engulfing:** A small red candle followed by a larger green candle that engulfs the previous candle.
<br>**Bearish Engulfing:** A small green candle followed by a larger red candle that engulfs the previous candle.
<br>**Morning Star:** A three-candle pattern indicating a bullish reversal.
<br>**Evening Star:** A three-candle pattern indicating a bearish reversal.


The situation getting complex here: pattern-recognition-api
<br>**Head and Shoulders Top:** A bearish reversal pattern.
<br>**Head and Shoulders Bottom (Inverse):** A bullish reversal pattern.
<br>**Double Top:** A bearish reversal pattern that forms after an uptrend.
<br>**Double Bottom:** A bullish reversal pattern that forms after a downtrend.

**3) METHODOLOGY**

So I have to go through the chart with the weekly candles and identify when does these patterns occour and create a different alert for all occurence. Basically, each indicator and pattern if appear, by theory it should predict the price movement of the observed ticker.  Trend analysis is good also for a past analytics and also for forecasting, but economically it is out of question utterly useless to predict only by price.
We need to use some pre-built libraries for this progress to make it easier to find patterns and indicator signs.
The followign libraries are needed at first thought:
-Pandas
-Pandas_ta
-TA_lib
-MPLfinance (coloring individual candlesticks to highlight various patterns
-yfinance 

**4) How i imagine the code should go (note for myself)**
So the first target will be the HUF/EUR chart, not to complicate with other at first glance. I imagine the following:
We create a table where there are 3 column. The first column will contain the name of the indicator or the pattern, the second column will show the number of occurence of the pattern or number of occurence of a bullish/bearish indicator. The third column should show the number of predicted movements became true. ALso now i think about i will definetiley need to store each and every occurence, to be able to visualise it and highlight when does that actually happened. THe question is how?

I want something like this as a output and as a unique table from which i will do the further elaboration:

| Type          | signal        | Name                | Occurence     |
| ------------- | ------------- | -------------       | ------------- |
| Indicator     | Bullish       | HAMMER              | 2022.01.02    |
| Pattern       | Bearish       | Bollinger Bands     | 2017.01.02    |

Example:
1) going through the chart and look for a Bullish  Hammer candle, if find 1,  save it somewhere to a  dictionary and go further and check if there exists more or not. If the for loop is done, went through all the candles and find x amount of bullish hammers which all added to the previously mentioned table



I also would like to create a closeness variable but with considering the candlesticks and volume also, not the fx rate on its own.
