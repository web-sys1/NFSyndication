import os
import sys
import argparse
import logging
from . import __version__, __base_path__
from . import config

def run():
  parser = argparse.ArgumentParser()
  parser.add_argument(
        "--version",
        action="store_true",
        help="print the version", default=1
    )
  args = parser.parse_known_args()
  if args[0].version:
      print('NFSyndication version: ' + __version__)
      sys.exit(0)
  try:
   logger = logging.getLogger()
   logger.setLevel(logging.DEBUG)
   if os.path.isfile(__base_path__) and os.access(__base_path__, os.R_OK):
    os.mkdir('output')
  except FileExistsError:
    # directory already exists
   pass
  return config.init()
  
if __name__ == '__main__':
    run()
