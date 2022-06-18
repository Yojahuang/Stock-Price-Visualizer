import time

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

    with open("result.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in datas:
            writer.writerow(row)

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

if __name__ == "__main__" :
    stockNumbers = ["2382", "00631L", "2885", "3006", "8454", "8478", "1319", "3008",
    "2606", "1303", "2006", "5269", "4958", "1216", "2892", "2542", "4755", "1102", "1590",
    "2347", "6409", "2345", "6781", "5871", "1524", "6669", "2883", "2357", "2884", "2313",
    "3533", "2379", "2305", "2409", "2637", "2481", "2327", "1101", "6235", "2881", "1301",
    "2891", "00878", "8261", "0056", "2882", "3036", "2002", "2308", "2412", "00637L", "3711",
    "3443", "2049", "00632R", "2368", "3481", "2886", "0050", "2634", "6770", "4919", "3532",
    "2615", "1605", "3189", "6415",  "3034", "8046", "3661", "2610", "1560", "1795", "2317",
    "3035", "2303", "2618", "2609", "2454", "3037", "2603", "2330"
    ]

    getCSV(stockNumbers)
    mergeCSV(stockNumbers)
