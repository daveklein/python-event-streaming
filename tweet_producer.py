import tweepy
import time
import json
from config import kafka_config, credentials, topics
from confluent_kafka import Producer


def init():
    auth = tweepy.OAuthHandler(credentials['consumer.key'], credentials['consumer.secret'])
    auth.set_access_token(credentials['access.token'], credentials['access.token_secret'])

    return Producer(kafka_config), tweepy.API(auth)


def load_tweets():
    producer, api = init()

    print('Begin fetching tweets')
    while True:
        for tweet in tweepy.Cursor(api.search_tweets,
                                   q="{conference_tag}",
                                   count=10,
                                   result_type="recent",
                                   include_entities=True,
                                   lang="en").items():
            jtweet = tweet_to_json(tweet)
            print(jtweet)
            producer.produce(topics['input'], key=tweet.user.name, value=jtweet)
            producer.flush()
        time.sleep(60)


def tweet_to_json(tweet):
    return json.dumps({
        'id':tweet.id,
        'user': tweet.user.name,
        'text': tweet.text
    })

if __name__ == "__main__":
    load_tweets()
    