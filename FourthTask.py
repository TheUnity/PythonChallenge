import geoplotlib
from geoplotlib.utils import DataAccessObject


class Coord:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return 'Координаты: {0}, {1}'.format(self.latitude, self.longitude)

    def __add__(self, other):
        return Coord(self.latitude + other.latitude, self.longitude + other.longitude)

    def map(self):
        geoplotlib.dot(DataAccessObject({'lat': [self.latitude], 'lon': [self.longitude]}))
        geoplotlib.show()


new_coord = Coord(float(input('Введите широту первой точки ')), float(input('Введите долготу первой точки ')))
new_coord2 = Coord(float(input('Введите широту второй точки ')), float(input('Введите долготу второй точки ')))

print(new_coord)
print(new_coord2)
print('Суммированные {0}'.format(new_coord + new_coord2))

Coord.map(new_coord)
