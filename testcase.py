import os
import NFSyndication
import subprocess
from NFSyndication import main as NFS_init

def entry_point():
    """ We use these conditions to check the statement"""
    subscriptions = [
     'http://feedpress.me/512pixels',
     'http://www.leancrew.com/all-this/feed/',
     'http://ihnatko.com/feed/',
     'http://blog.ashleynh.me/feed']
  
    with open(f'feeds.txt', 'w', encoding='utf8') as f:
     f.write(",".join(subscriptions).replace(',', '\n'))
    return NFS_init()


"""Then initialize code."""
entry_point()
