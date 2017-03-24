import datetime
from dspylib.date import relative_time

def test_relative_time():
  now = datetime.datetime.now()
  yesterday = now - datetime.timedelta(days=1)
  tomorrow = now + datetime.timedelta(days=1)
  
  assert relative_time(yesterday) == "1 day ago"
  assert relative_time(yesterday, from_datetime=yesterday) == "0 seconds ago"
  assert relative_time(tomorrow) == "in 1 day"
  assert relative_time(tomorrow, future_format="%s from now") == "1 day from now"
