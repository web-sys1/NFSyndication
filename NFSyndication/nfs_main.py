#!/usr/bin/env python
# coding=utf-8
import os
import collections
from datetime import datetime, timedelta
import time
from configparser import ConfigParser

import feedparser
import jinja2
import json
import logging
import pytz
import typing
import sys
import logging
from . import parser

from jinja2.exceptions import UndefinedError
from . import parser
from .extras import normalise_post, fetch_content

logging.basicConfig(format='%(message)s', datefmt='%I:%M', level=logging.DEBUG)

config = ConfigParser()
args = parser.parse_args()

argsFilename = args.filename

# Get a list of feed URLs
try:
 with open('feeds.txt') as f:
    SUBSCRIPTIONS = list(f)
    print('Loading feeds.txt')
except FileNotFoundError:   # If you don't have 'feeds.txt' in specified path, you can specify one (nfsyndication-src --filename=sample.txt)
 try:
  for documentList in argsFilename:
   with open(documentList) as f:
    SUBSCRIPTIONS = list(f)
   print('Loading file: ' + documentList)
 except TypeError:
   raise Exception('NFSyndication [ERROR]: feeds.txt not found. See `nfsyndication-src --help` for more.')

# Date and time setup. I want only posts from "today" and "yesterday",
# where the day lasts until 2 AM.
TIMEZONE = config.get(section='default', option='timezone', fallback='GMT')

# Get the current time in the home timezone, then step back to include
# the last two days.
home_tz = pytz.timezone(TIMEZONE)
dt = datetime.now(home_tz)
if dt.hour < 2:
    dt -= timedelta(hours=72)
else:
    dt -= timedelta(hours=48)
start = dt.replace(hour=0, minute=0, second=0, microsecond=0)

# Convert this time back into UTC.
utc = pytz.utc
START = start.astimezone(utc)


try:
   Post = typing.NamedTuple('Post', [('time', str), ('blog', str), ('title',str), ('author',str), ('link', str), ('body',str)])

except Exception as exc:
   print(f'Exception Error: {exc}')

def process_entry(entry, blog):
    """
    Coerces an entry from feedparser into a Post tuple.
    Returns None if the entry should be excluded.
    """
    # Get the date of the post.  If it was published more than two days
    # ago, drop the entry. Now, the feed entries is being analyzed and processed before reading in SUBSCRIPTIONS.
    try:
        when = entry['updated_parsed']
    except KeyError:
        when = entry['published_parsed']
    when = utc.localize(datetime.fromtimestamp(time.mktime(when)))

    if when < START:
        return
        
    title = entry['title']
    
    try:
        author = entry['author']
    except KeyError:
        author = ', '.join(a['name'] for a in entry.get('authors', []))
    link = entry['link']
    try:
        body = entry['content'][0]['value']
    except KeyError:
        body = entry['summary']
    return normalise_post(Post(when, blog, title, author, link, body))    

posts = []

try:
 for url in SUBSCRIPTIONS:
    try:
        feed = feedparser.parse(url)
        blog = feed['feed']['title']
    except KeyError:
        if args.verbose and feed.bozo:
            logging.error("Feed data summary on URL {}".format(url))
            logging.error("Exception [{bozo_exception}]: {bozo_message}".format(bozo_exception=str(feed.bozo_exception.__class__.__name__), bozo_message=str(feed.bozo_exception)))
            if (hasattr(feed.bozo_exception, 'getLineNumber') and hasattr(feed.bozo_exception, 'getMessage')):
                line = feed.bozo_exception.getLineNumber()
                logging.error('Line %d: %s', line, feed.bozo_exception.getMessage())
                
        raise Exception(f"[{feed.bozo_exception}] (code {feed.status}) \n{(f'Could not fetch URL(s): {url}')}")
        sys.exit(-1)
        continue
    for entry in feed['entries']:
        post = process_entry(entry, blog)
        if post:
            posts.append(post)
    try:
     fetch_content(url)
    except:
     raise SystemExit
except NameError:
  pass

# Get the template, and drop in the posts
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/templates/template.html', encoding='utf8') as f:
    print("\nChecking template...")
    template = jinja2.Template(f.read())
    
# When done, it converts to HTML.
with open(f'output/index.html', 'w', encoding='utf8') as f:
    f.write(template.render(posts=posts, time=datetime.now()))
    print('Successful.')