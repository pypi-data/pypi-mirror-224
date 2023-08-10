from src.prepare_q import f as prepare_q
from src.populate_changes_dict import f as populate_changes_dict
from src.git_pull import f as git_pull
from src.git_status import f as git_status
from src.add_and_commit_changes import f as add_and_commit_changes

# main
def f():
  git_pull()
  status_result = git_status()
  q = prepare_q(status_result)
  changes = populate_changes_dict(q)
  add_and_commit_changes(changes)

  if any([_ in changes for _ in [' M', '??', ' D']]): f()
