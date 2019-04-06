import unittest
from willsChallenge import marketData

class TestMarketData(unittest.TestCase):

    def test___init__(self):
        marketDataInst = marketData.marketData()

        self.assertIsNotNone(marketData)

class TestBtcData(unittest.TestCase):
    def test___init__(self):
        btcDataInit = marketData.btcData(0,0,0)
        self.assertIsNotNone(btcDataInit)
        self.assertNotEqual(btcDataInit.kraken, 0)
class TestETHData(unittest.TestCase):
    def test___init__(self):
        ethDataInit = marketData.ethData(0,0,0)
        self.assertIsNotNone(ethDataInit)
        self.assertNotEqual(ethDataInit.kraken,0)