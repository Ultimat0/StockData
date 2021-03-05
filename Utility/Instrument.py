import Config

import requests
from requests import HTTPError

from DateRange import DateRange
from datetime import datetime
from datetime import timedelta

import json
from typing import Generator

from tempfile import TemporaryFile

import re

class Instrument:

    def __init__ (self, symbol: str):
        self.symbol = symbol
        self.__fundamentals = {}
        self.CIK = None

    def populate (self):
        url = "https://api.tdameritrade.com/v1/instruments"
        params = {
            "apikey": Config.API_KEY,
            "symbol": self.symbol,
            "projection": "fundamental"
        }
        try:
            req = requests.get(url, params=params)
            f = json.loads(req.content)
            if f:
                self.__fundamentals = f[self.symbol]["fundamental"]
            else:
                raise Exception("Population failed: That instrument does not exist")
            req = requests.get("https://www.sec.gov/include/ticker.txt")
            exp = self.symbol.lower() + r"\s\d+"
            self.CIK = re.search(exp, str(req.content, "utf-8")).group().split("\t")[1]
        except HTTPError:
            print ("Popoulation failed: HTTPError")
    
    def get_fundamentals (self):
        if self.__fundamentals:
            return self.__fundamentals
        else:
            print (f'Populating for symbol: {self.symbol}')
            self.populate()
            return self.__fundamentals

    #TODO: Add customization to needExtendedHoursData. Idk where it should go rn
    def get_price_data (self, date_range: DateRange) -> Generator[str, None, None]:
        if not self.__fundamentals:
            print (f'Populating for symbol: {self.symbol}')
            self.populate()
        print (DateRange.convert_to_millis_since_epoch(date_range.start_date))
        print (DateRange.convert_to_millis_since_epoch(date_range.end_date))
        date_array = [i for i in date_range]
        url = f"https://api.tdameritrade.com/v1/marketdata/{self.__fundamentals['symbol']}/pricehistory"
        params = {
            "apikey": Config.API_KEY,
            "periodType": self.update_frequency.period_type,
            "frequencyType": self.update_frequency.frequency_type,
            "frequency": self.update_frequency.frequency,
            "startDate": str(DateRange.convert_to_millis_since_epoch(date_range.start_date)),
            "endDate": str(DateRange.convert_to_millis_since_epoch(date_range.end_date)),
            "needExtendedHoursData": "false"
        }
        req = requests.get(url, params=params)
        req.raise_for_status()
        return req.content.decode('utf-8')

    """def get_document (document_id: str) -> TemporaryFile:
        temp_file = TemporaryFile()
        requests.get("FIGURE OUT LATER", stream=True)
        for chunk in r.iter_content(chunk_size=256)
            if chunk:
                temp_file.write(chunk)
        return temp_file"""
        

apha = Instrument("WRB-C")
#for i in apha.get_price_data(DateRange(datetime(2020, 7, 1, 0, 0, 0), datetime(2020, 7, 30, 0, 0, 0))):
#    print (i)
print(apha.get_fundamentals())
print(apha.CIK)
