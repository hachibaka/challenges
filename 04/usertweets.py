from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple("Tweet",'id_str created_at text')

class UserTweets(object):
    """TODOs:
    - create a tweepy api interface
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory
    - implement len() an getitem() magic (dunder) methods"""
    def __init__(self, handle,max_id=None):
        self.handle = handle
        self.max_id = max_id


    @property
    def tweetapi(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        return tweepy.API(auth)

    @property
    def _usertweets(self):
        #user = self.tweetapi.get_user(self.user_id)
        tweets= self.tweetapi.user_timeline(self.handle,max_id=self.max_id,count=NUM_TWEETS)
        return [Tweet(s.id_str,s.created_at,s.text.replace('\n','')) for s in tweets]

    @property
    def output_file(self):
        ouputfilename = '{}.{}'.format(os.path.join(DEST_DIR, self.handle), EXT)
        with open(ouputfilename,'w') as f:
            writer = csv.writer(f)
            writer.writerow(Tweet._fields)
            writer.writerows(self._usertweets)
        return ouputfilename

    def __len__(self):
        return len(self._usertweets)

    def __getitem__(self,pos):
        return self._usertweets[pos]






if __name__ == "__main__":

    for handle in ('Harjeet','pybites', 'techmoneykids', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        print(len(user))
        print()
