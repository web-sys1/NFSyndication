'''
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
'''
from printy import printy
my_dict = {'id': 71, 'zip_codes': ['050001', '050005', '050011', '050015', '050024'], 'code': '05001', 'country': {'code': 'co'}, 'city_translations': [{'language_code': 'es', 'name': 'Medellín'}], 'flag': None}
printy(my_dict)
