import sys
import csv

i = list(map(str.strip, sys.stdin))
with open('plants.csv', 'w', newline='', encoding='utf-8') as csvf:
    writer = csv.writer(csvf, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['nomen', "definitio", "pluma", "Russian nomen", "familia", "Russian nomen familia"])

    for row in i:
        s = row.split('\t')
        writer.writerow(s)
