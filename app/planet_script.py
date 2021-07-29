from app.models import Planet
import csv

file_name = "planet.csv"
temp_array = []

with open(file_name, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # csv_reader is array of dicts
    for line in csv_reader:
        planet = Planet(
            image_name=line['image_name'],
            tags=line['tags']

        )

        temp_array.append(planet)


Planet.objects.bulk_create(temp_array)
