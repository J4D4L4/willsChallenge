import requests
import json

from abc import ABC, abstractmethod

class crawler(ABC):
    def getRequestData(self):
        pass
    def getRequest(self):
        pass
    def getMarketValResult(self):
        pass
    def getCurrentVal(self):
        pass

class krakenCrawler(crawler):
    def getConnection(self):
        return self

    def getRestCall(self):
        #response=requests.post(url,data)
        return self
    def getRequestData(self,type):
        requests={
            'btc': 'https://api.kraken.com/0/public/Ticker?pair=XBTUSD',
            'eth': 'https://api.kraken.com/0/public/Ticker?pair=ETHUSD'
        }

        return requests[type]
    def getRequest(self,url):
        requestData=json.loads(requests.get(url).text)
        return requestData

    def getMarketValResult(self, krakenRequestJson):
        result = krakenRequestJson["result"]
        returnVal = next(iter(result.values()))["c"]
        return returnVal
    def getCurrentVal(self,symbol):
        currentSymbolVal = krakenCrawler.getMarketValResult(self, krakenCrawler.getRequest(self, krakenCrawler.getRequestData(self, symbol)))
        return currentSymbolVal[0]

class bitrexCrawler(crawler):
    def getRequestData(self, type):
        requests = {
            'btc': 'https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC',
            'eth': 'https://api.bittrex.com/api/v1.1/public/getticker?market=USD-ETH'
        }
        return requests[type]
    def getRequest(self,url):
        requestData=json.loads(requests.get(url).text)
        return requestData
    def getMarketValResult(self, bitrexRequestJson):
        result = bitrexRequestJson["result"]
        returnVal = result["Last"]
        return returnVal
    def getCurrentVal(self,symbol):
        currentSymbolVal = bitrexCrawler.getMarketValResult(self, bitrexCrawler.getRequest(self, bitrexCrawler.getRequestData(self, symbol)))
        return currentSymbolVal

class bitstampCrawler(crawler):

    def getRequestData(self, type):
        requests = {
            'btc': 'https://www.bitstamp.net/api/v2/ticker/btcusd/',
            'eth': 'https://www.bitstamp.net/api/v2/ticker/ethusd/'
        }
        return requests[type]

    def getRequest(self,url):
        requestData=json.loads(requests.get(url).text)
        return requestData

    def getMarketValResult(self, bitrexRequestJson):
        result = bitrexRequestJson
        returnVal = result["last"]
        return returnVal

    def getCurrentVal(self,symbol):
        currentSymbolVal = bitstampCrawler.getMarketValResult(self, bitstampCrawler.getRequest(self, bitstampCrawler.getRequestData(self, symbol)))
        return currentSymbolVal