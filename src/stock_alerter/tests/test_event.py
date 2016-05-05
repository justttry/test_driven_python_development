# encoding: UTF-8

import unittest
from mock import Mock
try:
    from ..event import Event
except:
    import sys
    sys.path.append('..')
    from event import Event
        

########################################################################
class EventTest(unittest.TestCase):
    """"""

    #----------------------------------------------------------------------
    def test_a_listener_is_notified_when_an_event_is_raised(self):
        """"""
        listener = Mock()
        event = Event()
        event.connect(listener)
        event.fire()  
        self.assertTrue(listener.called)
        
    #----------------------------------------------------------------------
    def test_a_listener_is_passed_right_parameters(self):
        """"""
        listener = Mock()
        event = Event()
        event.connect(listener)
        event.fire(5, shape="square")
        listener.assert_called_with(5, shape="square")
    