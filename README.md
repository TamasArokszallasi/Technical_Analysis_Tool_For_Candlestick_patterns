# HUFEUR_TA 
Project deatails:
Started: 2024.06.10.
Current status: In Progress
Expected finishing date: 2024.07.31.
Finished date: 2024.06.25.

The aim of this project is to create a code which can do Trend Analysis on various FX Rate pairs by focusing on the **weekly** japanese candlestick patterns. 
The sole purpose of this is to provide a differentiation for my VAR analysis on the same dependent variable which is the HUF/EUR.

What we need before start coding?

**1) DATA COLLECTION**
<br> Database of FX Rates in weekly time period from 2006.01.01 until 2023.06.31
**The following pairs are needed : <br>HUF/USD	<br>CZK/USD	<br>PLN/USD	<br>DKK/USD	<br>SEK/USD	<br>CHF/USD	<br>EUR/USD**  . 
<br>These are the currencies of EU member states that are of course not within the Eurozone.
For this purpose i will use the **Stooq.com** website which is a free and open data source website. My plan is to write a python code to scrape the data from the website directly and save it to an excel file.
  
**2) DECIDING ANALYTICAL METHODS;    PATTERNS**
<br> In **TA-Lib** there are 61 candlestick patterns that can be recognized. At first glance, I plan to find all the 61 patterns in the weekly chart.

**Japanese candlestick patterns:**
<br> Two Crows 
<br> Three Black Crows        
<br> Three Inside Up/Down        
<br> Three Line Strike       
<br> Three Outside Up/Down        
<br> Three Stars In The South        
<br> Three Advancing White Soldiers        
<br> Abandoned Baby        
<br> Advance Block        
<br> Belt hold       
<br> Breakaway        
<br> Closing Marubozu        
<br> Concealing Baby Swallow        
<br> Counterattack        
<br> Dark Cloud Cover        
<br> Doji        
<br> Doji Star        
<br> Dragonfly Doji        
<br> Engulfing Pattern        
<br> Evening Doji Star        
<br> Evening Star        
<br> Up/Down gap side by side white lines     
<br> Gravestone Doji        
<br> Hammer        
<br> Hanging Man        
<br> Harami Pattern        
<br> Harami Cross Pattern        
<br> High Wave Candle       
<br> Hikkake Pattern        
<br> Modified Hikkake Pattern        
<br> Homing Pigeon        
<br> Identical Three Crows        
<br> In Neck Pattern       
<br> Inverted Hammer        
<br> Kicking        
<br> Kicking   bull/bear determined by the longer marubozu       
<br> Ladder Bottom        
<br> Long Legged Doji        
<br> Long Line Candle        
<br> Marubozu        
<br> Matching Low        
<br> Mat Hold        
<br> Morning Doji Star        
<br> Morning Star        
<br> On Neck Pattern       
<br> Piercing Pattern        
<br> Rickshaw Man        
<br> Rising/Falling Three Methods        
<br> Separating Lines        
<br> Shooting Star        
<br> Short Line Candle        
<br> Spinning Top        
<br> Stalled Pattern        
<br> Stick Sandwich        
<br> Takuri (Dragonfly Doji with very long lower shadow)        
<br> Tasuki Gap        
<br> Thrusting Pattern        
<br> Tristar Pattern        
<br> Unique 3 River        
<br> Upside Gap Two Crows        
<br> Upside/Downside Gap Three Methods        

As a plus if needed and have time, I can extend the analytics with **indicators:**
<br>**Moving Averages (SMA, EMA):** Identify trends and potential reversal points.
<br>**MACD:** Signal changes in the strength, direction, momentum, and duration of a trend.
<br>**RSI:** Identify overbought or oversold conditions.
<br>**Bollinger Bands:** Show volatility and potential reversal points.
<br>**ATR:** Measure volatility.
<br>**OBV:** Use volume to predict price changes.

Fibonacci Retracement must have to be calculated manually. I think i will create some sort of reusable code for this one
<br>**Fibonacci Retracement:** Identify potential support and resistance levels.


**3) METHODOLOGY**

So I have to go through the chart with the weekly candles and identify when does these patterns occour and create a different alert for all occurence. Basically, each pattern if appear, by theory it should predict the price movement of the observed ticker.  Technical analysis is good for past analytics and also for forecasting, but in economist way of thinking it is out of question utterly useless to predict only by price.

We need to use some pre-built libraries for this progress to make it easier to find patterns and indicator signs.
The followign libraries are needed:
**-Pandas**
**-Pandas_ta**
**-TA-lib**
**-MPLfinance**
**-ExcelWriter**
**-StringIO**


**4) How i imagine the code should go (note for myself)**
So the first target will be the HUF/EUR chart, not to complicate with other at first glance. I imagine the following:
We create a table where there are 3 column. The first column will contain the name of the pattern, the second column will show the type of the signal wether it is bullish or bearish. The third column should show the number of predicted movements became true or false (with the true section there will be a filter, which checks the first 5 candlestick after a pattern occour and checks if it occour on any day and highlight it on which day it occour. Of course, a fourth column to singla on which date are we.

It is important to have only these 4 column, no more, because it will makes it easier for further analytics in PowerBi or Excel.

I want something like this as a output and as a unique table from which i will do the further elaboration:

| Candlestick_name          | signal_type        | Signal_outcome                | Date     |
| ------------- | ------------- | -------------       | ------------- |
| HAMMER     | Bullish       |         True      | 2022.01.02    |
| Bollinger Bands       | Bearish       |  False    | 2017.01.02    |


I also would like to create a closeness variable but with considering the candlesticks and volume also, not the fx rate on its own.
