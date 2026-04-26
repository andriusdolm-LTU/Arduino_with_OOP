import pytest
from unittest.mock import MagicMock
from OOP_Arduino import Ismanus_Projektas, LED

def test_singleton():
    p1 = Ismanus_Projektas()
    p2 = Ismanus_Projektas()
    assert p1 is p2

def test_led_ijungimas():
    mock_board = MagicMock()
    led1 = LED(mock_board, 11)
    led1.on()
    led1._pin.write.assert_called_with(1)
    led2 = LED(mock_board, 10)
    led2.on()
    led2._pin.write.assert_called_with(1)
    led3 = LED(mock_board, 9)
    led3.on()
    led3._pin.write.assert_called_with(1)

def test_led_isjungimas():
    mock_board = MagicMock()
    led1 = LED(mock_board, 11)
    led1.off()
    led1._pin.write.assert_called_with(0)
    led2 = LED(mock_board, 10)
    led2.off()
    led2._pin.write.assert_called_with(0)
    led3 = LED(mock_board, 9)
    led3.off()
    led3._pin.write.assert_called_with(0)

def test_led_ryskumas():
    mock_board = MagicMock()
    led1 = LED(mock_board, 11)
    test_ryskumas = 5
    led1.led_ryskumas(test_ryskumas)
    led1._pin.write.assert_called_with(test_ryskumas)
    led2 = LED(mock_board, 10)
    led2.led_ryskumas(test_ryskumas)
    led2._pin.write.assert_called_with(test_ryskumas)
    led3 = LED(mock_board, 9)
    led3.led_ryskumas(test_ryskumas)
    led3._pin.write.assert_called_with(test_ryskumas)