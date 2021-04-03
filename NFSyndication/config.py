#!/usr/bin/python 
import sys
import colorful as cf

cfail = cf.bold_red

def init():
  try:
   from . import nfs_main, styles
  except Exception as e:
   print(cfail(f"Error while parsing: {e}"))
   sys.exit(1)
