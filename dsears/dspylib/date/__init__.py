import datetime
from dsears.dspylib import pluralize

def timedelta_to_seconds(delta):
  return delta.seconds + (delta.days * 86400)

def relative_time(then,
    now=datetime.datetime.now(),
    past_format="%s ago",
    future_format="in %s"):
  delta = now - then
  delta = timedelta_to_seconds(delta)
