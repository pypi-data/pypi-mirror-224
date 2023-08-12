from hak.pxyz import f as pxyz
from copy import deepcopy

def f(x):
  _x = deepcopy(x)
  return {'list': _x, 'popped': _x.pop()}

def t():
  x = ['a', 'b', 'c']
  y = {'list': ['a', 'b'], 'popped': 'c'}
  z = f(x)
  return pxyz(x, y, z)
