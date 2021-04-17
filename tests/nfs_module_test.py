import os, glob
import pytest
import subprocess
import pytest
from NFSyndication import init as NFS_init
# test@
# Change the action associated with your option to action='store'

def test_conf():
    #We use these conditions to check the statement
    subscriptions = [
     'http://feedpress.me/512pixels',
     'http://www.leancrew.com/all-this/feed/',
     'http://ihnatko.com/feed/',
     'http://blog.ashleynh.me/feed']
  
    with open(f'feeds.txt', 'w', encoding='utf8') as f:
     f.write(",".join(subscriptions).replace(',', '\n'))
    return NFS_init()
    
def test_entrypoint():
    #Then initialize code
    return test_conf()
    
def pytest_configure():
    pytest.something = test_entrypoint()
