from hak.pxyz import f as pxyz

f = lambda x_str, x_char: [i for (i, c) in enumerate(x_str) if c == x_char]

def t():
  x = {
    'x_str': 'a,b,c,defg',
    'x_char': ','
  }
  y = [1, 3, 5]
  z = f(**x)
  return pxyz(x, y, z)
