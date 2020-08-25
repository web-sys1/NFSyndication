
from NFSyndication.config import init as NFS_init
import os

subscriptions = [
  'http://feedpress.me/512pixels',
  'http://www.leancrew.com/all-this/feed/',
  'http://ihnatko.com/feed/',
  'http://blog.ashleynh.me/feed'
  'http://schmeiser.typepad.com/penny_wiseacre/rss.xml',
  'http://feeds.feedburner.com/PracticallyEfficient',
  'http://robjwells.com/rss',
  'http://www.red-sweater.com/blog/feed/',
  'http://feedpress.me/sixcolors',
]
  
with open(f'/feeds.txt', 'w', encoding='utf8') as f:
    f.write(",".join(subscriptions).replace(',', '\n'))

NFS_init()
