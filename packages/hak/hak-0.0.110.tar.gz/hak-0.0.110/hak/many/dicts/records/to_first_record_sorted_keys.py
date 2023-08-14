from hak.one.dict.get_sorted_keys import f as get_sorted_keys
from hak.pxyz import f as pxyz

# records_to_first_record_sorted_keys
f = lambda records: get_sorted_keys(records[0])

def t():
  x = [{'c': 0, 'b': 1, 'a': 2}, {}]
  y = list('abc')
  z = f(x)
  return pxyz(x, y, z)
