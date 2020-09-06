from datetime import datetime
from datetime import timedelta

EPOCH_DATE = datetime(1969, 12, 31, 0, 0, 0) # This is the magic date that acts as the beginning of time for TD Ameritrade

class DateRange:

    def __init__ (self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date

    #static method to convert TD Ameritrade datetimes to stockbot datetimes
    def convert_from_td_datetime (td_datetime: str) -> datetime:
        #Ameritrade datetimes come like this: "2002-01-17 00:00:00.000" from least precise to most
        date_components = td_datetime.split(" ")[0].split("-")
        time_components = td_datetime.split(" ")[1].split(":") # The third element (time_components[2]) is seconds then milliseconds separated by a "."
        return datetime (int(date_components[0]), int(date_components[1]), int(date_components[2]), int(time_components[0]), 
            int(time_components[1]), int(time_components[2].split(".")[0]), int(time_components[2].split(".")[1]) * 1000) # multiply by 1000 to convert milliseconds to microseconds

    #Factory method to create stockbot datetime from 2 TD Ameritrade datetime strings
    def from_td_date_range (td_start_date: str, td_end_date: str): #-> DateRange
        return DateRange(DateRange.convert_from_td_datetime(td_start_date), DateRange.convert_from_td_datetime(td_end_date))

    def convert_to_millis_since_epoch (date: datetime) -> int:
        delta = date - EPOCH_DATE
        return delta.days * 86400000 + delta.seconds * 1000 + delta.microseconds // 1000 # apparently time deltas only store days, seconds, and microseconds lol

    def __iter__ (self):
        self.cur_iter_date = self.start_date
        return self
    
    def __next__ (self):

        temp = self.cur_iter_date

        if self.cur_iter_date > self.end_date:
            raise StopIteration

        self.cur_iter_date = self.cur_iter_date + timedelta(days=1)
        return temp

if __name__ == "__main__":
    print (DateRange.convert_to_millis_since_epoch(datetime(2020, 6, 1, 0, 0, 0)))
    print (DateRange.convert_to_millis_since_epoch(datetime(2020, 6, 23, 0, 0, 0)))
