# encoding = utf-8
"""
This file contains the logic for filtering/munging posts.  It's kept in
a separate file from the main feed parsing logic so the commit history
for main.py doesn't get polluted with nitpicks and tweaks.
"""
import collections
from datetime import datetime
#from time import mktime
#def format_datetime(struct_time):
    #return datetime.fromtimestamp(mktime(struct_time))
import colorful as cf
import logging
import json
from colorama import init, Fore, Back, Style
#from . import parser

#args = parser.parse_args()

init(convert=True)

# List of keywords to filter
FILTER_WORDS = ['*']

cfail = cf.bold_red
cfhighlight = cf.bold_blue

def fetch_content(url):
   import feedparser
   try:
    feed = feedparser.parse(url)
    print("\nFeed title:", feed.feed.title or None)
    print("Link:", feed.feed.link or None)

    if hasattr(feed.feed, 'subtitle'):
        print("Subtitle:", feed.feed.subtitle)

    #print("Updated:", feed.feed.updated)
    #print("Updated (parsed):", format_datetime(feed.feed.updated_parsed))
    #print("Feed ID:", rss_url.feed.id)
    print('-----------------------------------------------')
    print("\nEntries:")
   
    for entry in feed.entries:
       print(cfhighlight(f" * Title: {entry.title}"))
       print(cfhighlight(f"   Link: {entry.link}"))
       print(cfhighlight(f"   Published: {entry.published}"))
       print(cfhighlight(f"   Updated: {entry.updated}"))
       print(cfhighlight(f"   Summary length: {len(entry.summary) or None} \n"))
       #print("   Content items count:", len(entry.content))
   except Exception as e:
    print(Fore.RED + 'Error occured while parsing some URLs: {feedurl} '.format(feedurl=url) + 'HTTP {return_code}'.format(return_code=feed.status))
    print('{}: {}'.format(str(e.__class__.__name__),str(e)))
    print(Style.RESET_ALL)
   else:
    print(cf.bold_green("   Respone: {}".format(feed.status)))
   finally:
    try:
     feedHeaders = json.dumps(feed.headers, indent=4, sort_keys=True)
     logging.info('Output headers JSON: \n' + feedHeaders)
    except Exception as e:
      print(e.__class__.__name__)

ExtendedPost = collections.namedtuple('Post', [
    'time',
    'blog',
    'title',
    'author',
    'link',
    'body',
    'permalink'
])


def remove_final_link(html_text):
    return html_text.rsplit('<a', maxsplit=1)[0]


def extract_last_link(html_text):
    return html_text.rsplit('"', maxsplit=2)[-2]


def normalise_post(post):
    """
    This function takes a post and a blog, and applies some
    transformations to normalise the text.  This is mostly based on
    special cases and lots of if statements.
    It returns an ExtendedPost tuple, which includes fields not found
    in the regular Post.
    It may also return None, which means this post should be hidden.
    """
    blog = post.blog

    if any(word.lower() in post.body.lower() for word in FILTER_WORDS):
        return None
    
    """ 
       --------------------- NO LONGER NEEDED ---------------------
       
    if (blog == 'Marco.org'):
        if ('coffee' in post.body):
            return None
        if post.title.startswith(u'→'):
            title = post.title[2:]
            body = remove_final_link(post.body)
            permalink = extract_last_link(post.body)
            return ExtendedPost(post.time, post.blog, title, post.author,
                                post.link, body, permalink)

    elif (blog == 'Daring Fireball') and u'★' in post.body:
        body = remove_final_link(post.body)
        permalink = extract_last_link(post.body)
        return ExtendedPost(post.time, post.blog, post.title, post.author,
                            post.link, body, permalink)

    elif (blog == 'Erica Sadun') and (post.author == 'erica'):
        return ExtendedPost(post.time, post.blog, post.title,
                            None, post.link, post.body, None)
                            
       --------------------- NO LONGER NEEDED ---------------------
    """

    return ExtendedPost(*post, permalink=None)
