#!/usr/bin/python 
import sys
import logging
import colorful as cf

cfail = cf.bold_red

def init():
  logging.info("Fetching...")
  try:
   from . import nfs_main, styles
  except Exception as e:
   print(cfail(f"Error while parsing: {e}"))
   sys.exit(1)
  except KeyboardInterrupt:
    print('Session terminated. Operation aborted by the user.')
