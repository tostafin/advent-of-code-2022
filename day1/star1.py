with open("input", "r") as calories_input:
    print(max(
        map(sum, (map(lambda c: int(c), calories_per_raindeer) for calories_per_raindeer in
                  map(lambda s: s.strip("\n").split("\n"), calories_input.read().split("\n\n"))))
    ))
