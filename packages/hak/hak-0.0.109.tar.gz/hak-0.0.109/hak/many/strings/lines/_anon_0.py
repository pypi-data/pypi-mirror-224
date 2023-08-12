from hak.pxyz import f as pxyz
from hak.one.string.find_last_char import f as find_last_char

def _f(l, top_width):
  j = find_last_char(l, '|')+1
  d = l[0]*(top_width - len(l))
  return l[:j]+d+l[j:]

f = lambda x: [_f(l, len(x[0])) if len(l) < len(x[0]) else l for l in x]

def t():
  x = [
    '------------|---------',
    '    numbers | letters ',
    '-----|------|-----',
    ' abc |  ghi | jkl ',
    '-----|------|-----',
    '   0 |    0 |   a ',
    '   1 |   10 |   b ',
    '   2 |  200 |   c ',
    '   3 | 3000 |   d ',
    '-----|------|-----'
  ]
  y = [
    '------------|---------',
    '    numbers | letters ',
    '-----|------|---------',
    ' abc |  ghi |     jkl ',
    '-----|------|---------',
    '   0 |    0 |       a ',
    '   1 |   10 |       b ',
    '   2 |  200 |       c ',
    '   3 | 3000 |       d ',
    '-----|------|---------'
  ]
  z = f(x)
  return pxyz(x, str(y), str(z))
