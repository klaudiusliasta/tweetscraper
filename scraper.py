import csv
import tweepy
import re

def search(consumer_key, consumer_secret, access_token, access_token_secret, keyword):
    
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    #initialize Tweepy API
    api = tweepy.API(auth)

    #open the spreadsheet we will write to
    with open('%s.csv' % (keyword), 'w') as file:

        w = csv.writer(file)

        #write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])

        #for each tweet matching our keyword, write relevant info to the spreadsheet, this time we only collect 100 update tweets
        for tweet in tweepy.Cursor(api.search, q=keyword+' -filter:retweets',
                                    tweet_mode='extended').items(1000):
            w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])

consumer_key = input('Consumer Key ')
consumer_secret = input('Consumer Secret ')
access_token = input('Access Token ')
access_token_secret = input('Access Token Secret ')
    
keyword = input('The Keyword to Search for ')

if __name__ == '__main__':
    search(consumer_key, consumer_secret, access_token, access_token_secret, keyword)
