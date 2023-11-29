import csv
from collections import defaultdict, namedtuple
import os
from csv import DictReader
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director() -> dict[list]:
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    directors: dict[list] = defaultdict(list)

    with open(MOVIE_DATA) as f:
        reader: DictReader[str] = csv.DictReader(f)

        for row in reader:
            director: str = row['director_name']
            title: str = row['movie_title'].replace('\xa0', '')
            try:
                year: int = int(row['title_year'])
            except ValueError:
                continue
            score: float = float(row['imdb_score'])

            if year >= MIN_YEAR:
                directors[director].append(Movie(title, year, score))

        return directors


def calc_mean_score(movies: list[namedtuple]) -> float:
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    summary: float = 0.0
    cnt: int = 0
    for movie in movies:
        summary += movie[2]
        cnt += 1
    return round(summary / cnt, 1)


def get_average_scores(directors) -> list[tuple]:
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    scores: list = []
    for director, movies in directors.items():
        if len(movies) < MIN_MOVIES:
            continue
        scores.append((director, calc_mean_score(movies)))

    return sorted(scores, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    directors = get_movies_by_director()
    for director, score in get_average_scores(directors):
        print(f"{director}: {score}")
