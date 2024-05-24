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
    
def test_time_interval_should_check_if_an_hour_is_within():
    start = Hour(hour=1, minute=0, second=0)
    end = Hour(hour=7, minute=0, second=0)

    check_within = Hour(hour=2, minute=0, second=0)
    check_outside = Hour(hour=23, minute=0, second=0)
    check_min_margin = start
    check_max_margin = end

    uut = TimeInterval(start, end)

    assert uut.is_within(check_within), \
            f"Expected {check_within} to be within margins; got otherwise instead"
    assert not uut.is_within(check_outside), \
            f"Expected {check_outside} to be outside margins; got otherwise instead"
    assert uut.is_within(check_min_margin), \
            f"Expected {check_min_margin} to be within margins; got otherwise instead"
    assert uut.is_within(check_max_margin), \
            f"Expected {check_max_margin} to be within margins; got otherwise instead"