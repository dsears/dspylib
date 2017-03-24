from dspylib.date import time_units_from_seconds

def test_time_units_from_seconds():
  assert time_units_from_seconds(0) == "0 seconds"
  assert time_units_from_seconds(1) == "1 second"
  assert time_units_from_seconds(89) == "1 minute"
  assert time_units_from_seconds(90) == "2 minutes"
  assert time_units_from_seconds(59*60) == "59 minutes"
  assert time_units_from_seconds(60*60) == "1 hour"
  assert time_units_from_seconds(23*3600) == "23 hours"
  assert time_units_from_seconds(24*3600) == "1 day"
  assert time_units_from_seconds(6*86400) == "6 days"
  assert time_units_from_seconds(7*86400) == "1 week"
  assert time_units_from_seconds(30*86400) == "4 weeks"
  assert time_units_from_seconds(32*86400) == "1 month"
  assert time_units_from_seconds(350*86400) == "11 months"
  assert time_units_from_seconds(365*86400) == "1 year"
  assert time_units_from_seconds(730*86400) == "2 years"
