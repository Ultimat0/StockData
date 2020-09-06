import unittest

from TradingStrategy import TradingStrategy
from Types import *

from datetime import datetime

#TODO uh write tests lol
class TradingStrategyTestCase (unittest.TestCase):

    def test_get_price_data (self):
        start_date = datetime(2020, 6, 1, 0, 0, 0)
        end_date = datetime(2020, 8, 1, 0, 0, 0)
        ts = TradingStrategy ("MSFT", 5000, UpdateFrequency.PER_MINUTE, NN_Params(), 
            DateRange(DateRange.convert_to_millis_since_epoch(start_date), DateRange.convert_to_millis_since_epoch(end_date)))
