from willsChallenge import marketCrawler

class marketData:
    def __init__(self,btc={},eth={}):
        btc = {

        }

        eth = {

        }

class btcData:

    def __init__(self,kraken,bitrex,bitstamp):
        self.kraken=marketCrawler.krakenCrawler.getCurrentVal(self, "btc")
        self.bitrex=marketCrawler.bitrexCrawler.getCurrentVal(self,"btc")
        self.bitstamp=marketCrawler.bitrexCrawler.getCurrentVal(self,"btc")

class ethData:
    def __init__(self, kraken, bitrex, bitstamp):
        self.kraken=marketCrawler.krakenCrawler.getCurrentVal(self, "eth")
        self.bitrex=marketCrawler.bitrexCrawler.getCurrentVal(self,"eth")
        self.bitstamp=marketCrawler.bitstampCrawler.getCurrentVal(self,"eth")