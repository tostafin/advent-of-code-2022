from typing import List, Set, Tuple

with open("input", "r") as moves_input:
    moves: List[Tuple[str, int]] = [
        (m, int(n)) for m, n in map(lambda s: s.split(), filter(None, moves_input.read().split("\n")))
    ]
    tail_pos: Tuple[int, int] = (0, 0)
    head_pos: List[int] = [0, 0]
    tail_positions: Set[Tuple[int, int]] = {tail_pos}
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

            new_tail: Tuple[int, int] = tail_pos
            if head_pos[0] != tail_pos[0] and head_pos[1] != tail_pos[1]:
                if head_pos[0] == tail_pos[0] + 1 and head_pos[1] == tail_pos[1] + 2 or \
                        head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1] + 1:
                    new_tail = (tail_pos[0] + 1, tail_pos[1] + 1)
                elif head_pos[0] == tail_pos[0] + 2 and head_pos[1] == tail_pos[1] - 1 or \
                        head_pos[0] == tail_pos[0] + 1 and head_pos[1] == tail_pos[1] - 2:
                    new_tail = (tail_pos[0] + 1, tail_pos[1] - 1)
                elif head_pos[0] == tail_pos[0] - 1 and head_pos[1] == tail_pos[1] - 2 or \
                        head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1] - 1:
                    new_tail = (tail_pos[0] - 1, tail_pos[1] - 1)
                elif head_pos[0] == tail_pos[0] - 2 and head_pos[1] == tail_pos[1] + 1 or \
                        head_pos[0] == tail_pos[0] - 1 and head_pos[1] == tail_pos[1] + 2:
                    new_tail = (tail_pos[0] - 1, tail_pos[1] + 1)

            else:
                if head_pos[1] == tail_pos[1] + 2:
                    new_tail = (tail_pos[0], tail_pos[1] + 1)
                elif head_pos[0] == tail_pos[0] + 2:
                    new_tail = (tail_pos[0] + 1, tail_pos[1])
                elif head_pos[1] == tail_pos[1] - 2:
                    new_tail = (tail_pos[0], tail_pos[1] - 1)
                elif head_pos[0] == tail_pos[0] - 2:
                    new_tail = (tail_pos[0] - 1, tail_pos[1])

            tail_positions.add(new_tail)
            tail_pos = new_tail

    print(len(tail_positions))
