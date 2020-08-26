# encoding = utf-8
"""
This file contains the logic for filtering/munging posts.  It's kept in
a separate file from the main feed parsing logic so the commit history
for main.py doesn't get polluted with nitpicks and tweaks.
"""

import collections
from datetime import datetime
#from time import mktime
from colored import  fg, bg, attr

#def format_datetime(struct_time):
    #return datetime.fromtimestamp(mktime(struct_time))

# List of keywords to filter
FILTER_WORDS = ['*']

col = fg(29)
res = attr('reset')

def fetch_content(url):
    import feedparser
    feed = feedparser.parse(url)
    print(" Feed title:", feed.feed.title or None)
    print(" Link:", feed.feed.link or None)

    if hasattr(feed.feed, 'subtitle'):
        print("Subtitle:", feed.feed.subtitle)

    #print("Updated:", feed.feed.updated)
    #print("Updated (parsed):", format_datetime(feed.feed.updated_parsed))
    #print("Feed ID:", rss_url.feed.id)
    print('-----------------------------------------\n')
    print("\nEntries:")

    for entry in feed.entries:
       print(col + " * Title:", entry.title)
       print(col + "   Link: ", entry.link)
       #print("   Published: ", entry.published)
       print(col + "   Updated: ", entry.updated + res)
       print(col+ "   Summary length: ", len(entry.summary) or None)
       print(res)
       #print("   Content items count:", len(entry.content))


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
    
    """if (blog == 'Marco.org'):
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
    """

    return ExtendedPost(*post, permalink=None)
