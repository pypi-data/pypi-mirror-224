from hak.pf import f as pf
from hak.pxyz import f as pxyz
from hak.many.values.detect_type import f as detect_type
from hak.one.tuple.is_a import f as is_tuple
from hak.one.string.is_a import f as is_str

def f(heading, values, path=None):
  if path and not is_tuple(path):
    if not is_str(path): raise TypeError(f'path should be tuple, path: {path}')
    path = tuple([path])
  return {
    'heading': heading,
    'values': values,
    'type': detect_type(values),
    'path': path or tuple()
  }

def t_0():
  x = {'heading': 'abc', 'values': [0, 1, 2]}
  y = {'heading': 'abc', 'values': [0, 1, 2], 'type': 'int', 'path': ()}
  z = f(**x)
  return pxyz(x, y, z)

def t_single_element_path_as_str():
  x = {'heading': 'abc', 'values': [0, 1, 2], 'path': 'root'}
  y = {
    'heading': 'abc',
    'values': [0, 1, 2],
    'type': 'int',
    'path': ('root',)
  }
  z = f(**x)
  return pxyz(x, y, z)

def t_path():
  x = {'heading': 'abc', 'values': [0, 1, 2], 'path': ('root', 'branch')}
  y = {
    'heading': 'abc',
    'values': [0, 1, 2],
    'type': 'int',
    'path': ('root', 'branch')
  }
  z = f(**x)
  return pxyz(x, y, z)

def t():
  if not t_0(): return pf('!t_0')
  if not t_path(): return pf('!t_path')
  return True
