from NFSyndication import main as NFS_init
import os

subscriptions = [
  'http://feedpress.me/512pixels',
  'http://www.leancrew.com/all-this/feed/',
  'http://ihnatko.com/feed/',
  'http://blog.ashleynh.me/feed']
  
with open(f'feeds.txt', 'w', encoding='utf8') as f:
    f.write(",".join(subscriptions).replace(',', '\n'))

def entry_point():
  return NFS_init()

print(entry_point())
