from collections import defaultdict
import csv

# miasta = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
miasta = defaultdict(lambda: defaultdict(int))

with open('uklad-komunikacyjny.csv', encoding='utf8') as file:
    reader = csv.DictReader(file, fieldnames=None, delimiter=';')
    for row in reader:
        miasta[row['miasto']][row['year']] = 0

for miasto in miasta:
    for rok in miasta[miasto]:
        print(f"{miasto} {rok}")
