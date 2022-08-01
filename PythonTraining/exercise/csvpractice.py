from fileinput import filename
import os
import csv

os.chdir(os.path.dirname(__file__)) 
"""
rows = []
header = []

with open('newfile.csv', 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    rows = [row for row in csvreader]


print(header)
print(rows)

"""

rows = [['Anu', 9, 40000], ['Vinu', 8, 30000], ['Manu', 6, 34000]]
header = ['Names', 'Experience', 'Salary']

filename = 'newfile.csv'
with open(filename, "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)


