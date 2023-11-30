import csv
from collections import defaultdict, namedtuple


pola: list[str] = [
    'dlugosc_tras_autobusowych_w_granicach_miasta',
    'dlugosc_tras_trolejbusowych_w_granicach_miasta',
    'dlugosc_linii_autobusowych_w_granicach_miasta',
    'dlugosc_linii_trolejbusowych_w_granicach_miasta',
    'wozokm_autobusowe_w_granicach_miasta',
    'wozokm_trolejbusowe_w_granicach_miasta'
]
Dane = namedtuple(typename='Dane', field_names=pola)
miasta = defaultdict(lambda: defaultdict(Dane))

with open('uklad-komunikacyjny.csv', encoding='utf8') as file:
    reader = csv.DictReader(file, fieldnames=None, delimiter=';')
    for row in reader:
        miasta[row['miasto']][row['year']] = Dane(
            dlugosc_linii_autobusowych_w_granicach_miasta=row['dlugosc_linii_autobusowych_w_granicach_miasta'],
            dlugosc_linii_trolejbusowych_w_granicach_miasta=row['dlugosc_linii_trolejbusowych_w_granicach_miasta'],
            dlugosc_tras_autobusowych_w_granicach_miasta=row['dlugosc_tras_autobusowych_w_granicach_miasta'],
            dlugosc_tras_trolejbusowych_w_granicach_miasta=row['dlugosc_tras_trolejbusowych_w_granicach_miasta'],
            wozokm_autobusowe_w_granicach_miasta=row['wozokm_autobusowe_w_granicach_miasta'],
            wozokm_trolejbusowe_w_granicach_miasta=row['wozokm_trolejbusowe_w_granicach_miasta']
        )

for miasto in miasta:
    for rok in miasta[miasto]:
        print(
            f"{miasto} "
            f"{rok}: "
            f"{miasta[miasto][rok].dlugosc_linii_autobusowych_w_granicach_miasta} "
            f"{miasta[miasto][rok].dlugosc_linii_trolejbusowych_w_granicach_miasta} "
            f"{miasta[miasto][rok].dlugosc_tras_autobusowych_w_granicach_miasta} "
            f"{miasta[miasto][rok].dlugosc_tras_trolejbusowych_w_granicach_miasta} "
            f"{miasta[miasto][rok].wozokm_autobusowe_w_granicach_miasta} "
            f"{miasta[miasto][rok].wozokm_trolejbusowe_w_granicach_miasta}"
        )
