from xgu.f_added import f as f_added
from xgu.f_modified import f as f_modified
from xgu.f_deleted import f as f_deleted

term_to_function = {' M': f_modified, '??': f_added, ' D': f_deleted}

# process_changes
def f(d, ask):
  for k in [' M', '??', ' D']:
    if k in d:
      term_to_function[k](sorted(d[k])[0], ask)
