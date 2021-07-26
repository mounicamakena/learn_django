from app.models import Netflix
import xlrd


def bulkcreate_netflix(filepath):

    tmp_array = []

    book = xlrd.open_workbook(filepath)
    sheet = book.sheet_by_index(0)

    for i in range(1, sheet.nrows):
        row = sheet.row(i)
        netflix = Netflix(
            show_id=row[0].value,
            show_type=row[1].value,
            title=row[2].value,
            director=row[3].value,
            cast=row[4].value,
            country=row[5].value,
            date_added=row[6].value,
            release_year=row[7].value,
            rating=row[8].value,
            duration=row[9].value,
            listed_in=row[10].value,
            description=row[11].value)

        tmp_array.append(netflix)
    Netflix.objects.bulk_create(tmp_array)
