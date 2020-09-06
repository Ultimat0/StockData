class UpdateFrequency ():

    #period will typically be none because we will be providing a date range
    def __init__ (self, period: str, period_type: str, frequency: str, frequency_type: str):
        self.period = period
        self.period_type = period_type
        self.frequency = frequency
        self.frequency_type = frequency_type
    