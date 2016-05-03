import os
import json

from twython import Twython
from twython import TwythonStreamer

with open(os.environ.get('HOME') + '/twitter_token', 'r') as f:
        api_token = f.read().replace('\n', '')

APP_KEY = 'qwc7VO7gg9dDNLvq1lnbqzHNS'

twitter = Twython(APP_KEY, access_token=api_token)

twiits = twitter.search(q='#tornientaisto', count=100)

good_twiits = [a for a in twiits['statuses'] if not 'retweeted_status' in a]

jsonp = 'callback(' + json.dumps(good_twiits) + ');'

with open('tweets.jsonp', 'w') as f:
    api_token = f.write(jsonp)

