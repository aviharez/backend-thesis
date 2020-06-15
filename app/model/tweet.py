from app import db
from datetime import datetime

class Tweets(db.Model) :
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    tweet = db.Column(db.String(300), nullable=False)
    url = db.Column(db.String(300), index=True, unique=True,nullable=False)
    result = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) :
        return '<Tweet {}>'.format(self.tweet)