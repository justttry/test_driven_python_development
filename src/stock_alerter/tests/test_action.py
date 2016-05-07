# encoding:UTF-8

import unittest
from mock import Mock
from mock import patch
try:
    from ..action import PrintAction
except:
    import sys
    sys.path.append('..')
    from action import PrintAction
    

########################################################################
class PrintActionTest(unittest.TestCase):
    """"""

    #----------------------------------------------------------------------
    def test_executing_action_prints_message_1(self):
        """"""
        mock_print = Mock()
        old_print = __builtins__["print"]
        __builtins__["print"] = mock_print
        try:
            action = PrintAction()
            action.execute("GOOG > $10")
            mock_print.assert_called_with("GOOG > $10")
        finally:
            __builtins__["print"] = old_print        

    #----------------------------------------------------------------------
    def test_executing_action_prints_message_2(self):
        """"""
        patcher = patch('__builtin__.print')
        mock_print = patcher.start()
        try:
            action = PrintAction()
            action.execute("GOOG > $10")
            mock_print.assert_called_with("GOOG > $10")
        finally:
            patcher.stop()          

    #----------------------------------------------------------------------
    def test_executing_action_prints_message_3(self):
        """"""
        with patch('__builtin__.print') as mock_print:
            action = PrintAction()
            action.execute("GOOG > $10")
            mock_print.assert_called_with("GOOG > $10") 

    #----------------------------------------------------------------------
    @patch('__builtin__.print')
    def test_executing_action_prints_message_4(self, mock_print):
        """"""
        action = PrintAction()
        action.execute("GOOG > $10")
        mock_print.assert_called_with("GOOG > $10")        
    

########################################################################
@patch('__builtin__.print')
class PrintActionTest2(unittest.TestCase):
    """"""

    #----------------------------------------------------------------------
    def test_executing_action_prints_message_0(self, mock_print):
        """"""
        action = PrintAction()
        action.execute("GOOG > $10")
        mock_print.assert_called_with("GOOG > $10")        
        
    
    