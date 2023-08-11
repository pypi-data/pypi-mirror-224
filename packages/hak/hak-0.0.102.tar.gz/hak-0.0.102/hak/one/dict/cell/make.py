from hak.one.dict.cell.to_str import f as to_str
from hak.one.string.colour.decolour import f as decol
from hak.pf import f as pf
from hak.pxyz import f as pxyz
from hak.one.dict.rate.make import f as make_rate
from datetime import date
from hak.one.dict.rate.is_a import f as is_rate
from hak.one.dict.rate.to_float import f as to_float
from hak.one.dict.rate.to_num import f as to_num
from hak.one.dict.get_or_default import f as get_or_default
from hak.one.dict.rate.to_str import f as rate_to_str

# make_cell
# src.cell.make
def f(x):
  _width = x['width']
  _format = get_or_default(x, 'format', None)
  _val_str = (
    (
      _format(x['value'])
      if x['value'] else
      ''
    )
    if _format else (
      (
        rate_to_str(x['value'])
        if to_num(x['value']) else
        ''
      )
      if is_rate(x['value']) else
      to_str(x['value'])
    )
  )
  
  _ = _width - len(decol(f'{_val_str:>{_width}}'))
  left_pad = ' '*_
  return left_pad + f'{_val_str:>{_width}}'

def t_0():
  # cell_dict
  x = {'value': 'a', 'width': 1}
  y = 'a'
  z = f(x)
  return pxyz(x, y, z)

def t_rate():
  x = {
    'value': make_rate(numerator=1, denominator=1, unit={'m': 1}),
    'width': 4
  }
  y = '1.00'
  z = f(x)
  return pxyz(x, y, z)

def t_date():
  x = {'value': date(2022, 4, 5), 'width': len('2022-04-05')}
  y = '2022-04-05'
  z = f(x)
  return pxyz(x, y, z)

def t_description():
  x = {'value': 'Purchased USD with AUD'}
  x['width'] = len('Purchased USD with AUD')
  y = 'Purchased USD with AUD'
  z = f(x)
  return pxyz(x, y, z)

def t_USD_rate():
  x = {'value': make_rate(5472, 1, {'USD': 1}), 'width': 8}
  y = ' 5472.00'
  z = f(x)
  return pxyz(x, y, z)

def t_asset_nabtrade_cash_AUD():
  x = {'value': make_rate(-7350.89, 1, {'AUD': 1}), 'width': 8}
  y = '-7350.89'
  z = f(x)
  return pxyz(x, y, z)

def t_rate_0():
  x = {
    'value': make_rate(numerator=0, denominator=1, unit={'m': 1}),
    'width': 4
  }
  y = ' '*x['width']
  z = f(x)
  return pxyz(x, [y], [z])

def t():
  if not t_0(): return pf('t_0 failed')
  if not t_rate(): return pf('t_rate failed')
  if not t_date(): return pf('!t_date')
  if not t_description(): return pf('!t_description')
  if not t_USD_rate(): return pf('!t_USD_rate')
  if not t_asset_nabtrade_cash_AUD(): return pf('!t_asset_nabtrade_cash_AUD')
  if not t_rate_0(): return pf('!t_rate_0')
  return True
