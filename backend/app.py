from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.databaseURL
db = SQLAlchemy(app)

class stockPrice(db.Model):
    price = db.Column(db.Numeric, nullable = False)
    stockNumber = db.Column(db.String(10), primary_key = True)
    date = db.Column(db.Date, primary_key = True)

    def __init__(self, price, stockNumber, date):
        self.price = price
        self.stockNumber = stockNumber
        self.date = date

class stockName(db.Model):
    chineseName = db.Column(db.Text, nullable = False)
    stockNumber = db.Column(db.String(10), primary_key = True)

    def __init__(self, chineseName, stockNumber):
        self.chineseName = chineseName
        self.stockNumber = stockNumber

@app.route('/')
def hello_world():
    return "Hello, World!"
