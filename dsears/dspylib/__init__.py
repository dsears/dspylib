def pluralize(number, unit):
  if number != 1:
    unit = "%ss" % unit
  return "%d %s" % (number, unit)
