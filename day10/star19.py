from typing import List, Tuple


def check_signal_strength(signal_strength: int, cycle: int, next_cycle_lookup: int) -> Tuple[int, int, int]:
    cycle += 1
    if cycle == next_cycle_lookup:
        signal_strength += cycle * x_value
        next_cycle_lookup += 40

    return signal_strength, cycle, next_cycle_lookup


with open("input", "r") as operations_input:
    operations: List[Tuple[str, int] | str] = [
        (op[0], int(op[1])) if len(op) == 2 else op[0]
        for op in map(lambda s: s.split(), filter(None, operations_input.read().split("\n")))
    ]
    signal_strength: int = 0
    cycle: int = 0
    next_cycle_lookup: int = 20
    x_value: int = 1
    for op in operations:
        if op[0] == "addx":
            signal_strength, cycle, next_cycle_lookup = check_signal_strength(signal_strength, cycle, next_cycle_lookup)
            signal_strength, cycle, next_cycle_lookup = check_signal_strength(signal_strength, cycle, next_cycle_lookup)
            x_value += op[1]

        else:
            signal_strength, cycle, next_cycle_lookup = check_signal_strength(signal_strength, cycle, next_cycle_lookup)

        if cycle >= 220:
            break

    print(signal_strength)
