# encoding:UTF-8

import unittest
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
        
    
    