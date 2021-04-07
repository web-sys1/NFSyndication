#!/usr/bin/python 
import sys
import logging
import colorful as cf
from jinja2 import Template, Environment, FileSystemLoader
import feedparser
import os
import shutil
from .extras import fetch_content

cfail = cf.bold_red

def init():
  logging.info("Fetching...")
  try:
   from . import nfs_main, styles
  except Exception as e:
    exception = cfail(
                  "Error while parsing: {exceptname}: {errmessage}".format(exceptname=str(e.__class__.__name__), errmessage=e)
                   )
    print(exception)
    sys.exit(1)
  except KeyboardInterrupt:
    print('Session terminated. Operation aborted by the user.')

class GetFeedDataPerConfiguration(object):
    def __init__(self, eachUrl, tempPath, emdF, fPath, outputPath, templFileLocation, outPath, pageTitle):
        self.feeds = []
        #self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.env = Environment(loader=FileSystemLoader(tempPath))
        self.fetch_feeds(eachUrl)
        self.empty_public(emdF)
        self.copy_static(fPath, outputPath)
        self.render_page(templFileLocation, outPath, pageTitle)

    def fetch_feeds(self, URLs):
        """ Request and parse all of the feeds, saving them in self.feeds """
        for url in URLs:
            print(f"Fetching {url}")
            self.feeds.append(feedparser.parse(url))
            fetch_content(url)

    def empty_public(self, sf):
        """ Ensure the public directory is empty before generating. """
        try:
            shutil.rmtree(sf) 
            os.mkdir(sf)
        except:
            print(cfail(f"Error cleaning up old files."))

    def copy_static(self, fPath, outputPath):
        """ Copy static assets to the public directory """
        try:
            shutil.copytree('{}'.format(fPath), '{}'.format(outputPath))
        except:
            print(cfail(f"Error copying static files."))

    def render_page(self, templFileLocation, outputPath, pageTitle):
        print("Rendering page to static file.")
        template = self.env.get_template(templFileLocation)
        with open('{}'.format(outputPath), 'w+', encoding='utf8') as file:
            html = template.render(
                title = '{}'.format(pageTitle),
                feeds = self.feeds
            )
            file.write(html)
