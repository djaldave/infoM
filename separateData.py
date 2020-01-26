import csv

with open('in.csv') as fin, open('out.csv', 'w+') as out:
    o = csv.writer(out)
    for line in fin:
        o.writerow(line.split())
