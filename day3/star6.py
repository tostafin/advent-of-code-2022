from typing import Dict
from string import ascii_lowercase, ascii_uppercase

with open("input", "r") as rucksacks_items:
    print(sum([
        ord(next(iter(set.intersection(s1, s2, s3)))) - ord("a") + 1 if
        next(iter(set.intersection(s1, s2, s3))).islower() else
        ord(next(iter(set.intersection(s1, s2, s3)))) - ord("A") + 27 for s1, s2, s3 in
        zip(*(iter(map(lambda i: set(i), filter(None, rucksacks_items.read().split("\n")))),) * 3)
    ]))
