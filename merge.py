import csv
import os

os.system("cls")

datasett_1 = []
datasett_2 = []

with open("dataset_1.csv", "r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        datasett_1.append(i)

header_1 = datasett_1[0]
planetsdata_1 = datasett_1[1:]

with open("dataset_2.csv", "r") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        datasett_2.append(i)

header_2 = datasett_2[0]
planetsdata_2 = datasett_2[1:]

final_header = header_1 + header_2
final_planetsdata = []

for index, row in enumerate(planetsdata_1):
    final_planetsdata.append(planetsdata_1[index]+planetsdata_2[index])

with open("final_data.csv", "a+", newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(final_header)
    csvwriter.writerows(final_planetsdata)  