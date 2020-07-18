from app.model.tweet import Tweets
from app import response, app
from app.lib import twitter
from flask import request, url_for, Markup
from app import db
import pickle


def index() :
    try :
        tweets = Tweets.query.all()
        data = transform(tweets)
        return response.ok(data, "")
    except Exception as e :
        print(e)


def transform(tweets) :
    array = []
    for i in tweets:
        array.append({
            'tweet': i.tweet,
            'url': i.url,
            'result': i.result
        })
    return array


def show(id) :
    try :
        tweets = Tweets.query.filter_by(id=id).first()
        if not tweets:
            return response.badRequest([], 'Empty....')
        
        data = singleTransform(tweets)
        return response.ok(data, "")
    except Exception as e :
        print(e)


def singleTransform(tweets) :
    data = {
        'tweet': tweets.tweet,
        'url': tweets.url,
        'result': tweets.result
    }
    return data


def store(tweet, url, result):
    try :

        check = Tweets.query.filter_by(url=url).first()
        if not check:
            tweets = Tweets(tweet=tweet, url=url, result=result)
            db.session.add(tweets)
            db.session.commit()
            return True
        else :
            return False

    except Exception as e :
        print(e)


def detect():
    try :
        url = request.json['url']
        s = url.split("/")
        id = s[-1]
        tweet = twitter.get_tweet(id)
        # print(tweet)
        pickle_in = open('model_fakenews.pickle', 'rb')
        pac = pickle.load(pickle_in)
        tfidf = open('tfidf.pickle', 'rb')
        tfidf_vectorizer = pickle.load(tfidf)
        input_data = [tweet.text.rstrip()]
        # transforming input
        tfidf_test = tfidf_vectorizer.transform(input_data)
        # predicting the input
        y_pred = pac.predict(tfidf_test)

        result = y_pred[0]
        
        tes = store(tweet.text, url, result)
        if tes :
            print('sudah disimpan')
        
        data = customTransform(tweet, result, id)

        return response.ok(data, 'Success')

    except Exception as e :
        print(e)
        return response.badRequest([], 'Failed')

def customTransform(tweet, result, id):
    data = {
        'tweet' : tweet.text,
        'result' : result,
        'name' : tweet.user.name,
        'screen_name' : tweet.user.screen_name,
        'profile_pic' : tweet.user.profile_image_url_https,
        'id' : id
    }
    return data