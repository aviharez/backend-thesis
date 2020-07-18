import tweepy

CONSUMER_KEY= "tVSOrJIfWcnpRCtZtTWnudwvy"
CONSUMER_SECRET= "dMPSbOt6UWXna7HNwLa4Qy14UaIlojjPzYgHtHo0wJTqXW53NN"
ACCESS_TOKEN_KEY= "2361187837-d02EzmDIeRbMZ7fQ8n5e7Gl0aC7gmygZMNGvTSc"
ACCESS_TOKEN_SECRET= "lMjLxPaq8a6V4oANFOKbWJqqU0TYrzeDRXs1ENnHnxLMW"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def get_tweet(id) :
    tweet = api.get_status(id)
    return tweet