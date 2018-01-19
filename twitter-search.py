import tweepy
import config
import random
import sys
from datetime import datetime

#def login():
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
print('Logged in twitter |･ω･｀)')



def search_key(key):
    print('searching... (҂⌣̀_⌣́)')
    tweet_list = api.search(key, count=10, tweet_mode='extended')
    print('writing result to file... ( •̀ᄇ• ́)ﻭ✧')
    with open('search_result.txt', 'a') as file:
        file.write('\n\n\n\n{:*^50}\n'.format('NEW SEARCH o(≧∇≦o)'))
        file.write('search key is"{}" at {}\n\n'.format(key, str(datetime.now())))
        for tweet in tweet_list:
        #TO DO: print those into a file
            file.write('{} says: {}\n\tlink: https://twitter.com/{}/status/{}\n\n'.format(tweet._json['user']['name'] ,tweet.full_text,tweet._json['user']['screen_name'] ,tweet._json['id']))
    print('file closed ~ヾ(＾∇＾)')
if __name__ == "__main__":
    search_key(sys.argv[1])

