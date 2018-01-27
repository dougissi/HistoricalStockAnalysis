from urllib2 import Request, urlopen, URLError
import json

# constants for querying url for Alpha Vantage API
server = "https://www.alphavantage.co/"
functionType = "TIME_SERIES_MONTHLY_ADJUSTED"
#stock = "AAPL"
apiKey = "YRPBYKAPXX2TF1Q0"


# folder where files are to be created
directory = "NASDAQDataFiles"
stocksList = "stocksToDownload.txt"

# formats querying url for Alpha Vantage API
# e.g. https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=AAPL&apikey=YRPBYKAPXX2TF1Q0
def buildQueryURL(symbol):
    url = server + "query?function=" + functionType + "&symbol=" + symbol + "&apikey=" + apiKey
    #print url
    return url

stocksFile = open(stocksList,"r")    # opens and  prepares to read stocksList, which contains all of the stock tickers, located in same directory
for line in stocksFile:
    stock = line.rstrip('\n')        # strips off '\n' character
    #print stock
    newFilename = directory + "/" + stock + ".txt"
    #print newFilename
    queryURL = buildQueryURL(stock)
    #print queryURL
    jsonQuery = Request(queryURL)        # attempt to query from server
    try:
        jsonResponse = urlopen(jsonQuery)
        pythonData = json.load(jsonResponse)
        if "Monthly Adjusted Time Series" in pythonData:
            json.dump(pythonData, open(newFilename, 'w'))
        else:
            print "No data for:", stock

    except URLError, e:
        print 'Fail on: ', stock, 'Please retry.', e

