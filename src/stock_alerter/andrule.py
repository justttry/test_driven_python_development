# encoding:UTF-8


########################################################################
class AndRule:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, *args):
        """Constructor"""
        self.rules = args
        
    #----------------------------------------------------------------------
    def matches(self, exchange):
        """"""
        return all([rule.matches(exchange) for rule in self.rules])
    