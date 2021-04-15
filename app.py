"""Cloud Foundry test"""
from flask import Flask, render_template
import os
from NFSyndication.config import GetFeedDataPerConfiguration

app = Flask(__name__, static_folder="output/static")

port = int(8900)

URLS = (
  'http://www.leancrew.com/all-this/feed/',
  'http://ihnatko.com/feed/',
  'http://blog.ashleynh.me/feed',
  'http://www.betalogue.com/feed/',
)

@app.route('/')
def dev_production():
   fg= GetFeedDataPerConfiguration(URLS, 'NFSyndicationa/templates', 'output', 'templates/static', 'output/static', '_layout.html', 'output/index.html', 'PSF')
   dsf=open('output/index.html', 'r', encoding='utf-8')
   return render_template('NFSyndication/templates/_layout.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=port)