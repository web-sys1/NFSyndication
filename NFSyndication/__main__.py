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
        help="print the version"
    )
  args = parser.parse_known_args()
  if args.version:
      print('NFSyndication version ' + __version__)
      sys.exit()
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
