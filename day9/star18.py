from typing import List, Set, Tuple

with open("input", "r") as moves_input:
    moves: List[Tuple[str, int]] = [
        (m, int(n)) for m, n in map(lambda s: s.split(), filter(None, moves_input.read().split("\n")))
    ]
    head_pos: List[int] = [0, 0]
    other_knots: List[Tuple[int, int]] = [(0, 0) for _ in range(9)]
    tail_positions: Set[Tuple[int, int]] = {other_knots[8]}
    for m, n in moves:
        for _ in range(n):
            match m:
                case "U":
                    head_pos[1] += 1
                case "R":
                    head_pos[0] += 1
                case "D":
                    head_pos[1] -= 1
                case "L":
                    head_pos[0] -= 1

            next_knot: Tuple[int, int] = tuple(head_pos)
            for i, knot in enumerate(other_knots):
                curr_knot: Tuple[int, int] = knot
                if next_knot[0] != knot[0] and next_knot[1] != knot[1]:
                    if next_knot[0] == knot[0] + 1 and next_knot[1] == knot[1] + 2 or \
                            next_knot[0] == knot[0] + 2 and next_knot[1] == knot[1] + 1:
                        curr_knot = (knot[0] + 1, knot[1] + 1)
                    elif next_knot[0] == knot[0] + 2 and next_knot[1] == knot[1] - 1 or \
                            next_knot[0] == knot[0] + 1 and next_knot[1] == knot[1] - 2:
                        curr_knot = (knot[0] + 1, knot[1] - 1)
                    elif next_knot[0] == knot[0] - 1 and next_knot[1] == knot[1] - 2 or \
                            next_knot[0] == knot[0] - 2 and next_knot[1] == knot[1] - 1:
                        curr_knot = (knot[0] - 1, knot[1] - 1)
                    elif next_knot[0] == knot[0] - 2 and next_knot[1] == knot[1] + 1 or \
                            next_knot[0] == knot[0] - 1 and next_knot[1] == knot[1] + 2:
                        curr_knot = (knot[0] - 1, knot[1] + 1)

                    elif next_knot[0] == knot[0] + 2 and next_knot[1] == knot[1] + 2:
                        curr_knot = (knot[0] + 1, knot[1] + 1)
                    elif next_knot[0] == knot[0] + 2 and next_knot[1] == knot[1] - 2:
                        curr_knot = (knot[0] + 1, knot[1] - 1)
                    elif next_knot[0] == knot[0] - 2 and next_knot[1] == knot[1] - 2:
                        curr_knot = (knot[0] - 1, knot[1] - 1)
                    elif next_knot[0] == knot[0] - 2 and next_knot[1] == knot[1] + 2:
                        curr_knot = (knot[0] - 1, knot[1] + 1)

                else:
                    if next_knot[1] == knot[1] + 2:
                        curr_knot = (knot[0], knot[1] + 1)
                    elif next_knot[0] == knot[0] + 2:
                        curr_knot = (knot[0] + 1, knot[1])
                    elif next_knot[1] == knot[1] - 2:
                        curr_knot = (knot[0], knot[1] - 1)
                    elif next_knot[0] == knot[0] - 2:
                        curr_knot = (knot[0] - 1, knot[1])

                other_knots[i] = curr_knot
                next_knot = curr_knot
                if i == 8:
                    tail_positions.add(curr_knot)

    print(len(tail_positions))
