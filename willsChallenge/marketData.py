from willsChallenge import marketCrawler

class marketData:
    def __init__(self,btc={},eth={}):
        btc = {

        }

        eth = {

        }

class btcData:

    def __init__(self,kraken,val2,val3):
        self.kraken=marketCrawler.krakenCrawler.getCurrentVal(self, "btc")
        self.val2=val2
        self.val3=val3

class ethData:
    def __init__(self, kraken, val2, val3):
        self.kraken=marketCrawler.krakenCrawler.getCurrentVal(self, "eth")
        self.val2=val2
        self.val3=val3