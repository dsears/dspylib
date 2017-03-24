from dspylib import pluralize

def test_pluralize():
  assert pluralize(2, "monkey") == "2 monkeys"
  assert pluralize(1, "monkey") == "1 monkey"
  assert pluralize(0, "monkey") == "0 monkeys"
  assert pluralize(-1, "monkey") == "-1 monkeys"
  assert pluralize(-2, "monkey") == "-2 monkeys"
