import unittest
import blockchain
import json
from willsChallenge import marketCrawler

class TestKrakenMarketCrawler(unittest.TestCase):


    def test_getConnections(self):
        result = marketCrawler.krakenCrawler.getConnection(self)
        self.assertIsNotNone(result)

    def test_getRestCall(self):
        result = marketCrawler.krakenCrawler.getRestCall(self)
        self.assertIsNotNone(result)
    def test_getReqeuestData(self):
        type="btc"
        resultBTC=marketCrawler.krakenCrawler.getRequestData(self, type)
        self.assertEqual(resultBTC,'https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        resultETH=marketCrawler.krakenCrawler.getRequestData(self, "eth")
        self.assertEqual(resultETH,'https://api.kraken.com/0/public/Ticker?pair=ETHUSD')

    def test_getRequest(self):
        result = marketCrawler.krakenCrawler.getRequest(self, marketCrawler.krakenCrawler.getRequestData(self, "eth"))
        self.assertIsNotNone(result['result'])

    def test_getKrakenMarketValResult(self):
        request = marketCrawler.krakenCrawler.getRequest(self, marketCrawler.krakenCrawler.getRequestData(self, "eth"))
        result = marketCrawler.krakenCrawler.getMarketValResult(self, request)
        self.assertIsNotNone(result)

    def test_getCurrentVal(self):
        resultEth = marketCrawler.krakenCrawler.getCurrentVal(self, "eth")
        resultBtc = marketCrawler.krakenCrawler.getCurrentVal(self, "btc")
        self.assertIsNotNone(resultBtc)
        self.assertIsNotNone(resultEth)
class TestBittrexMarketCrawler(unittest.TestCase):

    def test_getReqeuestData(self):
        type="btc"
        resultBTC=marketCrawler.bitrexCrawler.getRequestData(self, type)
        self.assertEqual(resultBTC,'https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC')
        resultETH=marketCrawler.bitrexCrawler.getRequestData(self, "eth")
        self.assertEqual(resultETH,'https://api.bittrex.com/api/v1.1/public/getticker?market=USD-ETH')
    def test_getRequest(self):
        result = marketCrawler.bitrexCrawler.getRequest(self, marketCrawler.bitrexCrawler.getRequestData(self, "eth"))
        self.assertIsNotNone(result['result'])




