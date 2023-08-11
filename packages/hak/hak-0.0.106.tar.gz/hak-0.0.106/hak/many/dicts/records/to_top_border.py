# ignore_overlength_lines
from .k_branch.to_branch_col_width import f as get_top_head_width
from .fn.to_fn_applied_to_sorted_keys_of_records import f as records_and_fn_to_fn_applied_to_sorted_keys_of_records
from hak.many.strings.to_table_row import f as cell_strings_to_table_row_string
from hak.pxyz import f as pxyz
from hak.pf import f as pf
from datetime import date

# records_to_top_border
def f(x):
  _a = [
    '-'*_ for _ in records_and_fn_to_fn_applied_to_sorted_keys_of_records(
      x,
      get_top_head_width
    )
  ]
  return cell_strings_to_table_row_string(_a, '-')

from hak.one.dict.rate.make import f as make_rate

def t_nest():
  x = [
    {
      'prices': {
        'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(1, 2, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': make_rate(1, 1, {'apple': 1}),
        'bananazzz': make_rate(2, 1, {'banana': 1}),
        'pearzzzzzz': make_rate(3, 1, {'pear': 1})
      },
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    }, 
    {
      'prices': {
        'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(1, 1, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': make_rate(4, 1, {'apple': 1}),
        'bananazzz': make_rate(5, 1, {'banana': 1}),
        'pearzzzzzz': make_rate(6, 1, {'pear': 1})
      },
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    }
  ]
  y = '|--------------------|-----------------------------------|--------|'
  z = f(x)
  return pxyz(x, y, z)

def t_date():
  x = [
    {
      'date': date(2023, 7, 27),
      'prices': {'apples': make_rate(1, 4, {'$': 1, 'apple': -1})},
    },
    {
      'date': date(2023, 7, 28),
      'prices': {'apples': make_rate(3, 4, {'$': 1, 'apple': -1})},
    }
  ]
  y = "|------------|---------|"
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_nest(): return pf('t_nest failed')
  # if not t_date(): return pf('t_date failed')
  return True
