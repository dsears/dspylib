DAYS_PER_YEAR = 365.25
DAYS_PER_MONTH = DAYS_PER_YEAR / 12.0

def pluralize(number, unit):
  if number != 1:
    unit = "%ss" % unit
  return "%d %s" % (number, unit)
