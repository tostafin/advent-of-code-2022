with open("input", "r") as elves_tasks:
    print(len([[int(e1t1), int(e1t2), int(e2t1), int(e2t2)] for e1t1, e1t2, e2t1, e2t2 in
               map(lambda s: s.split("-"), filter(None, elves_tasks.read().replace(",", "-").split("\n")))
               if max(int(e1t1), int(e2t1)) <= min(int(e1t2), int(e2t2))
               ]))
