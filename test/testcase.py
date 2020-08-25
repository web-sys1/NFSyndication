from pytest import fixture
import subprocess

@fixture()
def entry_point():
  try:
   subprocess.run(["nfsyndication-src"])
  except Exception:
   print('ERROR')
