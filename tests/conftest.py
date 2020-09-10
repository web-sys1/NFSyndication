import os, glob
import NFSyndication
import subprocess
from NFSyndication import main as NFS_init

def test_conf():
    """ We use these conditions to check the statement"""
    subscriptions = [
     'http://feedpress.me/512pixels',
     'http://www.leancrew.com/all-this/feed/',
     'http://ihnatko.com/feed/',
     'http://blog.ashleynh.me/feed']
  
    with open(f'feeds.txt', 'w', encoding='utf8') as f:
     f.write(",".join(subscriptions).replace(',', '\n'))
    NFS_init.entry_point()
    
def test_entrypoint():
    """Then initialize code."""
    return NFS_init()
