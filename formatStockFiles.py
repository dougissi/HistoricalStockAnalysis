import json
import os

# location of stock data files
directory = "NASDAQDataFiles"
stocksList = "stocksToDownload.txt"
newDirectory = "formattedNASDAQ"

# constants for stock data in file, formated according to Alpha Vantage API
seriesType = "Monthly Adjusted Time Series"
valueType = "5. adjusted close"

for file in os.listdir(directory):
    if file.endswith(".txt"):
        stockData = {}
        stockData[seriesType] = {}
        
        particularStockFile = os.path.join(directory, file)
        #print particularStockFile
        with open(particularStockFile) as jsonFile:
            pythonData = json.load(jsonFile)
            #print pythonData
            for fullDate in pythonData[seriesType]:
                shortDate = fullDate.split("-")[0] + "-" + fullDate.split("-")[1]
                #print file, shortDate
                stockData[seriesType][shortDate] = pythonData[seriesType][fullDate]
        json.dump(stockData, open(os.path.join(newDirectory,file),'w'))




                                                    


