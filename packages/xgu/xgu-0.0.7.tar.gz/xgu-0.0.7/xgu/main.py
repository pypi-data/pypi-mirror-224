from xgu.prepare_q import f as prepare_q
from xgu.populate_changes_dict import f as populate_changes_dict
from xgu.git_pull import f as git_pull
from xgu.git_status import f as git_status
from xgu.add_and_commit_changes import f as add_and_commit_changes

# main
def f(ask):
  git_pull()
  status_result = git_status()
  q = prepare_q(status_result)
  changes = populate_changes_dict(q)
  add_and_commit_changes(changes, ask)
  if any([_ in changes for _ in [' M', '??', ' D']]): f(ask)
