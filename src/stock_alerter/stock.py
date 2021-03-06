# encoding:UTF-8

from timeseries import TimeSeries
import bisect
import collections
from event import Event


########################################################################
class StockSignal():
    """""" 
    buy = 1
    neutral = 0
    sell = -1  

PriceEvent = collections.namedtuple("PriceEvent",
                                    ["timestamp", "price"])

########################################################################
class Stock:
    """"""
    LONG_TERM_TIMESPAN = 10
    SHORT_TERM_TIMESPAN = 5     
    
    #----------------------------------------------------------------------
    def __init__(self, symbol):
        """Constructor"""
        self.symbol = symbol
        self.history = TimeSeries()
        self.updated = Event()
    
    #----------------------------------------------------------------------
    @property
    def price(self):
        """"""
        try:
            return self.history[-1].value
        except IndexError:
            return None
    
    #----------------------------------------------------------------------
    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")  
        self.history.update(timestamp, price)
        self.updated.fire(self)
    
    #----------------------------------------------------------------------
    def is_increasing_trend(self):
        """"""
        return self.history[-3].value < self.history[-2].value  < \
               self.history[-1].value 
    
    #----------------------------------------------------------------------
    def _is_crossover_below_to_above(self, prev_ma, prev_reference_ma,
                                     current_ma, current_reference_ma):
        return prev_ma < prev_reference_ma \
               and current_ma > current_reference_ma     
    
    #----------------------------------------------------------------------
    def get_crossover_signal(self, on_date):
        """"""
        NUM_DAYS = self.LONG_TERM_TIMESPAN + 1
        closing_price_list = self.history.get_closing_price_list(on_date, NUM_DAYS)   
        
        # Return NEUTRAL signal
        if len(closing_price_list) < 11:   
            return 0        
        
        long_term_series = closing_price_list[-self.LONG_TERM_TIMESPAN:]
        prev_long_term_series = closing_price_list[-self.LONG_TERM_TIMESPAN-1:-1]
        short_term_series = closing_price_list[-self.SHORT_TERM_TIMESPAN:]
        prev_short_term_series = closing_price_list[-self.SHORT_TERM_TIMESPAN-1:-1]        
        
        long_term_ma = sum([update.value for update in long_term_series]) \
            /self.LONG_TERM_TIMESPAN        
        prev_long_term_ma = sum([update.value for update in prev_long_term_series])\
            /self.LONG_TERM_TIMESPAN        
        short_term_ma = sum([update.value for update in short_term_series])\
            /self.SHORT_TERM_TIMESPAN        
        prev_short_term_ma = sum([update.value for update in prev_short_term_series])\
            /self.SHORT_TERM_TIMESPAN        
        
        # BUY signal
        if self._is_crossover_below_to_above(prev_short_term_ma,
                                             prev_long_term_ma,
                                             short_term_ma,
                                             long_term_ma):
            return StockSignal.buy
        
        # BUY signal
        if self._is_crossover_below_to_above(prev_long_term_ma,
                                             prev_short_term_ma,
                                             long_term_ma,
                                             short_term_ma):
            return StockSignal.sell    
        
        # NEUTRAL signal
        return StockSignal.neutral 