import requests

from Utility.DateRange import DateRange
from Utility.UpdateFrequency import UpdateFrequency
from Utility.NN_Params import NN_Params

import Utility.Config

from datetime import datetime
from datetime import timedelta

from typing import Generator
import json

class TradingStrategy():

    def __init__ (self, ticker: str, initial_amount: int, update_frequency: UpdateFrequency, nn_params: NN_Params, training_date_range: DateRange, test_date_range: DateRange):
        self.ticker = ticker
        self.initial_amount = initial_amount
        self.update_frequency = update_frequency
        self.training_date_range = training_date_range
        self.test_date_range = test_date_range

    #TODO: Add customization to needExtendedHoursData. Idk where it should go rn
    def get_price_data (self, date_range: DateRange) -> Generator[str, None, None]:
        print (DateRange.convert_to_millis_since_epoch(date_range.start_date))
        print (DateRange.convert_to_millis_since_epoch(date_range.end_date))
        date_array = [i for i in date_range]
        #for date in date_array[::10]:
        url = f"https://api.tdameritrade.com/v1/marketdata/{self.ticker}/pricehistory"
        params = {
            "apikey": Utility.Config.API_KEY,
            "periodType": self.update_frequency.period_type,
            "frequencyType": self.update_frequency.frequency_type,
            "frequency": self.update_frequency.frequency,
            "startDate": str(DateRange.convert_to_millis_since_epoch(date_range.start_date)),
            "endDate": str(DateRange.convert_to_millis_since_epoch(date_range.end_date)),
            "needExtendedHoursData": "false"
        }
        req = requests.get(url, params=params)
        print (req.status_code)
        req.raise_for_status()
        return req.content.decode('utf-8')

    def get_fundamentals (self):
        #So this appears to be an enormous pain in the butt.
        #The SEC keeps all the financial data I need, but their website is old,
        #and I haven't figured out how it's organized. It's certainly not by
        #ticker. Will delve when I'm less tired
        #https://www.sec.gov/developer
        print ("TODO")

    def train (self):
        print ("TODO")

    def test (self):
        print ("TODO")

ts = TradingStrategy("TLT", 5000, UpdateFrequency(None, "day", "1", "minute"), [16, 16], DateRange(datetime(2020, 7, 1, 0, 0, 0), datetime(2020, 7, 30, 0, 0, 0)), (10, 15))

ts.get_price_data(ts.training_date_range)
#print(json.loads(ts.get_price_data(ts.training_date_range))["candles"])


