import datetime
from dspylib import pluralize
from dspylib import DAYS_PER_MONTH

def timedelta_to_seconds(delta):
  """
  Take a timedelta object and return the total number of seconds.
  """
  return delta.seconds + (delta.days * 86400)

def time_units_from_seconds(seconds):
  """
  Take an integer number of seconds and return the largest time unit with a non-zero value.
  """
  if seconds < 60:
    return pluralize(seconds, "second")
  
  minutes = seconds / 60.0
  minutes_rounded = int(round(minutes))
  if minutes_rounded < 60:
    return pluralize(minutes_rounded, "minute")
  
  hours = minutes / 60.0
  hours_rounded = int(round(hours))
  if hours_rounded < 24:
    return pluralize(hours_rounded, "hour")

  days = hours / 24.0
  days_rounded = int(round(days))
  if days_rounded < 7:
    return pluralize(days_rounded, "day")
  
  weeks = days / 7.0
  weeks_rounded = int(round(weeks))
  if days < DAYS_PER_MONTH:
    return pluralize(weeks_rounded, "week")
  
  months = days / DAYS_PER_MONTH
  months_rounded = int(round(months))
  if months_rounded < 12:
    return pluralize(months_rounded, "month")
  
  years = months / 12.0
  years_rounded = int(round(years))
  return pluralize(years_rounded, "year")

def relative_time(to_datetime,
    from_datetime=datetime.datetime.now(),
    past_format="%s ago",
    future_format="in %s"):
  delta = to_datetime - from_datetime
  delta = timedelta_to_seconds(delta)
  if delta > 0:
    return future_format % time_units_from_seconds(delta)
  else:
    return past_format % time_units_from_seconds(delta * -1)
