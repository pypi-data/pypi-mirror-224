from subprocess import run as sprun

# prepare_q
def f(status_result):
  q_0=[_ for _ in status_result.stdout.decode().split("\n") if _]
  
  ls_files_result = sprun(
    args=['git', 'ls-files', '--others', '--exclude-standard'],
    capture_output=True,
    cwd='.'
  )
  q_1=[f'?? {_}' for _ in ls_files_result.stdout.decode().split("\n") if _]
  
  return [
    _ for
    _ in (q_0 + q_1)
    if not _.endswith('/')
  ]
