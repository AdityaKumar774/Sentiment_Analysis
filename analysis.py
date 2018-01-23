import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'svHeEjNftbNHRJzIjVFP4BirJ'
consumer_secret = 'AMnNo0GN9kdgalE9HsTqu5z02tUnDStsMsUmaEmC1F0lkEWeO5'
access_token = '268657390-wOtkT47MSf7tQ6ODYSikkDrkEojsZPJ1PPy5gCRv'
access_secret = 'oq2Lug0yg2Q4T6tbCPNzT94jdG82PG2wjf4sCNENivoCI'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('data.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Manchester United'])
 