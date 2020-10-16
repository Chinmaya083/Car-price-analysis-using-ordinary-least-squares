import csv
import statistics
import random

# Reads the dataset, removes outliers and takes a simple random sample of 750 rows from this cleaned dataset and stores it into a new file called 'cleanDataset.csv'


# Utility Functions #


def readFile():
    i = open("car_price_sample.csv", 'r')
    csvreader = csv.reader(i)

    fields = next(csvreader)[1:]
    rows = []
    for row in csvreader:
        rows.append(row[1:])
    return fields, rows


def writeFile(fields, rows):
    o = open('cleanDataset.csv', 'w', newline='')
    csvwriter = csv.writer(o)
    csvwriter.writerow(fields)
    [csvwriter.writerow(row) for row in rows]


def median(a, l, r):
    n = r - l + 1
    n = (n + 1) // 2 - 1
    return n + l


def quartiles(a, n):
    a.sort()
    mid_index = median(a, 0, n)
    Q1 = a[median(a, 0, mid_index)]
    Q3 = a[median(a, mid_index + 1, n)]
    return Q1, Q3


def removeOutliers(dataset, columnIndex):
    attribute = [float(row[columnIndex]) for row in dataset]
    q1, q3 = quartiles(attribute, len(attribute))
    iqr = q3 - q1
    lowerLimit = q1 - 1.5*iqr
    upperLimit = q3 + 1.5*iqr

    return [row for row in dataset if lowerLimit <= float(row[columnIndex]) <= upperLimit]

# End of Utility Functions #

# Main Function #


def cleanData():
    fields, rows = readFile()
    isCatagorical = [0, 1, 0, 1, 0, 0, 1, 1, 1, 1]

    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if (rows[i][j] in [' ', '0', '0.0'] or (j == 0 and float(rows[i][j]) < 100)):
                if (isCatagorical[j]):
                    rows[i][j] = rows[i-1][j]
                else:
                    rows[i][j] = str(round(statistics.mean([float(i[j]) for i in rows])))

    print('Number of records before any removing outliers = %d' % len(rows))
    rows = removeOutliers(rows, 4)
    print('Number of records after removing outliers in horse power (powerPS) = %d' % len(rows))
    rows = removeOutliers(rows, 0)
    print('Number of records after removing outliers in price = %d' % len(rows))
    [print(x[4]) for x in rows]
    #Takes a simple random sample of 750 rows
    rows = random.sample(rows, 750)
    print('Number of records after SRS = %d' % len(rows))
    # writeFile(fields, rows)

# End of Main Function #

cleanData()
