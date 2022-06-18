import subprocess
from datetime import datetime, timedelta

def getCSV(days):
    import random, time
    for i in range(days):
        date = str(datetime.date(datetime.now()) - timedelta(days = i)).replace("-", "")
        url = "https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date={}&selectType=ALL".format(date)
        time.sleep(random.uniform(1, 5))
        content = subprocess.check_output(["curl", url]).decode("cp950")
        with open(date + ".csv", "w", encoding="cp950") as file:
            file.write(content)


def mergeCSV(days):
    import csv
    data = []
    for i in range(days):
        date = str(datetime.date(datetime.now()) - timedelta(days = i)).replace("-", "")
        filename = date + ".csv"
        lineCount = 0
        with open(filename, encoding="cp950") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                lineCount = lineCount + 1
                if len(row) != 8 or lineCount <= 2:
                    continue
                row[7] = date
                data.append(row)

    with open("result.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

    for i in range(days):
        date = str(datetime.date(datetime.now()) - timedelta(days = i)).replace("-", "")
        filename = date + ".csv"
        subprocess.Popen(["rm", filename])

if __name__ == "__main__":
    dates = 1000
    getCSV(dates)
    mergeCSV(dates)
