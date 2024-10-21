# Technical Analysis Tool for Candlestick Patterns

## Project Description

**Project Overview:**
This project is a technical analysis tool that automates the identification of Japanese candlestick patterns and analyzes foreign exchange rate pairs. It allows users to collect data for various currency pairs over specific time periods, detect candlestick patterns, and assess their outcomes. The analysis helps to predict potential market movements, thereby aiding trading and investment decisions.

## Key Features
- **Data Collection:** The project uses Stooq.com as a data source, scraping historical foreign exchange rate data for specific currency pairs.
- **Pattern Analysis:** Uses TA-Lib, a Python library for technical analysis, to identify and assess the presence of 19 major Japanese candlestick patterns.
- **Outcome Evaluation:** For each detected pattern, it checks if the expected market movement occurred within the next five periods (days/weeks), providing an evaluation of the pattern's reliability.
- **Customizable Inputs:** Users can specify the currency pairs, observation periods, and date ranges for a tailored analysis.
- **Excel Output:** The analyzed data, along with the raw data, is saved into an Excel file, which can be used for further analysis using tools like Power BI or Excel.

## Benefits of This Tool
This tool helps traders and analysts by automating a significant part of the technical analysis process, specifically for candlestick patterns. Key benefits include:
- **Efficiency:** The tool automates data collection, pattern detection, and outcome assessment, saving users significant time compared to manual analysis.
- **Accuracy:** Using TA-Lib ensures that the pattern detection and indicator calculations are based on industry-standard algorithms, reducing the chances of human error in interpretation.
- **Custom Analysis:** Users can adapt the tool to their specific needs by selecting the desired currency pairs, timeframes, and candlestick patterns for analysis.
- **Data Visualization Ready:** The output is formatted into Excel files, making it easy for users to visualize or further analyze the results in tools like Power BI or Excel.

## How It Works
The tool is composed of several key components:
1. **Data Collection:** The tool requests data from Stooq.com for user-specified currency pairs and date ranges, scrapes the historical data, and saves it into a DataFrame.
2. **Pattern Detection:** Using TA-Lib, the tool identifies key Japanese candlestick patterns such as Hammer, Shooting Star, Bullish Engulfing, Bearish Engulfing, Evening Star, Morning Star, Bullish Harami, Bearish Harami, Three Black Crows, Three White Soldiers, Gravestone Doji, Dragonfly Doji, Bullish Long Legged Doji, Bearish Long Legged Doji, Marubozu, Hanging Man, Inverted Hammer, Piercing Line, and Dark Cloud Cover. For each pattern, it checks whether the expected outcome (bullish, bearish, or continuation) occurs within five subsequent periods.
3. **Analysis:** The detected patterns are analyzed to determine if they correctly predicted the market movement, which helps evaluate the accuracy of each pattern under specific market conditions.
4. **Output Generation:** The final analysis, including the raw data and detected patterns, is saved into an Excel file with multiple sheets for easy consumption and further analysis.

## Project Workflow
The first target is analyzing the HUF/EUR chart, with the ability to expand to other currency pairs later. The workflow follows these steps:
1. Obtain inputs: currency pair(s), start date, end date, and period size (daily, weekly, or monthly).
2. Scrape the data from Stooq.com based on these inputs.
3. Identify candlestick patterns using TA-Lib for each period.
4. Check the outcome of each detected pattern within the next five periods.
5. Save the raw and analyzed data into an Excel file, with distinct sheets for easy access.

## Future Development Options and Use Cases
There are numerous potential extensions and use cases for this tool:
- **Extended Pattern and Indicator Analysis:** The analysis could be extended to include additional indicators for a more comprehensive technical analysis.
- **Automation for Real-Time Analysis:** The project could be expanded to fetch real-time data, allowing users to get up-to-date analysis and make timely trading decisions.
- **API Integration:** The tool could be enhanced to integrate with various broker APIs, allowing for automated trading signals based on pattern detections.
- **Public Release:** The final tool could be published for research communities, supporting further analysis and the sharing of economic insights and technical analysis strategies.

## Conclusion
This project provides a robust foundation for performing technical analysis on foreign exchange rate pairs through automated candlestick pattern recognition and evaluation. By providing detailed, customizable, and automated analysis, this tool can significantly enhance the efficiency and accuracy of technical analysis for traders, researchers, and analysts. The outputs are structured in a way that facilitates further investigation, making it suitable for integration with business intelligence tools.
