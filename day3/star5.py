with open("input", "r") as rucksacks_items:
    print(sum([
        ord(next(iter(set.intersection(s1, s2)))) - ord("a") + 1 if
        next(iter(set.intersection(s1, s2))).islower() else
        ord(next(iter(set.intersection(s1, s2)))) - ord("A") + 27 for s1, s2 in
        map(lambda i: [set(i[:len(i) // 2]), set(i[len(i) // 2:])], filter(None, rucksacks_items.read().split("\n")))
    ]))
