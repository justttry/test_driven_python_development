# encoding: UTF-8


import unittest
from datetime import datetime
try:
    from ..rule import PriceRule
    from ..stock import Stock
except:
    import sys
    sys.path.append('..')
    from rule import PriceRule
    from stock import Stock


########################################################################
class PriceRuleTest(unittest.TestCase):
    """"""

    @classmethod
    #----------------------------------------------------------------------
    def setUpClass(cls):
        """"""
        goog = Stock("GOOG")
        goog.update(datetime(2014, 2, 10), 11)
        cls.exchange = {"GOOG": goog}  
        
    #----------------------------------------------------------------------
    def test_a_PriceRule_matches_when_it_meets_the_condition(self):
        """"""
        rule = PriceRule("GOOG", lambda stock: stock.price > 10)
        self.assertTrue(rule.matches(self.exchange))        
    
    #----------------------------------------------------------------------
    def test_a_PriceRule_is_False_if_the_condition_is_not_met(self):
        """"""
        rule = PriceRule("GOOG", lambda stock: stock.price < 10)
        self.assertFalse(rule.matches(self.exchange))        
    
    #----------------------------------------------------------------------
    def test_a_PriceRule_is_False_if_the_stock_is_not_in_the_exchange(self):
        """"""
        rule = PriceRule("MSFT", lambda stock: stock.price > 10)
        self.assertFalse(rule.matches(self.exchange))        
    
    #----------------------------------------------------------------------
    def test_a_PriceRule_is_False_if_the_stock_hasnt_got_an_update_yet(self):
        """"""
        self.exchange["AAPL"] = Stock("AAPL")
        rule = PriceRule("AAPL", lambda stock: stock.price > 10)
        self.assertFalse(rule.matches(self.exchange))        
    
    #----------------------------------------------------------------------
    def test_a_PriceRule_only_depends_on_its_stock(self):
        """"""
        rule = PriceRule("MSFT", lambda stock: stock.price > 10)
        self.assertEqual({"MSFT"}, rule.depends_on())        