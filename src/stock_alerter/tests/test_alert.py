# encoding:UTF-8


import unittest
from datetime import datetime
from mock import Mock
from mock import MagicMock

try:
    from ..alert import Alert
    from ..rule import PriceRule
    from ..stock import Stock
except:
    import sys
    sys.path.append('..')
    from alert import Alert
    from rule import PriceRule
    from stock import Stock


########################################################################
class TestAction:
    """"""
    executed = False

    #----------------------------------------------------------------------
    def execute(self, description):
        """Constructor"""
        self.executed = True


########################################################################
class AlertTest(unittest.TestCase):
    """"""

    #----------------------------------------------------------------------
    def test_action_is_executed_when_rule_matches(self):
        """"""
        exchange = {"GOOG": Stock("GOOG")}
        rule = PriceRule("GOOG", lambda stock: stock.price > 10)
        action = MagicMock()
        alert = Alert("sample alert", rule, action)
        alert.connect(exchange)
        exchange["GOOG"].update(datetime(2014, 2, 10), 11)
        action.execute.assert_called_with("sample alert")   
        
    #----------------------------------------------------------------------
    def test_action_is_executed_when_rule2_matches(self):
        """"""
        exchange = {"GOOG": Stock("GOOG")}
        rule = MagicMock(spec=PriceRule)
        rule.matches.return_value = True
        rule.depends_on.return_value = {"GOOG"}
        action = MagicMock()
        alert = Alert("sample alert", rule, action)
        alert.connect(exchange)
        exchange["GOOG"].update(datetime(2014, 2, 10), 11)
        action.execute.assert_called_with("sample alert")        
    
    
        
    
    