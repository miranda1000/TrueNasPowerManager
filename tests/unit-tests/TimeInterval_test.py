import pytest
import unittest
from src.entities.time.TimeInterval import TimeInterval
from src.entities.time.Hour import Hour
from src.entities.time.HourFactory import HourFactory

def test_time_interval_should_save_a_time_interval():
    start = Hour(hour=1, minute=0, second=0)
    end = Hour(hour=7, minute=0, second=0)

    uut = TimeInterval(start, end)

    assert uut.start == start
    assert uut.end == end

def test_time_interval_should_parse_a_time_interval_string():
    start = Hour(hour=1, minute=10, second=20)
    start_str = '01:10:20'
    end = Hour(hour=7, minute=50, second=40)
    end_str = '07:50:40'

    uut = TimeInterval(start_str, end_str)

    assert uut.start == start
    assert uut.end == end