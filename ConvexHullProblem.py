import itertools
import random


def find_subsets(s, m):
    return set(itertools.combinations(s, m))


def make_list():
    list_minor = [random.randint(-1000, 1001), random.randint(-1000, 1001)]
    return list_minor


number = int(input())

list_major = []

for num in range(number):
    list_major.append(make_list())


print(list_major)

subsets = find_subsets(set(list_major), number)
print(subsets)
