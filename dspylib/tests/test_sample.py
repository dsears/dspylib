import datetime
from dspylib.date import relative_time

def test_relative_time():
  then = datetime.datetime.now()
  then -= datetime.timedelta(days=1)
  assert relative_time(then) == "1 day ago"
