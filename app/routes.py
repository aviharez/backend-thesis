from app import app
from app.controller import TweetController
from flask import request

@app.route('/tweets', methods=['POST', 'GET'])
def tweet():
    if request.method == 'GET':
        return TweetController.index()
    else :
        return TweetController.detect()

@app.route('/tweets/<id>')
def tweetDetail(id):
    return TweetController.show(id)
