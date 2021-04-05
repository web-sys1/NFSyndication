import os
import sys
import argparse
import logging
import time
import logging.handlers
from . import __version__, __base_path__
from . import config
from . import parser

from functools import wraps

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()

verbose = False

args = parser.parse_args()


def exec_wrapper(func):
    """This decorator prints the execution time for the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution took {}s".format(round(end - start, 2)))
        return result

    return wrapper

args = parser.parse_args()
if args.version:
      print('NFSyndication version: ' + __version__)
      sys.exit(0)

@exec_wrapper
def run():
  try:
   logger.setLevel(logging.DEBUG)
   if os.path.isfile(__base_path__) and os.access(__base_path__, os.R_OK):
    os.mkdir('output')
  except FileExistsError:
    # directory already exists
   pass
  return config.init()

logger = logging.StreamHandler()

if args.verbose == 1:
        logging.getLogger().setLevel(logging.INFO)
elif args.verbose == 2:
        logging.getLogger().setLevel(logging.DEBUG)


if __name__ == '__main__':
    run()

