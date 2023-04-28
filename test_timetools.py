# TEST FOR MODULE TIMETOOLS.PY

# Lets import module to be tested
import timetools

# UNIT TESTS DEFINITIONS

def test_dateiff():
    assert timetools.datediff("2023-04-28","2023-04-10") == 18