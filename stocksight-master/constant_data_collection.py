import subprocess
import time
from random import randint
from config import *

if __name__ == "__main__":

    tickers = ['MYL','TSLA','BTC','^GSPC','KSS','DDS','NTAP','DAL','AEO','CLF','DHI','IR','ETC','XRP']
    keywords = [['myl','mylan','manufacturing','hydroxychloroquine','hydroxychloraquine','sulfate','nasdaq','medication','#hydroxychloroquine','ramping','production','tablets','200mg'],
    ["neuralink", "solar", "tesla", "@tesla", "#tesla", "tesla", "tsla", "#tsla", "elonmusk", "elon", "musk", "spacex", "starlink"],
    ['bitcoin','btc','crypto','cryptocurrency','blockchain','digitalcurrency','satoshi','bitsahara','digitalwallet','digitalcoin','ethereum','dogecoin','#crypto','#bitcoin'],
    ['s&p500','index','s&p','bear','bull','rising','falling','marketopen','marketclose','industries','stock','stocks','financial','nasdaq','top500','stockmarket','djia','dowjones','industrialaverage'],
    ["kss","kohl's","kohls","clothes","deals","reward","#lovekohls","clothing","handbags","cosmetics","beauty","department","shopping","leadership","sales","profit","shutdown","stores","retail","sephora","ultabeauty"],
    ["dds","dillards","designer","dresses","shoes","clothing","handbags","cosmetics","beauty","bedding","wedding","registry","department","shopping","retail"],
    ["netapp", "#hybridcloud", "ntap", "@georgekurian", "#datadriven", "netappassist","#storagemanagement","hybrid-flash","#netapp","#saas","@netappcloud"],
    ["airlines", "delta", "deltaairlines", "#delta","#flydelta", "travel","airtravel", "airplanes", "dal"],
    ["clothing", "department", "store", "americaneagle", "aeo","#aeo", "#americaneagle","fashion", "mall","malls"],
    ["clf","cleveland-cliffs","cleveland","mining","essentialbusiness","(nyse:clf)","steel","futures","hbi","iron", "ore"],
    ["dhi","$dhi","#dhi","horton","@drhorton","homes","builder","@kbhome","housing","pandemic","affordable"],
    ["ir","thermo","trane","ingersoll","#ingersollrand","cooling","refrigeration","#heatpump","hvac"],
    ["etc","ethereum","btc","#etc","ethereumcoin","gitcoin","#blockchain","#solidity","#crypto","#ccryptocurrency"],
    ["xrp","$xrp","#xrp","#xrpthestandard","#fedsisdead","#xrpcommmunity","#xrpusd","ripple","#ripplenet","ripplenet","deemoney","@randizuckerberg","@azimo" ]]

    while(True):
        #randomly decide which of the stocks to investigate next after there is no more data to mine for a given stock
        i = randint(0,len(tickers)-1)
        for numruns in range(4):
            bashCommand = "python3 sentiment.py -s" + tickers[i] + " -k" + keywords[i][0] + ','.join(keywords[i][1:])
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()

        time.sleep(30)
