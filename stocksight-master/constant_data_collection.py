import subprocess
import time

if __name__ == "__main__":

    tickers = ['MYL','TSLA','BTC','^GSPC','KSS','DDS','NTAP','DAL','AEO']
    keywords = [['myl','mylan','manufacturing','hydroxychloroquine','hydroxychloraquine','sulfate','nasdaq','medication'],
    ["neuralink", "solar", "tesla", "@tesla", "#tesla", "tesla", "tsla", "#tsla", "elonmusk", "elon", "musk", "spacex", "starlink"],
    ['bicoin','btc','crypto','cryptocurrency','blockchain','digitalcurrency','satoshi','bitsahara','digitalwallet','digitalcoin','ethereum','dogecoin'],
    ['s&p500','index','s&p','bear','bull','rising','falling','marketopen','marketclose','industries','stock','stocks','financial','nasdaq','top500','stockmarket','djia','dowjones','industrialaverage'],
    ["kss","kohl's","kohls","shop","clothes","deals","reward","#lovekohls","clothing","handbags","cosmetics","beauty","department","shopping","leadership","sales","profit","shutdown","stores","retail","sephora","ultabeauty"],
    ["dds","dillards","shop","designer","dresses","shoes","clothing","handbags","cosmetics","beauty","bedding","wedding","registry","department","shopping","stores","retail"],
    ["netapp", "#hybridcloud", "ntap", "georgekurian", "#datadriven", "netappassist"],
    ["airlines", "delta", "deltaairlines", "#delta", "travel","airtravel", "airplaines", "dal"],
    ["clothing", "department", "store", "americaneagle", "AEO", "#americaneagle","fashion", "mall","malls"]]

    while(True):
        for i in range(len(tickers)):
            bashCommand = "python3 sentiment.py -s" + tickers[i] + " -k" + keywords[i][0] + ','.join(keywords[i][1:]) + "--overridetokensreq" + keywords[i][0] + ','.join(keywords[i][1:]) + "--upload"
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()

        time.sleep(30)
