from hak.one.string.colour.bright.cyan import f as cy
from subprocess import run as sprun

# git_pull
def f():
  print(cy("Executing 'git pull'"))
  pull_result = sprun(args=['git', 'pull'], capture_output=True, cwd='.')
  print(cy('pull_result.stdout.decode():')+f' {pull_result.stdout.decode()}')
