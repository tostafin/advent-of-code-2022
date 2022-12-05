from typing import Union, Final, List

with open("input", "r") as crates_input:
    crates: str
    moves: Union[str, List[int]]
    crates, moves = crates_input.read().split("\n\n")

    num_of_stacks: Final[int] = int(crates[-1])
    stacks: List[List[str]] = [[] for _ in range(num_of_stacks)]
    crates_rows: List[str] = crates.split("\n")
    for crate in reversed(crates_rows):
        for i in range(1, len(crate), 4):
            if crate[i].isupper():
                stacks[i // 4].append(crate[i])

    moves = [int(c) for m in filter(None, moves.split("\n")) for c in m.split() if c.isdigit()]

    for i in range(0, len(moves), 3):
        for _ in range(moves[i]):
            stacks[moves[i + 2] - 1].append(stacks[moves[i + 1] - 1].pop())

    print(*map(lambda c: c[-1], stacks), sep="")
