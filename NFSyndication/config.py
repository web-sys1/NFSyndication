#!/usr/bin/python 
import sys
from colored import  fg, bg, attr

def init():
  try:
   from NFSyndication import nfs_main, styles
  except Exception as e:
   print(f"%s%sFatal: {e} %s"%(fg(1),bg(0),attr('reset')))
   sys.exit(1)
  
  #return os.popen(f'{dir_path}/nfs_main.py').read()
  #run = lambda filename : exec(open(filename).read(), globals())
  #return run(f'{dir_path}/main.py')
  #fload = lambda filename : exec(open(filename).read(), globals())
  #return fload(f'{dir_path}/styles.py')
