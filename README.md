# HistoricalStockAnalysis

Primary code is in 'historicalstockanalysis.py', written in Python as the extension implies

Stock data pulled from Alpha Vantage in November 2017


To run the script:

1.Download 'historicalstockanalysis.py', 'NASDAQ.txt', and 'formattedNASDAQ.zip'. 

2. Make sure all in the same directory. 

3. Unzip formattedNASDAQ.zip. This creates a folder in the directory with all of the stock data (functionally my database).

4. From Terminal, navigate to the directory using the 'cd' command, then enter (without the "") "python ./historicalstockanalysis.py"

5. Be sure to expand the Terminal window to be able to view the output in a clean manner


Output:
There are two main outputs: the printed output of the program in the Terminal and four JSON files for analysis in Tableau.

  Printed Output:
  There are three sections of the output
  1. The visual representation of what is going on in an example theory. Adjust constants in the "Main Program" section of the script to print out the results of another individual theory
  2. The ranked results of the history based theories. In the various columns you'll find the theory (e.g. "(36, 12)" which means 3 year history length and 1 year future length), then either the overall growth or monthly average growth (or both), the average number of months that this theory was implemented over (seeing as some theories can't be implemented as often based on the limitation of the 20 year dataset and the 4 year subset focus), and then finally the number of stocks in the portfolio
  3. The ranked results of the randomly selected theories. The columns have the same format as history-based performances described above.


