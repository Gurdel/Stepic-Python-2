import csv

with open('Crimes.csv') as sr:
    r = csv.reader(sr)
    crimes = []
    for row in r:
        if '2015' in row[2]:
            crimes.append(row[5])
    print(max(set(crimes), key=crimes.count))

import pandas

df = pandas.read_csv('Crimes.csv')
df['Primary Type'].describe()