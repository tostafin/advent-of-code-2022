from typing import Dict
from string import ascii_lowercase, ascii_uppercase

with open("input", "r") as rucksacks_items:
    letters_priorities: Dict[str, int] = {c: ord(c) - ord("a") + 1 for c in ascii_lowercase}
    letters_priorities.update({c: ord(c) - ord("A") + 27 for c in ascii_uppercase})
    print(sum([
        letters_priorities[(next(iter(set.intersection(s1, s2, s3))))] for s1, s2, s3 in
        zip(*(iter(map(lambda i: set(i), filter(None, rucksacks_items.read().split("\n")))),) * 3)
    ]))
