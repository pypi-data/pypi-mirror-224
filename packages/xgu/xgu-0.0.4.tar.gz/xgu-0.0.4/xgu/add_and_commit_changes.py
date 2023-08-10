from xgu.f_a import f as f_A
from xgu.f_m import f as f_M
from xgu.f_d import f as f_D

term_to_function = {' M': f_M, '??': f_A, ' D': f_D}

# process_changes
def f(d):
  for k in [' M', '??', ' D']:
    if k in d:
      term_to_function[k](sorted(d[k])[0])
