from hak.pf import f as pf
from hak.fake.printer import f as FP

f = lambda x, y, z, p=print: y == z or pf([f'x: {x}', f'y: {y}', f'z: {z}'], p)

def t_true():
  _fake_printer = FP()
  x = {'x': 1, 'y': 1, 'z': 1}
  y = True
  z = f(**x, p=_fake_printer)
  return y == z and _fake_printer.history == []

def t_false():
  _fake_printer = FP()
  x = {'x': 1, 'y': 1, 'z': 2}
  y = False
  z = f(**x, p=_fake_printer)
  return y == z and _fake_printer.history == ['x: 1\ny: 1\nz: 2']

def t():
  if not t_true(): return pf('!t_true')
  if not t_false(): return pf('!t_false')
  return True
