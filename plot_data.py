# python libraries
import sys
import os
import ssl
import csv
openssl_dir, openssl_cafile = os.path.split(
    ssl.get_default_verify_paths().openssl_cafile)
# no content in this folder
os.listdir(openssl_dir)
from datetime import datetime

# numpy libraries
import numpy as np

# matplotlib libraries
import matplotlib as mpl
import matplotlib.pyplot as plt

#urllib libraries
from urllib import request

######################################################################
# global settings
######################################################################

mpl.lines.width = 2
mpl.axes.labelsize = 14


######################################################################
# functions
######################################################################
def scrapeLastTwoYearsData(otherTicker):

    otherURL = "https://query1.finance.yahoo.com/v7/finance/download/{}?period1=1521590400&period2=1584748800&interval=1d&events=history".format(otherTicker)
    print(otherURL)
    spURL = "https://query1.finance.yahoo.com/v7/finance/download/^GSPC?period1=1521590400&period2=1584748800&interval=1d&events=history"

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    spDataCsv = request.urlopen(spURL, context=ctx).read()
    spcsvstr = str(spDataCsv).strip("b'")
    lines = spcsvstr.split("\\n")
    spfile = open("./last-two-years/last-two-years-sp500.csv", "w")
    for line in lines:
       spfile.write(line + "\n")
    spfile.close()


    otherDataCsv = request.urlopen(otherURL, context = ctx).read()
    othercsvstr = str(otherDataCsv).strip("b'")
    lines = othercsvstr.split("\\n")
    otherfile = open("./last-two-years/last-two-years-{}.csv".format(otherTicker), "w")
    for line in lines:
       otherfile.write(line + "\n")
    otherfile.close()

    return "./last-two-years/last-two-years-sp500.csv", "./last-two-years/last-two-years-{}.csv".format(otherTicker)

def scrape2007to2009Data(otherTicker):

    otherURL = "https://query1.finance.yahoo.com/v7/finance/download/{}?period1=1169337600&period2=1232496000&interval=1d&events=history".format(otherTicker)
    spURL = "https://query1.finance.yahoo.com/v7/finance/download/^GSPC?period1=1169337600&period2=1232496000&interval=1d&events=history"

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    spDataCsv = request.urlopen(spURL, context=ctx).read()
    spcsvstr = str(spDataCsv).strip("b'")
    lines = spcsvstr.split("\\n")
    spfile = open("2007-2009/2007-2009-sp500.csv", "w")
    for line in lines:
       spfile.write(line + "\n")
    spfile.close()


    otherDataCsv = request.urlopen(otherURL, context = ctx).read()
    othercsvstr = str(otherDataCsv).strip("b'")
    lines = othercsvstr.split("\\n")
    otherfile = open("2007-2009/2007-2009-{}.csv".format(otherTicker), "w")
    for line in lines:
       otherfile.write(line + "\n")
    otherfile.close()

    return "2007-2009/2007-2009-sp500.csv", "2007-2009/2007-2009-{}.csv".format(otherTicker)

def plot_ticker_vs_sp500(spDataPath, otherCompanyDataPath, otherCompanyName, timeframe, month_start):
    other_csv = list(csv.DictReader(open(spDataPath)))
    sp_csv = list(csv.DictReader(open(otherCompanyDataPath)))
    #print(other_csv)

    x1, y1, x2, y2 = [], [], [], []
    base_price_1 = (float(other_csv[0]['Adj Close']) -float(other_csv[0]['Open'])) / float(other_csv[0]['Open'])
    base_price_2 = (float(sp_csv[0]['Adj Close']) -float(sp_csv[0]['Open'])) / float(sp_csv[0]['Open'])
    for row in other_csv:
        date = str(row['Date'])
        x1.append(date)
        #FMT =  '%Y-%m-%d'
        weekday = datetime.strptime(date, '%Y-%m-%d')
        weekday = weekday.weekday()
        #print(weekday)
        percent_gain_daily = (float(row['Adj Close']) -float(row['Open'])) / float(row['Open'])
        if(weekday == 4):
            while weekday < 6:
                x1.append('any string')
                y1.append(percent_gain_daily + base_price_1)
                weekday += 1
        y1.append(percent_gain_daily)
    for row in sp_csv:
        date = str(row['Date'])
        x2.append(date)
        #FMT = '%Y-%m-%d'
        weekday = datetime.strptime(date, '%Y-%m-%d')
        weekday = weekday.weekday()
        percent_gain_daily = (float(row['Adj Close']) -float(row['Open'])) / float(row['Open'])
        if(weekday == 4):
            while weekday < 6:
                x2.append('any string')
                y2.append(percent_gain_daily + base_price_2)
                weekday += 1
        y2.append(percent_gain_daily)


    plt.plot(range(len(y1)), y1, 'r', label=otherCompanyName)
    plt.plot(range(len(y2)), y2, 'b', label='S&P500')
    plt.xlabel('')



    plt.title('Market Value of {} vs S&P500 Index from {}'.format(otherCompanyName,timeframe))
    plt.ylabel('Market Value')
    #print(x1)
    month_intervals = []
    for i in range(24):
        month_intervals.append(31*i)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec',
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    months = months[month_start-1:] + months[0:month_start-1]
    plt.xticks(month_intervals, months)
    plt.legend()
    plt.show()

def plot_ticker(otherTicker, otherCompanyName, timeframe, month_start):
    _, otherCompanyDataPath = scrapeLastTwoYearsData(otherTicker)
    other_csv = list(csv.DictReader(open(otherCompanyDataPath)))
    #print(other_csv)

    x1, y1 = [], []
    base_price_1 = (float(other_csv[0]['Adj Close']))
    for row in other_csv:
        date = str(row['Date'])
        x1.append(date)
        #FMT =  '%Y-%m-%d'
        weekday = datetime.strptime(date, '%Y-%m-%d')
        weekday = weekday.weekday()
        #print(weekday)
        #dollar_gain_daily = (float(row['Adj Close']) - float(row['Open']))
        if(weekday == 4):
            while weekday < 6:
                x1.append('any string')
                y1.append(float(row['Adj Close']))
                weekday += 1
        y1.append(float(row['Adj Close']))

    plt.plot(range(len(y1)), y1, 'r', label=otherCompanyName)
    plt.xlabel('Month')
    plt.ylabel('Value (US Dollars)')
    month_intervals = []
    for i in range(24):
        month_intervals.append(31*i)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec',
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    months = months[month_start-1:] + months[0:month_start-1]
    plt.xticks(month_intervals, months)
    plt.title('{} performance over the past 2 years'.format(otherCompanyName))
    plt.legend()
    plt.show()


def plot_ticker_vs_sp500_present_and_historic(otherTicker, otherCompanyName):

    ##############
    # parameters:
    # otherTicker: string, name of ticker
    # otherCompanyName: string, name of the company associated with the ticker

    spDataPath, otherCompanyDataPath = scrapeLastTwoYearsData(otherTicker)
    plot_ticker_vs_sp500(spDataPath,otherCompanyDataPath, otherCompanyName, "March 2018 to March 2020", 3)
    #spDataPath, otherCompanyDataPath = scrape2007to2009Data(otherTicker)
    #plot_ticker_vs_sp500(spDataPath,otherCompanyDataPath,otherCompanyName, "Jan 2007 to Jan 2009",1)


def plot_ticker_performance(otherTicker, otherCompanyName):
    plot_ticker(otherTicker, otherCompanyName, "March 2018 to March 2020", 3);
    plot_ticker_vs_sp500_present_and_historic(otherTicker, otherCompanyName)



if __name__ == "__main__":
    outperforming_tickers = ['LSI', 'UNM', 'KSS', 'PETS', 'WGO', 'PFG', 'DAL', 'LNC', 'AEO', 'IPG', 'DHI', 'CLF', 'WHR', 'DDS', 'CCL', 'BWA', 'GWW', 'FLWS', 'BIG', 'PBI', 'XRX', 'IR', 'NTAP', 'MYL']
    for ticker in outperforming_tickers:
        plot_ticker_performance(ticker, ticker)
    # if len(sys.argv) == 5:
    #     plot_ticker_vs_ticker(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
