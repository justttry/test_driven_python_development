# encoding:UTF-8

import unittest
from datetime import datetime
import mock
from mock import Mock
from mock import patch
try:
    from ..legacy import AlertProcessor
except:
    import sys
    sys.path.append('..')
    from legacy import AlertProcessor
    

########################################################################
class AlertProcessorTest(unittest.TestCase):
    """"""

    #----------------------------------------------------------------------
    @patch('__builtin__.print')
    def test_processor_characterization_1(self, mock_print):
        """Constructor"""
        AlertProcessor()
        mock_print.assert_has_calls([mock.call("AAPL", 8),
                                     mock.call("GOOG", 15),
                                     mock.call("AAPL", 10),
                                     mock.call("GOOG", 21)])   

    #----------------------------------------------------------------------
    def test_processor_characterization_2(self):
        """Constructor"""
        processor = AlertProcessor(autorun=False)
        with patch("__builtin__.print") as mock_print:
            processor.run()
        mock_print.assert_has_calls([mock.call("AAPL", 8),
                                     mock.call("GOOG", 15),
                                     mock.call("AAPL", 10),
                                     mock.call("GOOG", 21)])  

    #----------------------------------------------------------------------
    def test_processor_characterization_3(self):
        """Constructor"""
        processor = AlertProcessor(autorun=False)
        mock_goog = Mock()
        processor.exchange = {"GOOG": mock_goog}
        updates = [("GOOG", datetime(2014, 12, 8), 5)]
        processor.do_updates(updates)
        mock_goog.update.assert_called_with(datetime(2014, 12, 8), 5)

    #----------------------------------------------------------------------
    def test_processor_characterization_4(self):
        """Constructor"""
        mock_goog = Mock()
        mock_aapl = Mock()
        exchange = {"GOOG": mock_goog, "AAPL": mock_aapl}
        processor = AlertProcessor(autorun=False, exchange=exchange)
        updates = [("GOOG", datetime(2014, 12, 8), 5)]
        processor.do_updates(updates)
        mock_goog.update.assert_called_with(datetime(2014, 12, 8), 5)
    
    #----------------------------------------------------------------------
    def test_processor_characterization_5(self):
        """"""
        mock_goog = Mock()
        mock_aapl = Mock()
        exchange = {"GOOG": mock_goog, "AAPL": mock_aapl}
        processor = TestAlertProcessor(exchange)
        updates = [("GOOG", datetime(2014, 12, 8), 5)]
        processor.do_updates(updates)
        mock_goog.update.assert_called_with(datetime(2014, 12, 8), 5)
        
    #----------------------------------------------------------------------
    def test_processor_characterization_6(self):
        """"""
        processor = AlertProcessor(autorun=False)
        processor.do_updates = Mock()
        processor.run()
        processor.do_updates.assert_called_with([
            ('GOOG', datetime(2014, 2, 11, 14, 10, 22, 130000), 5),
            ('AAPL', datetime(2014, 2, 11, 0, 0), 8),
            ('GOOG', datetime(2014, 2, 11, 14, 11, 22, 130000), 3),
            ('GOOG', datetime(2014, 2, 11, 14, 12, 22, 130000), 15),
            ('AAPL', datetime(2014, 2, 11, 0, 0), 10),
            ('GOOG', datetime(2014, 2, 11, 14, 15, 22, 130000), 21)])        
        
    
########################################################################
class TestAlertProcessor(AlertProcessor):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, exchange):
        """Constructor"""
        #AlertProcessor.__init__(self, autorun=False)
        super(TestAlertProcessor, self).__init__(autorun=False)
        self.exchange = exchange        