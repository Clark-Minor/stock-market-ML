import subprocess
import time

if __name__ == "__main__":

    keywords = ['myl','mylan','manufacturing','hydroxychloroquine','hydroxychloraquine','sulfate','nasdaq','medication']
    #("neuralink", "solar", "tesla", "@tesla", "#tesla", "tesla", "tsla", "#tsla", "elonmusk", "elon", "musk", "spacex", "starlink") #['myl','mylan','manufacturing','hydroxychloroquine','hydroxychloraquine','sulfate','nasdaq','medication']
    #['bicoin','btc','crypto','cryptocurrency','blockchain','digitalcurrency','satoshi','bitsahara','wallet','coin','ethereum','lightningcoin']

     #['s&p500','market','index','s&p','rising','falling','rise','fall','open','close','industries','stock','stocks','financial','nasdaq']
    bashCommand = "python3 sentiment.py -s TSLA -k" + keywords[0] + ','.join(keywords[1:])

    while(True):
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        time.sleep(30)
