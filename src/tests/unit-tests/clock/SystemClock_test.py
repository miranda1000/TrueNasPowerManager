import pytest
import unittest
from time import sleep

from clock.SystemClock import SystemClock

def test_system_clock_increments():
    clock = SystemClock()

    start = clock.get_current_hour()
    print(f"[i] Starting at {start}")

    sleep(2)

    end = clock.get_current_hour()
    print(f"[i] Ending at {end}")

    if start.hour == 23 and end.hour == 0:
        pytest.skip("Running the test between days - This test will fail")

    assert end > start, \
        "Expected to end later than the start"