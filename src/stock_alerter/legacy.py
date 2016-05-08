from datetime import datetime
try:
    from .stock import Stock
    from .rule import PriceRule
except:
    from stock import Stock
    from rule import PriceRule
    

#----------------------------------------------------------------------
def printFunc(symbol, price):
    """"""
    __builtins__['print'](symbol, price)
    

########################################################################
class FileReader:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, filename):
        """Constructor"""
        self.filename = filename
        
    #----------------------------------------------------------------------
    def get_updates(self):
        """"""
        updates = []
        with open("updates.csv", "r") as fp:
            for line in fp.readlines():
                symbol, timestamp, price = line.split(",")
                updates.append((symbol,
                                datetime.strptime(timestamp,
                                                  "%Y-%m-%dT%H:%M:%S.%f"), 
                                int(price)))
        return updates     
    
    
########################################################################
class AlertProcessor(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, autorun=True, reader=None, exchange=None):
        """Constructor"""
        self.reader = reader if reader else FileReader("updates.csv")
        if exchange is None:
            self.exchange = {"GOOG": Stock("GOOG"),
                             "AAPL": Stock("AAPL")}
        else:
            self.exchange = exchange
        rule_1 = PriceRule("GOOG", lambda stock: stock.price > 10)
        rule_2 = PriceRule("AAPL", lambda stock: stock.price > 5)
        self.exchange["GOOG"].updated.connect(
            lambda stock: self.print_action(stock, rule_1))
        self.exchange["AAPL"].updated.connect(
            lambda stock: self.print_action(stock, rule_2))
        
        if autorun:
            self.run()
    
    def print_action(self, stock, rule):
        printFunc(stock.symbol, stock.price) \
                    if rule.matches(self.exchange) else None        

    def run(self):
        updates = self.reader.get_updates()
        self.do_updates(updates)

    def do_updates(self, updates):
        for symbol, timestamp, price in updates:
            stock = self.exchange[symbol]
            stock.update(timestamp, price)