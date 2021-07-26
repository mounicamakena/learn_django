from app.models import Netflix
import csv

file_name = "netflix_titles.csv"
temp_array = []

with open(file_name, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # csv_reader is array of dicts
    for line in csv_reader:
        netflix = Netflix(
            show_id=line['show_id'],
            show_type=line['type'],
            title=line['title'],
            director=line['director'],
            cast=line['cast'],
            country=line['country'],
            date_added=line['date_added'],
            release_year=line['release_year'],
            rating=line['rating'],
            duration=line['duration'],
            listed_in=line['listed_in'],
            description=line['description']
        )

        temp_array.append(netflix)


Netflix.objects.bulk_create(temp_array)
