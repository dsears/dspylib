from datetime import timedelta
from dspylib.date import timedelta_to_seconds

def test_timedelta_to_seconds():
  assert timedelta_to_seconds(timedelta(days=1, seconds=600)) == 87000
  assert timedelta_to_seconds(timedelta(days=0, seconds=600)) == 600
