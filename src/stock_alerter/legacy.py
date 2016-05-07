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
class AlertProcessor(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, autorun=True, exchange=None):
        """Constructor"""
        if exchange is None:
            self.exchange = {"GOOG": Stock("GOOG"),
                             "AAPL": Stock("AAPL")}
        else:
            self.exchange = exchange
        rule_1 = PriceRule("GOOG", lambda stock: stock.price > 10)
        rule_2 = PriceRule("AAPL", lambda stock: stock.price > 5)
        self.exchange["GOOG"].updated.connect(
            lambda stock: printFunc(stock.symbol, stock.price) \
            if rule_1.matches(self.exchange) else None)
        self.exchange["AAPL"].updated.connect(
            lambda stock: printFunc(stock.symbol, stock.price) \
            if rule_2.matches(self.exchange) else None)
        
        if autorun:
            self.run()

    def run(self):
        updates = []
        with open("updates.csv", "r") as fp:
            for line in fp.readlines():
                symbol, timestamp, price = line.split(",")
                updates.append((symbol,
                                datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f"),
                                int(price)))
        self.do_updates(updates)

    def do_updates(self, updates):
        for symbol, timestamp, price in updates:
            stock = self.exchange[symbol]
            stock.update(timestamp, price)