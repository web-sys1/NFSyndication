from pytest import fixture
import subprocess

@fixture()
def entry_point():
    subprocess.run(["nfsyndication-src"])
