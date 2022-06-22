from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import config

app = Flask(__name__)
CORS(app)
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

@app.route('/<stockNumber>', methods = ['GET'])
def getClosingPrice(stockNumber):
    prices = stockPrice.query.filter_by(stockNumber = stockNumber).all()
    result = []
    for item in prices:
        result.append({
            "date" : item.date.strftime("%Y/%m/%d"),
            "price" : item.price
        })
    if len(result) == 0:
        return jsonify({"message" : "stock number not found"}), 404
    return jsonify(result), 200

@app.route('/<stockNumber>', methods = ['POST'])
def updateClosingPrice(stockNumber):
    import time, datetime

    def getCSV(stockNumbers):
        import subprocess,random

        for stockNumber in stockNumbers:
            for year in [2021, 2022]:
                for month in range(1, 13, 1):
                    if year == 2022 and month > 6:
                        break
                    yearStr = str(year)
                    monthStr = str(month)
                    if month < 10:
                        monthStr = "0" + monthStr
                    date = yearStr + monthStr + "01"

                    url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=csv&date={}&stockNo={}".format(date, str(stockNumber))
                    time.sleep(random.uniform(1, 5))

                    content = subprocess.check_output(["curl", url]).decode("cp950")
                    with open(str(stockNumber) + ":" + yearStr + ":" + monthStr + ".csv", "w", encoding="cp950") as file:
                        file.write(content)

    getCSV([stockNumber])

    def mergeCSV(stockNumbers):
        import subprocess, csv

        datas = []
        for stockNumber in stockNumbers:
            for year in [2021, 2022]:
                for month in range(1, 13, 1):
                    if year == 2022 and month > 6:
                        break
                    yearStr = str(year)
                    monthStr = str(month)
                    if month < 10:
                        monthStr = "0" + monthStr

                    filename = str(stockNumber) + ":" + yearStr + ":" + monthStr + ".csv"
                    lineCount = 0
                    with open(filename, encoding="cp950") as file:
                        reader = csv.reader(file)
                        for row in reader:
                            lineCount = lineCount + 1
                            if len(row) != 3 or (row[0] < '0' or row[0] > '9'):
                                continue
                            row[2] = stockNumber
                            datas.append(row)

        for row in datas:
            year = int(row[0].split("/")[0]) + 1911
            month = int(row[0].split("/")[1])
            day = int(row[0].split("/")[2])
            date = datetime.date(year, month, day)

            price = float(0)
            if row[1] == "--":
                price = 0
            else:
                price = float(row[1].replace(",", ""))

            current = stockPrice.query.filter_by(price = price, stockNumber = str(row[2]), date = date).all()

            if len(current):
                continue

            item = stockPrice(price = price, stockNumber = str(row[2]), date = date)

            db.session.add(item)
            db.session.commit()

        for stockNumber in stockNumbers:
            for year in [2021, 2022]:
                for month in range(1, 13, 1):
                    if year == 2022 and month > 6:
                        break
                    yearStr = str(year)
                    monthStr = str(month)
                    if month < 10:
                        monthStr = "0" + monthStr

                    filename = str(stockNumber) + ":" + yearStr + ":" + monthStr + ".csv"
                    subprocess.Popen(["rm", filename])

    mergeCSV([stockNumber])
    return jsonify("Data added!"), 200
