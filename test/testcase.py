import subprocess

def entry_point():
  try:
   subprocess.run(["nfsyndication-src"])
  except Exception:
   print('ERROR')
