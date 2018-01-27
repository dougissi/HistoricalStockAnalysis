#from urllib2 import Request, urlopen, URLError
import json
import timeit
import random
import copy

start_time = timeit.default_timer()

"""
    Notes:
    * Valid through end of Oct. 2017 and back to the end of Feb. 2000
"""


"""
    Global Constants
"""

intToDate = {214:'2017-12',213:'2017-11',212:'2017-10',211:'2017-09',210:'2017-08',209:'2017-07',208:'2017-06',207:'2017-05',206:'2017-04',205:'2017-03',204:'2017-02',203:'2017-01',202:'2016-12',201:'2016-11',200:'2016-10',199:'2016-09',198:'2016-08',197:'2016-07',196:'2016-06',195:'2016-05',194:'2016-04',193:'2016-03',192:'2016-02',191:'2016-01',190:'2015-12',189:'2015-11',188:'2015-10',187:'2015-09',186:'2015-08',185:'2015-07',184:'2015-06',183:'2015-05',182:'2015-04',181:'2015-03',180:'2015-02',179:'2015-01',178:'2014-12',177:'2014-11',176:'2014-10',175:'2014-09',174:'2014-08',173:'2014-07',172:'2014-06',171:'2014-05',170:'2014-04',169:'2014-03',168:'2014-02',167:'2014-01',166:'2013-12',165:'2013-11',164:'2013-10',163:'2013-09',162:'2013-08',161:'2013-07',160:'2013-06',159:'2013-05',158:'2013-04',157:'2013-03',156:'2013-02',155:'2013-01',154:'2012-12',153:'2012-11',152:'2012-10',151:'2012-09',150:'2012-08',149:'2012-07',148:'2012-06',147:'2012-05',146:'2012-04',145:'2012-03',144:'2012-02',143:'2012-01',142:'2011-12',141:'2011-11',140:'2011-10',139:'2011-09',138:'2011-08',137:'2011-07',136:'2011-06',135:'2011-05',134:'2011-04',133:'2011-03',132:'2011-02',131:'2011-01',130:'2010-12',129:'2010-11',128:'2010-10',127:'2010-09',126:'2010-08',125:'2010-07',124:'2010-06',123:'2010-05',122:'2010-04',121:'2010-03',120:'2010-02',119:'2010-01',118:'2009-12',117:'2009-11',116:'2009-10',115:'2009-09',114:'2009-08',113:'2009-07',112:'2009-06',111:'2009-05',110:'2009-04',109:'2009-03',108:'2009-02',107:'2009-01',106:'2008-12',105:'2008-11',104:'2008-10',103:'2008-09',102:'2008-08',101:'2008-07',100:'2008-06',99:'2008-05',98:'2008-04',97:'2008-03',96:'2008-02',95:'2008-01',94:'2007-12',93:'2007-11',92:'2007-10',91:'2007-09',90:'2007-08',89:'2007-07',88:'2007-06',87:'2007-05',86:'2007-04',85:'2007-03',84:'2007-02',83:'2007-01',82:'2006-12',81:'2006-11',80:'2006-10',79:'2006-09',78:'2006-08',77:'2006-07',76:'2006-06',75:'2006-05',74:'2006-04',73:'2006-03',72:'2006-02',71:'2006-01',70:'2005-12',69:'2005-11',68:'2005-10',67:'2005-09',66:'2005-08',65:'2005-07',64:'2005-06',63:'2005-05',62:'2005-04',61:'2005-03',60:'2005-02',59:'2005-01',58:'2004-12',57:'2004-11',56:'2004-10',55:'2004-09',54:'2004-08',53:'2004-07',52:'2004-06',51:'2004-05',50:'2004-04',49:'2004-03',48:'2004-02',47:'2004-01',46:'2003-12',45:'2003-11',44:'2003-10',43:'2003-09',42:'2003-08',41:'2003-07',40:'2003-06',39:'2003-05',38:'2003-04',37:'2003-03',36:'2003-02',35:'2003-01',34:'2002-12',33:'2002-11',32:'2002-10',31:'2002-09',30:'2002-08',29:'2002-07',28:'2002-06',27:'2002-05',26:'2002-04',25:'2002-03',24:'2002-02',23:'2002-01',22:'2001-12',21:'2001-11',20:'2001-10',19:'2001-09',18:'2001-08',17:'2001-07',16:'2001-06',15:'2001-05',14:'2001-04',13:'2001-03',12:'2001-02',11:'2001-01',10:'2000-12',9:'2000-11',8:'2000-10',7:'2000-09',6:'2000-08',5:'2000-07',4:'2000-06',3:'2000-05',2:'2000-04',1:'2000-03',0:'2000-02'}

dateToInt = {'2017-12':214,'2017-11':213,'2017-10':212,'2017-09':211,'2017-08':210,'2017-07':209,'2017-06':208,'2017-05':207,'2017-04':206,'2017-03':205,'2017-02':204,'2017-01':203,'2016-12':202,'2016-11':201,'2016-10':200,'2016-09':199,'2016-08':198,'2016-07':197,'2016-06':196,'2016-05':195,'2016-04':194,'2016-03':193,'2016-02':192,'2016-01':191,'2015-12':190,'2015-11':189,'2015-10':188,'2015-09':187,'2015-08':186,'2015-07':185,'2015-06':184,'2015-05':183,'2015-04':182,'2015-03':181,'2015-02':180,'2015-01':179,'2014-12':178,'2014-11':177,'2014-10':176,'2014-09':175,'2014-08':174,'2014-07':173,'2014-06':172,'2014-05':171,'2014-04':170,'2014-03':169,'2014-02':168,'2014-01':167,'2013-12':166,'2013-11':165,'2013-10':164,'2013-09':163,'2013-08':162,'2013-07':161,'2013-06':160,'2013-05':159,'2013-04':158,'2013-03':157,'2013-02':156,'2013-01':155,'2012-12':154,'2012-11':153,'2012-10':152,'2012-09':151,'2012-08':150,'2012-07':149,'2012-06':148,'2012-05':147,'2012-04':146,'2012-03':145,'2012-02':144,'2012-01':143,'2011-12':142,'2011-11':141,'2011-10':140,'2011-09':139,'2011-08':138,'2011-07':137,'2011-06':136,'2011-05':135,'2011-04':134,'2011-03':133,'2011-02':132,'2011-01':131,'2010-12':130,'2010-11':129,'2010-10':128,'2010-09':127,'2010-08':126,'2010-07':125,'2010-06':124,'2010-05':123,'2010-04':122,'2010-03':121,'2010-02':120,'2010-01':119,'2009-12':118,'2009-11':117,'2009-10':116,'2009-09':115,'2009-08':114,'2009-07':113,'2009-06':112,'2009-05':111,'2009-04':110,'2009-03':109,'2009-02':108,'2009-01':107,'2008-12':106,'2008-11':105,'2008-10':104,'2008-09':103,'2008-08':102,'2008-07':101,'2008-06':100,'2008-05':99,'2008-04':98,'2008-03':97,'2008-02':96,'2008-01':95,'2007-12':94,'2007-11':93,'2007-10':92,'2007-09':91,'2007-08':90,'2007-07':89,'2007-06':88,'2007-05':87,'2007-04':86,'2007-03':85,'2007-02':84,'2007-01':83,'2006-12':82,'2006-11':81,'2006-10':80,'2006-09':79,'2006-08':78,'2006-07':77,'2006-06':76,'2006-05':75,'2006-04':74,'2006-03':73,'2006-02':72,'2006-01':71,'2005-12':70,'2005-11':69,'2005-10':68,'2005-09':67,'2005-08':66,'2005-07':65,'2005-06':64,'2005-05':63,'2005-04':62,'2005-03':61,'2005-02':60,'2005-01':59,'2004-12':58,'2004-11':57,'2004-10':56,'2004-09':55,'2004-08':54,'2004-07':53,'2004-06':52,'2004-05':51,'2004-04':50,'2004-03':49,'2004-02':48,'2004-01':47,'2003-12':46,'2003-11':45,'2003-10':44,'2003-09':43,'2003-08':42,'2003-07':41,'2003-06':40,'2003-05':39,'2003-04':38,'2003-03':37,'2003-02':36,'2003-01':35,'2002-12':34,'2002-11':33,'2002-10':32,'2002-09':31,'2002-08':30,'2002-07':29,'2002-06':28,'2002-05':27,'2002-04':26,'2002-03':25,'2002-02':24,'2002-01':23,'2001-12':22,'2001-11':21,'2001-10':20,'2001-09':19,'2001-08':18,'2001-07':17,'2001-06':16,'2001-05':15,'2001-04':14,'2001-03':13,'2001-02':12,'2001-01':11,'2000-12':10,'2000-11':9,'2000-10':8,'2000-09':7,'2000-08':6,'2000-07':5,'2000-06':4,'2000-05':3,'2000-04':2,'2000-03':1,'2000-02':0}

# constants for filenames
directory = "formattedNASDAQ" # folder where files are to be created
stocksList = "NASDAQ.txt" # list of stocks to be considered

# constants for stock data in file, formated according to Alpha Vantage API
seriesType = "Monthly Adjusted Time Series"
valueType = "5. adjusted close"
close = "4. close"


"""
    Supplementary functions
"""

# prepares and returns 'stocksData' dictionary
# for each stock in 'stocksList', adds pertinent information to 'stocksData' from that stock's file (in 'directory')
def pullStockData():
    stocksData = {}     # stock data goes in here
    stocksFile = open(stocksList,"r")    # opens and  prepares to read file containing the list of stocks, located in same directory
    for line in stocksFile:
        stock = line.rstrip('\n')
        #print stock
        stocksData[stock] = {}
        particularStockFile = directory + "/" + stock + ".txt"
        #print particularStockFile
        
        with open(particularStockFile) as jsonFile:
            pythonData = json.load(jsonFile)
            for dateKey in pythonData[seriesType]:
                if float(pythonData[seriesType][dateKey][close]) < .005:
                    stocksData[stock][dateKey] = 0
                else:
                    stocksData[stock][dateKey] = float(pythonData[seriesType][dateKey][valueType])

    return stocksData

# removes stocks with gaps from stocksData dictionary
def removeStocksWithGaps():
    gaps = []
    for stock in stocksData:
        
        # results in a sorted list of dates for each stock
        datesList = []
        for date in stocksData[stock]:
            date = str(date)
            datesList.append(date)
        datesList = sorted(datesList)
        #print dates
        
        # start indices for previous and next dates in datesList
        previous = dateToInt[datesList[0]] # first date
        next = -1 # intentional impossible value
        
        i = 1
        while i < len(datesList):
            next = dateToInt[datesList[i]]
            if (next - previous) >= 2: # if gap, don't add to new dictionary
                #print "gap:", stock, intToDate[previous], "-", intToDate[next]
                gaps.append(stock)
                previous = next
            else: # since no gap, add to new dictionary
                previous = next
            i += 1

    for gappyStock in gaps:
        del stocksData[gappyStock]


# returns the percentage change of a stock from start to end dates (returns None if stock not existant at start date)
def analyzeStockOverTime(stock, start, end):
    #print stock            # prints stock name
    
    if start in stocksData[stock]:     # if stock goes back far enough, then continue, otherwise return None
        if end in stocksData[stock]:    # detects if there is a gap or bad date
            if latestDate in stocksData[stock]:        # if stock continues all the way up through today (or at least the latest date)
                if stocksData[stock][start] >= .01:       # if start didn't start unbuyable
                    startValue = stocksData[stock][start]
                    #print "%s: %s" % (start, startValue)
                    endValue = stocksData[stock][end]
                    #print "%s: %s" % (end, endValue)
                    percent = endValue / startValue
                    #print "%s: %s%s" % ("Change", percent, "\n")
                    return percent
                else:
                    return None
            else:
                print "bad last date: ", stock,":", latestDate
                return None
        else:
            print "bad end date: ", stock,":", end
            return None
    else:
        #print "bad start date", stock, end
        return None


# creates and returns a new LIST OF TUPLES of top stocks
# contains the desired number of top stocks (see constant above)
def historyTopStocks(startDate, currentDate, numberTopStocks):
    
    # empty dictionary to eventually rank stocks by price changes over initial time period
    allHistoryPercents = {}
    
    # each valid stock gets analized over history test period and percent change is added to allInitalPercentChanges
    for stock in stocksData:
        #totalStockCounter += 1       # adds one to totalStockCounter
        percent = analyzeStockOverTime(stock, startDate, currentDate)
        
        if percent != None:     # percent == None when stock when deemed invalid (see analyseStockOverTime)
            #validStockCounter += 1      # adds one to validStockCounter
            allHistoryPercents[stock] = percent

    # sorts stocks based on performance in new LIST OF TUPLES
    # puts the desired number of top stocks (see constant above), unless there aren't enough valid stocks in allHistoryPercents
    topStocks = sorted(allHistoryPercents.iteritems(), key=lambda x:-x[1])[:numberTopStocks]
    #print topStocks
    
    # ensures we have enough valid stocks
    if len(topStocks) < numberTopStocks:
        print "Insufficient number of valid stocks for desired number of top stocks"
        quit()

    return topStocks

def futureOverallPercent(topStocks, currentDate, futureDate):
    overallList = {}

    maxNumberStocks = 1
    while maxNumberStocks <= min(numberTopStocks, len(topStocks)):
        currentIndex = 0

        # calculates the sum of all of the top stocks growths over history period, to be used for proportional investment
        sumHistoryPercents = 0
        while currentIndex < maxNumberStocks:
            sumHistoryPercents += topStocks[currentIndex][1]
            currentIndex += 1

        #print sumHistoryPercents

        #Loops though topStocks, first the single top stocks, then the two most top stocks, then three, etc.
        #analyzes stocks over future time period (see currentDate and futureDate constants), populates overallList dictionary
        currentIndex = 0
        sumFuturePercents = 0
        propInvestOverall = 0
        
        while currentIndex < maxNumberStocks:
            stock = topStocks[currentIndex][0]
            #print stock
            historyPercent = topStocks[currentIndex][1]

            futurePercent = analyzeStockOverTime(stock, currentDate, futureDate)
            #print futurePercent

            sumFuturePercents += futurePercent
            propInvestOverall += historyPercent / sumHistoryPercents * futurePercent
            #print propInvestOverall
            
            currentIndex += 1
        
        evenInvestOverall = sumFuturePercents / maxNumberStocks
        #print evenInvestOverall
        
        overallList[maxNumberStocks] = (evenInvestOverall,propInvestOverall)

        maxNumberStocks += 1
    
    return overallList


# preps theories and results dictionaries with keys as the different theory types, e.g. (1,2), and adds appropriate number of empty lists for each possible starting point of theory, for all numb top stocks
def prepPerformanceBasedDictionaries():
    nextHistoryLength = historyUnit
    nextFutureLength = futureUnit
    # iterates over all history lengths and future lengths within subset of timeline limitation
    while (nextHistoryLength + nextFutureLength) <= timelineLength and nextHistoryLength <= maxHistoryLength:   # iterates over history lengths
        while (nextHistoryLength + nextFutureLength) <= timelineLength and nextFutureLength <= maxFutureLength:     #iterates over future lengths
            
            # add history length and future length tuple key, e.g. (1, 2) to theories and results
            theoryType = (nextHistoryLength,nextFutureLength)
            theories[theoryType] = {}
            results[theoryType] = {}
            
            fewerTopStocks = 1
            while fewerTopStocks <= numberTopStocks:
                theories[theoryType][fewerTopStocks] = []
                results[theoryType][fewerTopStocks] = []
                fewerTopStocks += 1
            
            
            # the maximum number of starting points is equal to the future length (could start at 1, 2, ... , futureLength)
            # only limited by the amount of space left and space left in subset
            spaceLeft = timelineLength - (max(nextHistoryLength,subsetStartDate) + nextFutureLength) + 1
            datesLeft = subsetEndDate - nextHistoryLength + 1
            numberStartingPoints = min(nextFutureLength, spaceLeft, datesLeft)
            #print numberStartingPoints
            while numberStartingPoints > 0:
                
                fewerTopStocks = 1
                while fewerTopStocks <= numberTopStocks:
                    theories[theoryType][fewerTopStocks].append([])
                    results[theoryType][fewerTopStocks].append([1,1,0])
                    fewerTopStocks += 1
                
                numberStartingPoints -= dateUnit
            
            nextFutureLength += futureUnit
        
        nextHistoryLength += historyUnit
        nextFutureLength = futureUnit

    #print sorted(theories.keys(), key = lambda x:x[0])
    #print results

# fills in the theories dictionary for each theory, e.g. (1,2), for all possible number of top stocks, and for all possible starting points
# does so in such an order that each history analysis only needs to be done once, i.e. all instances of particular history analysis added to theories, then next
def fillPerformanceBasedDictionaries():
    nextHistoryLength = historyUnit
    nextFutureLength = futureUnit
    while (nextHistoryLength + nextFutureLength) <= timelineLength and nextHistoryLength <= maxHistoryLength:   # iterates over history lengths
        dateStart = max(nextHistoryLength, subsetStartDate)    # earliest start date for history length is the history length itself or subset start date
        nextDate = dateStart
        
        # loops for all dates up until the end (but doesn't quite touch end)
        while nextDate <= subsetEndDate and nextDate < timelineLength:
            
            currentDate = intToDate[nextDate]
            startDate = intToDate[(nextDate - nextHistoryLength)]
            #print "history:", startDate,currentDate
            topStocks = historyTopStocks(startDate, currentDate, numberTopStocks)
            #print topStocks
            
            # loops through future lengths repeatedly for each date, as long as fits with history length for the timeline, subset, and nextDate
            while (nextHistoryLength + nextFutureLength) <= timelineLength and nextFutureLength <= maxFutureLength and (nextDate + nextFutureLength) <= timelineLength:
                mod = ((nextDate - dateStart) % nextFutureLength) / dateUnit    # which of the starting points the nextDate belongs to
                #print '(%s, %s): (%s - %s) mod %s = %s' % (nextHistoryLength, nextFutureLength, nextDate ,nextHistoryLength ,nextFutureLength, mod)
                
                futureDate = intToDate[(nextDate + nextFutureLength)]
                #print futureDate
                
                # dictionary of performances of top stocks over future timeframe, for all number of top stocks
                # Each number of top stocks maps to a tuple of even investment performance, then proportional inventment performance
                overallList = futureOverallPercent(topStocks, currentDate, futureDate)
                #print overallList
                
                fewerTopStocks = 1
                while fewerTopStocks <= numberTopStocks:
                    results[(nextHistoryLength,nextFutureLength)][fewerTopStocks][mod][0] = results[(nextHistoryLength,nextFutureLength)][fewerTopStocks][mod][0] * overallList[fewerTopStocks][0]
                    results[(nextHistoryLength,nextFutureLength)][fewerTopStocks][mod][1] = results[(nextHistoryLength,nextFutureLength)][fewerTopStocks][mod][1] * overallList[fewerTopStocks][1]
                    results[(nextHistoryLength,nextFutureLength)][fewerTopStocks][mod][2] += 1  # adds to tally of total number of dates this particular theory is employed
                    
                    theories[(nextHistoryLength,nextFutureLength)][fewerTopStocks][mod].append(nextDate)
                    
                    fewerTopStocks += 1
                
                
                #print theories
                nextFutureLength += futureUnit
            
            nextDate += dateUnit
            nextFutureLength = futureUnit       # reset the future length to the beginning
        
        nextHistoryLength += historyUnit
        nextFutureLength = futureUnit

    #print theories
    #print results


def randomOverallPercent(currentDate, futureDate):
    randomList = {}
    
    maxNumberStocks = 1
    while maxNumberStocks <= numberTopStocks:
        randomStocks = random.sample(stocksData.keys(), maxNumberStocks)
        currentIndex = 0
        
        #print sumHistoryPercents
        
        #Loops though all topStocks, analyzes stocks over future time period (see currentDate and futureDate constants), populates topStocksFuturePercents dictionary
        currentIndex = 0
        sumFutureRandomPercents = 0
        
        while currentIndex < maxNumberStocks:
            
            # random stock analysis
            randomStock = randomStocks[currentIndex]
            #print "Random stock:", randomStock
            randomPercent = analyzeStockOverTime(randomStock, currentDate, futureDate)
            while randomPercent == None:
                otherPick = random.choice(stocksData.keys())
                while (otherPick in randomStocks):
                    otherPick = random.choice(stocksData.keys())
                randomPercent = analyzeStockOverTime(otherPick, currentDate, futureDate)
            sumFutureRandomPercents += randomPercent
            
            currentIndex += 1
    
        randomInvestOverall = sumFutureRandomPercents / maxNumberStocks
        
        randomList[maxNumberStocks] = randomInvestOverall

        maxNumberStocks += 1

    return randomList


def prepRandomDictionaries():
    nextFutureLength = futureUnit
    # with history length set to smallest historyUnit, iterates over all future lengths within timeline limitation
    while (historyUnit + nextFutureLength) <= timelineLength and nextFutureLength <= maxFutureLength:
        
        # add history length and future length tuple key, e.g. (1, 2) to theoriesRandom and resultsRandom dictionaries
        theoryType = (historyUnit,nextFutureLength)
        #print theoryType
        theoriesRandom[theoryType] = {}
        resultsRandom[theoryType] = {}
        
        # add all possible number of top stocks to be considered, e.g. 1, 2, ... , numberTopStocks, to theoriesRandom and resultsRandom dictionaries
        fewerTopStocks = 1
        while fewerTopStocks <= numberTopStocks:
            resultsRandom[theoryType][fewerTopStocks] = []
            theoriesRandom[theoryType][fewerTopStocks] = []
            fewerTopStocks += 1
        
        
        # the maximum number of starting points is equal to the future length (could start at 1, 2, ... , futureLength)
        # only limited by the amount of space left
        spaceLeft = timelineLength - (max(historyUnit,subsetStartDate) + nextFutureLength) + 1
        datesLeft = subsetEndDate - historyUnit + 1
        numberStartingPoints = min(nextFutureLength, spaceLeft, datesLeft)
        #print numberStartingPoints
        while numberStartingPoints > 0:
            
            # add lists to hold info in both dictionaries to each possible number of top stocks
            fewerTopStocks = 1
            while fewerTopStocks <= numberTopStocks:
                theoriesRandom[theoryType][fewerTopStocks].append([])
                resultsRandom[theoryType][fewerTopStocks].append([1,0])     # the 1 will be used to multiply with future growth/loss decimal, 0 will be used to add to tally for number of dates theory was used
                fewerTopStocks += 1
            
            numberStartingPoints -= dateUnit
        
        nextFutureLength += futureUnit

    #print theoriesRandom
    #print resultsRandom


# fills in the theoriesRandom dictionary for each theory, e.g. (1,2), for all possible starting points for each number of top stocks
# does so in such an order that each history analysis only needs to be done once, i.e. all instances of particular history analysis added to theories, then next
def fillRandomDictionaries(resultsRandom):
    nextFutureLength = futureUnit
    dateStart = max(historyUnit, subsetStartDate)    # earliest start date for history length is the history length itself or subset start date, whichever is greater
    nextDate = dateStart
    
    # loops for all dates up until the end of timeline/subset (but doesn't quite touch end of timeline)
    while nextDate <= subsetEndDate and nextDate < timelineLength:
        
        currentDate = intToDate[nextDate]
        
        # loops through future lengths, as long as fits with history length AND nextDate
        while (historyUnit + nextFutureLength) <= timelineLength and nextFutureLength <= maxFutureLength and (nextDate + nextFutureLength) <= timelineLength:
            mod = ((nextDate - dateStart) % nextFutureLength) / dateUnit    # which of the starting points the nextDate belongs to
            #print '(%s, %s): (%s - %s) mod %s = %s' % (historyUnit, nextFutureLength, nextDate ,historyUnit ,nextFutureLength, mod)
            
            futureDate = intToDate[(nextDate + nextFutureLength)]
            #print futureDate
            
            randomList = randomOverallPercent(currentDate, futureDate)
            #print randomList
            
            
            fewerTopStocks = 1
            while fewerTopStocks <= numberTopStocks:
                resultsRandom[(historyUnit,nextFutureLength)][fewerTopStocks][mod][0] = resultsRandom[(historyUnit,nextFutureLength)][fewerTopStocks][mod][0] * randomList[fewerTopStocks]
                resultsRandom[(historyUnit,nextFutureLength)][fewerTopStocks][mod][1] += 1  # adds to tally of total number of dates this particular theory is employed
                
                theoriesRandom[(historyUnit,nextFutureLength)][fewerTopStocks][mod].append(nextDate)
                
                fewerTopStocks += 1
            
            #print theoriesRandom
            nextFutureLength += futureUnit

        nextDate += dateUnit
        nextFutureLength = futureUnit       # reset the future length to the beginning

    #print theoriesRandom
    #print resultsRandom


# formats decimal to percent
def percentFormat(growth):
    decimal = growth - 1
    percent = '{:.2%}'.format(decimal)
    return percent

# calculates average rate, month over month
def averageRate(growth, time):
    return (growth ** (1. / time))

# implements a single theory, evaluated at 'currentDate'
def implementTheory(currentDate, historyLength, futureLength, numberTopStocks):
    
    """
        Initial Variables
    """
    # empty dictionary to eventually hold stocks by price changes over future time period
    topStocksFuturePercents = {}
    
    # dates
    currentDateInt = dateToInt[currentDate]
    startDate = intToDate[(currentDateInt - historyLength)]
    futureDate = intToDate[(currentDateInt + futureLength)]
    
    # top stocks based on performance in new LIST OF TUPLES
    # contains the desired number of top stocks (see constant above)
    topStocks2 = historyTopStocks(startDate, currentDate, numberTopStocks)



    """
        Prints info on top stocks over history timeframe
    """

    print "Percent increase of top performers over history timeframe (" + str(historyLength) + " months(s), "+ startDate + " to " + currentDate + ")"

    # displays the number of top stocks (see constant above) with greatest positive price changes
    for key, value in topStocks2:
        print "%s: %s" % (key, percentFormat(value))
        histories.append({"Stock": key, "Percent Result": (value-1)*100, "Date of Result": currentDate, "Type": "History"})

    #Loops though all topStocks, analyzes stocks over future time period (see currentDate and futureDate constants), populates topStocksFuturePercents dictionary
    for tuples in topStocks2:
        stock = tuples[0]
        percent = tuples[1]
        #print "%s:\t%s\t(%s monthly avg.)" % (stock, percentFormat(percent), percentFormat( (percent ** (1. / historyLength) ) ) )      # displays the number of top stocks (see constant above) with greatest positive price changes
        #print percent
        percent = analyzeStockOverTime(stock, currentDate, futureDate)
        topStocksFuturePercents[stock] = percent
    #print topStocksFuturePercents

    # sorts stocks based on performance in new LIST OF TUPLES
    futurePerformance = sorted(topStocksFuturePercents.iteritems(), key=lambda x:-x[1])[:]
    #print futurePerformance


    """
        Prints info on test period top performers over future timeframe
    """

    print "\nPercent increase of history period top performers over future timeframe (" + str(futureLength) + " months(s), " + currentDate + " to " + futureDate + ")"

    # displays future performance of top stocks
    for key, value in futurePerformance:
        print "%s: %s" % (key, percentFormat(value))
        futures.append({"Stock": key, "Percent Result": (value-1)*100, "Date of Result": futureDate, "Type": "Future"})
    

    # calculates and displays total percentage growth/loss assuming even investment in top stocks at end of test timeframe
    sumFuturePercentages = 0
    for key, value in futurePerformance:
        #print "%s:\t%s\t(%s monthly avg.)" % (key, percentFormat(value), percentFormat( (value ** (1. / futureLength) ) ) )       # displays future performance of top stocks
        #print value
        sumFuturePercentages += value
    
    averagePercent = sumFuturePercentages / numberTopStocks
    print "\nAssuming even investment across top stocks, total percent growth/loss: "
    print '%s (%s monthly avg.)' % (percentFormat(averagePercent), percentFormat( (averagePercent ** (1. / futureLength) ) ) )
    
    if len(growth["Even"]) == 0:
        growth["Even"].append({"Percent Growth": averagePercent, "Date": futureDate})
    else:
        growth["Even"].append({"Percent Growth": growth["Even"][len(growth["Even"])-1]["Percent Growth"]*averagePercent, "Date": futureDate})



    """
        Prints overall combined performance of investing (both evenly and proportionally) in top stocks over future time period
    """
    # sum of all top stock percentages at the end of history test period, to be used for calculating growth if invested proportionally to test period growth
    sumTestPercentages = 0
    for key, value in topStocks2:
        sumTestPercentages += (value)
    #print sumTestPercentages

    weightedSum = 0
    for key, value in topStocks2:
        weightedSum += value / sumTestPercentages * topStocksFuturePercents[key]
        #print weightedSum
    #print weightedSum
    print "\nAssuming proporational investment across top stocks based on performance over history period, total percent increase/decrease: "
    print '%s (%s monthly avg.)' % (percentFormat(weightedSum), percentFormat( averageRate(weightedSum, futureLength) ) )

    if len(growth["Prop"]) == 0:
        growth["Prop"].append({"Percent Growth": weightedSum, "Date": futureDate})
    else:
        growth["Prop"].append({"Percent Growth": growth["Prop"][len(growth["Prop"])-1]["Percent Growth"]*weightedSum, "Date": futureDate})



    """
        Prints RANDOMLY selected stocks performance over future time period, both individually and collectively
    """
    print "\nPercent increase of RANDOM stocks over future timeframe (" + str(futureLength) + " months(s), " + currentDate + " to " + futureDate + ")"
    randomStockz = random.sample(stocksData.keys(), numberTopStocks)
    sumItemPercents = 0
    for item in randomStockz:
        itemPercent = analyzeStockOverTime(item, currentDate, futureDate)
        if itemPercent != None:
            print "%s:\t%s" % (item, percentFormat(itemPercent))
            randFutures.append({"Stock": item, "Percent Result": (itemPercent-1)*100, "Date of Result": futureDate, "Type": "Random Future"})
        otherPick = None
        while itemPercent == None:
            otherPick = random.choice(stocksData.keys())
            while (otherPick in randomStockz):
                otherPick = random.choice(stocksData.keys())
            itemPercent = analyzeStockOverTime(otherPick, currentDate, futureDate)
        if otherPick != None:
            print "%s:\t%s" % (otherPick, percentFormat(itemPercent))
            randFutures.append({"Stock": item, "Percent Result": (itemPercent-1)*100, "Date of Result": futureDate, "Type": "Random Future"})
        #print "%s:\t%s" % (item, percentFormat(itemPercent))
        
        sumItemPercents += itemPercent

    print "\nAssuming even investment across RANDOM stocks, total percent growth/loss: "
    print percentFormat(sumItemPercents/numberTopStocks)


    if len(growth["Rand"]) == 0:
        growth["Rand"].append({"Percent Growth": (sumItemPercents/numberTopStocks), "Date": futureDate})
    else:
        growth["Rand"].append({"Percent Growth": growth["Rand"][len(growth["Rand"])-1]["Percent Growth"]*(sumItemPercents/numberTopStocks), "Date": futureDate})

    print "___________________________________\n"






"""
    Constants for Main program
"""
# puts limits for length of time
# measured in months
earliestDate = "2000-02"
latestDate = "2017-10"
timelineLength = 212

# establishes how much history lengths, future lengths, and individual dates should vary
# measured in months
historyUnit = 12
futureUnit = 12
dateUnit = 1

# if focusing on a subset of the whole timeline, adjust these variables
# otherwise, set to standard measures
subsetStartDate = 164
subsetEndDate = 212
maxHistoryLength = subsetEndDate
maxFutureLength = timelineLength - subsetStartDate

# constants for (maximum) number of top stocks to consider in theories
numberTopStocks = 40

# number of trials (or iterations) of selecting random stocks
numberTrials = 10

# number of top theories to display
numberTopTheories = 1000000



"""
    Main program
"""
# pull and clean data from stock files (stored in a folder in directory)
stocksData = pullStockData()
removeStocksWithGaps()

# initiates, prepares, and fills dictioaries that contain the overall performances of portfolios theories, which are based on historical performance of stocks
theories = {}
results = {}
prepPerformanceBasedDictionaries()
fillPerformanceBasedDictionaries()

# initiates and prepares dictionaries that contain the overall performances of portfolios theories based on randomly selecting stock
# these dictionaries will be used to run multiple random trials
theoriesRandom = {}
resultsRandom = {}
prepRandomDictionaries()
resultsRandomBasic = copy.deepcopy(resultsRandom)   # creating deep copy of unfilled dictonary so that multiple random trials can be run
theoriesRandomBasic = copy.deepcopy(theoriesRandom) # creating deep copy of unfilled dictonary so that multiple random trials can be run

# adds each round of random analysis trial to allTrials dictionary
allTrials ={}
i = 1
while i <= numberTrials:
    resultsRandom = copy.deepcopy(resultsRandomBasic)
    theoriesRandom = copy.deepcopy(theoriesRandomBasic)
    fillRandomDictionaries(resultsRandom)
    allTrials[i] = resultsRandom
    i += 1

# establishes values for implementing a specific theory
theoryToTest = (36,12)
chosenNumStocks = 5
chosenCurrentDate = dateToInt["2016-10"]

# prints above constants
print "**EXAMPLE THEORY**\n"
print "Theory being tested: ", theoryToTest
print "Number of Stocks: ", chosenNumStocks
print "Chosen current date: ", intToDate[chosenCurrentDate], "\n"

# lists and dictionaries for tracking implemented theory
histories = []
futures = []
randFutures = []
growth = {}
growth["Even"] = []
growth["Prop"] = []
growth["Rand"] = []

# implements a specific theory and tracks info in various lists and dictionaries
for case in theories[theoryToTest][chosenNumStocks]:
    if chosenCurrentDate in case:
        for date in case:
            implementTheory(intToDate[date], theoryToTest[0], theoryToTest[1], chosenNumStocks)

# creates JSON file providing info on each stock's performance in the implemented theory
implementedTheoryResults = histories + futures + randFutures
with open('implementedTheoryResults.json', 'w') as outfile:
    json.dump(implementedTheoryResults, outfile)

# creates JSON file providing info on portfolio's performance over time in implemented theory
formattedGrowth = []
for type in growth:
    for pair in growth[type]:
        formattedGrowth.append({"Type": type, "Date": pair["Date"], "Percent Growth": (pair["Percent Growth"]-1)*100})
with open('implementedTheoryGrowth.json', 'w') as outfile:
    json.dump(formattedGrowth, outfile)


print "\n\n\n"
print "**RESULTS OF ALL HISTORICAL-PERFORMANCE THEORIES FOR GIVEN SUBSET OF TIMELINE\n"

#original
maxes = []
averagesByTheory = []
for theory in results:
    for numStocks in results[theory]:
        sum0 = 0
        sum1 = 0
        sumavg0 = 0
        sumavg1 = 0
        monthCounter = 0
        counter = 0
        for startingPoint in results[theory][numStocks]:
            numberMonths = startingPoint[2]*theory[1]
            yrlAvg0 = averageRate(startingPoint[0], numberMonths)
            yrlAvg1 = averageRate(startingPoint[1], numberMonths)
            maxes.append((theory, startingPoint[0], yrlAvg0, startingPoint[1], yrlAvg1, numStocks))
            
            sum0 += startingPoint[0]
            sum1 += startingPoint[1]
            sumavg0 += averageRate(startingPoint[0], numberMonths)
            sumavg1 += averageRate(startingPoint[1], numberMonths)
            monthCounter += numberMonths
            counter += 1
        avg0 = sum0 / counter
        avg1 = sum1 / counter
        avgavg0 = sumavg0 / counter
        avgavg1 = sumavg1 / counter
        avgMonths = monthCounter / counter

        averagesByTheory.append((theory, avg0, avgavg0, avg1, avgavg1, avgMonths, numStocks))


averagesByTheory2 = [{"historyLength": i[0], "futureLength":i[1], "theory": str(i), "totalAvgEven": (j-1)*100, "avgAvgEven": (k-1)*100, "totalAvgProp": (l-1)*100, "avgAvgProp": (m-1)*100, "avgMonths": n, "numStocks": o} for i,j,k,l,m,n,o in averagesByTheory]
#print json.dumps(averagesByTheory2, indent = 4)
with open('historyResults.json', 'w') as outfile:
    json.dump(averagesByTheory2, outfile)



print "Maxes by Theory: "
sortedAverageTotalsEven = sorted(averagesByTheory, key = lambda x: -x[1])[:numberTopTheories]
sortedAverageTotalsProp = sorted(averagesByTheory, key = lambda x: -x[3])[:numberTopTheories]

sortedAverageMonthlyAvgsEven = sorted(averagesByTheory, key = lambda x: -x[2])[:numberTopTheories]
sortedAverageMonthlyAvgsProp = sorted(averagesByTheory, key = lambda x: -x[4])[:numberTopTheories]

#sortedAverageMonthlyAvgsEven = sorted(sortedAverageMonthlyAvgsEven, key = lambda x:-x[1])
#sortedAverageMonthlyAvgsProp = sorted(sortedAverageMonthlyAvgsProp, key = lambda x:-x[3])


k = 0
print '{0:^24} {1:^24} {2:^40} {3:^40}'.format("Avg Total, Even","Avg Total, Prop", "Avg Monthly Avg, Even","Avg Monthly Avg, Prop")
while k < min(numberTopTheories, len(averagesByTheory)):
    print '{0:^10} {1:^10} {2:^2d} {3:^10} {4:^10} {5:^2d} {6:^10} {7:^10} {8:^10} {9:^2d} {10:^2d} {11:^10} {12:^10} {13:^10} {14:^2d} {15:^2d}'.format(sortedAverageTotalsEven[k][0], percentFormat(sortedAverageTotalsEven[k][1]), sortedAverageTotalsEven[k][6], sortedAverageTotalsProp[k][0], percentFormat(sortedAverageTotalsProp[k][3]), sortedAverageTotalsProp[k][6], sortedAverageMonthlyAvgsEven[k][0], percentFormat(sortedAverageMonthlyAvgsEven[k][2]), percentFormat(sortedAverageMonthlyAvgsEven[k][1]), sortedAverageMonthlyAvgsEven[k][5], sortedAverageMonthlyAvgsEven[k][6], sortedAverageMonthlyAvgsProp[k][0], percentFormat(sortedAverageMonthlyAvgsProp[k][4]), percentFormat(sortedAverageMonthlyAvgsProp[k][3]), sortedAverageMonthlyAvgsProp[k][5], sortedAverageMonthlyAvgsProp[k][6])
    k += 1


print "\n\n-------------------------------------------------------------------------------------------------------------------\n\n"

print "**RESULTS OF ALL THEORIES BASED ON RANDOM SELECTION OF STOCKS FOR GIVEN SUBSET OF TIMELINE\n"

# computes averages for each theory across all trials
# dictionary where the averages for each trial's theories are stored
averagesByTrialTheoryandNumStocks = {}

for trial in allTrials:
    averagesByTrialTheoryandNumStocks[trial] = {}
    for theory in allTrials[trial]:
        averagesByTrialTheoryandNumStocks[trial][theory] = {}
        for numStocks in allTrials[trial][theory]:
            sum0 = 0
            sumavg0 = 0
            monthCounter = 0
            counter = 0
            for result in allTrials[trial][theory][numStocks]:
                numberMonths = result[1]*theory[1]
                yrlAvg0 = averageRate(result[0], numberMonths)
                
                sum0 += result[0]
                sumavg0 += averageRate(result[0], numberMonths)
                
                monthCounter += numberMonths
                counter += 1
            avg0 = sum0 / counter
            avgavg0 = sumavg0 / counter
            avgMonths = monthCounter / counter
            
            averagesByTrialTheoryandNumStocks[trial][theory][numStocks] = (avg0, avgavg0, avgMonths)


comboRandResults = []
for theory in averagesByTrialTheoryandNumStocks[1]: # only need to cycle through different theory types once, so chose to cycle through the different theories from trial 1
    for numStocks in averagesByTrialTheoryandNumStocks[1][theory]: # only need to cycle through different number of stocks types once, so chose to cycle through the different number of trials from trial 1
        sumTrialsTotals = 0
        sumTrialsAvgs = 0
        numMonths = 0
        for trial in averagesByTrialTheoryandNumStocks:
            sumTrialsTotals += averagesByTrialTheoryandNumStocks[trial][theory][numStocks][0]
            sumTrialsAvgs += averagesByTrialTheoryandNumStocks[trial][theory][numStocks][1]
            numMonths = averagesByTrialTheoryandNumStocks[trial][theory][numStocks][2]  #doesn't change (?)
        avgTrialsTotals = sumTrialsTotals / numberTrials
        avgTrialsAvgs = sumTrialsAvgs / numberTrials

        comboRandResults.append((theory, avgTrialsTotals, avgTrialsAvgs, numMonths, numStocks))

# creates JSON file for all random results
comboRandResults2 = [{"historyLength": i[0], "futureLength":i[1], "theory": str(i), "avgTrialsTotals": (j-1)*100, "avgTrialsAvgs": (k-1)*100, "numMonths": l, "numStocks": m} for i,j,k,l,m in comboRandResults]
with open('randomResults.json', 'w') as outfile:
    json.dump(comboRandResults2, outfile)


print "Combo -- Maxes by Theory: "
sortedAverageTotalsRand = sorted(comboRandResults, key = lambda x: -x[1])[:numberTopTheories] # sorted by average totals, taking only the number of maxes
sortedAverageMonthlyAvgsRand = sorted(comboRandResults, key = lambda x: -x[2])[:numberTopTheories] # sorted by average averages, taking only the number of maxes

k = 0
print '{0:^24} {1:^24}'.format("Avg Total, Rand", "Avg Monthly, Rand")
while k < min(numberTopTheories, len(comboRandResults)):
    print '{0:^10} {1:^10} {2:^2d} {3:^10} {4:^10} {5:^10} {6:^2d} {7:^2d}'.format(sortedAverageTotalsRand[k][0], percentFormat(sortedAverageTotalsRand[k][1]), sortedAverageTotalsRand[k][4], sortedAverageMonthlyAvgsRand[k][0], percentFormat(sortedAverageMonthlyAvgsRand[k][2]), percentFormat(sortedAverageMonthlyAvgsRand[k][1]), sortedAverageMonthlyAvgsRand[k][3], sortedAverageMonthlyAvgsRand[k][4])
    k += 1


# end program
elapsed = timeit.default_timer() - start_time
print "\n", "Total runtime in seconds: ", elapsed, "\n"
