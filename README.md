<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Technical Analysis Tool for Candlestick Patterns</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    body {
      color: white;
      background-color: black;
    }
  </style>
</head>

<body>
  <div class="content">
    <h1 id="technical_analysis_tool_for_candlestick_patterns">Technical Analysis Tool for Candlestick Patterns</h1>
    
    <h2>Project Description</h2>
    <p><strong>Project Overview:</strong><br>
      This project is a technical analysis tool that automates the identification of Japanese candlestick patterns and analyzes foreign exchange rate pairs. It allows users to collect data for various currency pairs over specific time periods, detect candlestick patterns, and assess their outcomes. The analysis helps to predict potential market movements, thereby aiding trading and investment decisions.
    </p>
    
    <h2>Key Features</h2>
    <ul>
      <li><strong>Data Collection:</strong> The project uses Stooq.com as a data source, scraping historical foreign exchange rate data for specific currency pairs.</li>
      <li><strong>Pattern Analysis:</strong> Uses TA-Lib, a Python library for technical analysis, to identify and assess the presence of 19 major Japanese candlestick patterns.</li>
      <li><strong>Outcome Evaluation:</strong> For each detected pattern, it checks if the expected market movement occurred within the next five periods (days/weeks), providing an evaluation of the pattern's reliability.</li>
      <li><strong>Customizable Inputs:</strong> Users can specify the currency pairs, observation periods, and date ranges for a tailored analysis.</li>
      <li><strong>Excel Output:</strong> The analyzed data, along with the raw data, is saved into an Excel file, which can be used for further analysis using tools like Power BI or Excel.</li>
    </ul>
    
    <h2>Benefits of This Tool</h2>
    <p>This tool helps traders and analysts by automating a significant part of the technical analysis process, specifically for candlestick patterns. Key benefits include:</p>
    <ul>
      <li><strong>Efficiency:</strong> The tool automates data collection, pattern detection, and outcome assessment, saving users significant time compared to manual analysis.</li>
      <li><strong>Accuracy:</strong> Using TA-Lib ensures that the pattern detection and indicator calculations are based on industry-standard algorithms, reducing the chances of human error in interpretation.</li>
      <li><strong>Custom Analysis:</strong> Users can adapt the tool to their specific needs by selecting the desired currency pairs, timeframes, and candlestick patterns for analysis.</li>
      <li><strong>Data Visualization Ready:</strong> The output is formatted into Excel files, making it easy for users to visualize or further analyze the results in tools like Power BI or Excel.</li>
    </ul>
    
    <h2>How It Works</h2>
    <p>The tool is composed of several key components:</p>
    <ol>
      <li><strong>Data Collection:</strong> The tool requests data from Stooq.com for user-specified currency pairs and date ranges, scrapes the historical data, and saves it into a DataFrame.</li>
      <li><strong>Pattern Detection:</strong> Using TA-Lib, the tool identifies key Japanese candlestick patterns such as Hammer, Shooting Star, Bullish Engulfing, Bearish Engulfing, Evening Star, Morning Star, Bullish Harami, Bearish Harami, Three Black Crows, Three White Soldiers, Gravestone Doji, Dragonfly Doji, Bullish Long Legged Doji, Bearish Long Legged Doji, Marubozu, Hanging Man, Inverted Hammer, Piercing Line, and Dark Cloud Cover. For each pattern, it checks whether the expected outcome (bullish, bearish, or continuation) occurs within five subsequent periods.</li>
      <li><strong>Analysis:</strong> The detected patterns are analyzed to determine if they correctly predicted the market movement, which helps evaluate the accuracy of each pattern under specific market conditions.</li>
      <li><strong>Output Generation:</strong> The final analysis, including the raw data and detected patterns, is saved into an Excel file with multiple sheets for easy consumption and further analysis.</li>
    </ol>
    
    <h2>Project Workflow</h2>
    <p>The first target is analyzing the HUF/EUR chart, with the ability to expand to other currency pairs later. The workflow follows these steps:</p>
    <ol>
      <li>Obtain inputs: currency pair(s), start date, end date, and period size (daily, weekly, or monthly).</li>
      <li>Scrape the data from Stooq.com based on these inputs.</li>
      <li>Identify candlestick patterns using TA-Lib for each period.</li>
      <li>Check the outcome of each detected pattern within the next five periods.</li>
      <li>Save the raw and analyzed data into an Excel file, with distinct sheets for easy access.</li>
    </ol>
    
    <h2>Future Development Options and Use Cases</h2>
    <p>There are numerous potential extensions and use cases for this tool:</p>
    <ul>
      <li><strong>Extended Pattern and Indicator Analysis:</strong> The analysis could be extended to include additional indicators for a more comprehensive technical analysis.</li>
      <li><strong>Automation for Real-Time Analysis:</strong> The project could be expanded to fetch real-time data, allowing users to get up-to-date analysis and make timely trading decisions.</li>
      <li><strong>API Integration:</strong> The tool could be enhanced to integrate with various broker APIs, allowing for automated trading signals based on pattern detections.</li>
      <li><strong>Public Release:</strong> The final tool could be published for research communities, supporting further analysis and the sharing of economic insights and technical analysis strategies.</li>
    </ul>
    
    <h2>Conclusion</h2>
    <p>This project provides a robust foundation for performing technical analysis on foreign exchange rate pairs through automated candlestick pattern recognition and evaluation. By providing detailed, customizable, and automated analysis, this tool can significantly enhance the efficiency and accuracy of technical analysis for traders, researchers, and analysts. The outputs are structured in a way that facilitates further investigation, making it suitable for integration with business intelligence tools.</p>
  </div>
</body>

</html>
