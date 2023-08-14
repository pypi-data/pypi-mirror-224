from hak.pf import f as pf
from hak.pxyz import f as pxyz

# cell_val_widths_to_aggregate_width
f = lambda x: sum(x)+(len(x)-1)*len(' | ')

def t_6():
  x = [6] # | 123456 |
  y = 6   # | 123456 |
  z = f(x)
  return pxyz(x, y, z)

def t_7_8():
  x = [7, 8] # | 1234567 | 12345678 |
  y = 18     # | 123456789012345678 |
  z = f(x)
  return pxyz(x, y, z)

def t_8_9_10():
  x = [8, 9, 10] # | 12345678 | 123456789 | 1234567890 |
  y = 33         # | 123456789012345678901234567890123 |
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_6():      return pf('!t_6')
  if not t_7_8():    return pf('!t_7_8')
  if not t_8_9_10(): return pf('!t_8_9_10')
  return True
