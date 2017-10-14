import itertools
import random


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return self + -point


def find_subsets(s, m):
    return set(itertools.combinations(s, m))


def make_point_object():
    return Point(random.randint(-1000, 1001), random.randint(-1000, 1001))


number = int(input())
list_major = []

for num in range(number):
    list_major.append(make_point_object())

# print(list_major)
print(list_major[0].split(', '))
