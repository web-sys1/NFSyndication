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
log_format = "%(asctime)s %(levelname)s -- %(message)s"
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
# logger.addHandler(handler)

# always write everything to the rotating log files
if not os.path.exists('logs'): os.mkdir('logs')
log_file_handler = logging.handlers.TimedRotatingFileHandler('logs/args.log', when='M', interval=2)
log_file_handler.setFormatter( logging.Formatter('%(asctime)s [%(levelname)s](%(name)s:%(funcName)s:%(lineno)d): %(message)s') )
log_file_handler.setLevel(logging.DEBUG)
logger.addHandler(log_file_handler)

# also log to the console at a level determined by the --verbose flag
console_handler = logging.StreamHandler() # sys.stderr
console_handler.setLevel(logging.CRITICAL) # set later by set_log_level_from_verbose() in interactive sessions
console_handler.setFormatter( logging.Formatter('[%(levelname)s](%(name)s): %(message)s') )
logger.addHandler(console_handler)

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

  parser = argparse.ArgumentParser()
  parser.add_argument(
        "--version",
        action="store_true",
        help="print the version"
    )
  args = parser.parse_args()
  if args.version:
      print('NFSyndication version: ' + __version__)
      sys.exit(0)

  try:
   logger.setLevel(logging.DEBUG)
   if os.path.isfile(__base_path__) and os.access(__base_path__, os.R_OK):
    os.mkdir('output')
  except FileExistsError:
    # directory already exists
   pass
  return config.init()


    if not args.verbose:
        console_handler.setLevel('ERROR')
    elif args.verbose == 1:
        console_handler.setLevel('WARNING')
    elif args.verbose == 2:
        console_handler.setLevel('INFO')
    elif args.verbose >= 3:
        console_handler.setLevel('DEBUG')
    else:
        logger.critical("UNEXPLAINED NEGATIVE COUNT!")
   
if __name__ == '__main__':
    run()
