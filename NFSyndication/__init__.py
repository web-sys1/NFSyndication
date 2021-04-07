#!/usr/bin/python 
# -*- coding: utf-8 -*-
import argparse
import sys
import logging

__version_info__ = (0,2,23)
__version__ = '.'.join(map(str,__version_info__))

__base_path__ = 'feeds.txt'

parser = argparse.ArgumentParser(description='News Feed Syndication {} - A package that read and fetch RSS feeds from the publications.'.format(__version__))
parser.add_argument("-V",
        "--version",
        action="store_true",
        help="Print the package version and quit"
        )
parser.add_argument('-v', '--verbose', help='Show verbose messages', action='count', default=0)
                        
parser.add_argument('-f','--filename',help="specify which file type to use (for example: nfsyndication-src --filename=./path/to/sample.file.txt)", nargs='+')