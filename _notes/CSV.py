import csv

with open("file.csv") as file:
    data = csv.reader(file)
    for row in data:
        print(row)