from subprocess import run as sprun
from hak.one.string.colour.bright.cyan import f as cy

# git_status
def f():
  print(cy("Executing 'git status -s'"))
  return sprun(args=['git', 'status', '-s'], capture_output=True, cwd='.')
