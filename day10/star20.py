from typing import List, Tuple
from pprint import pprint


def put_pixel(image: List[str], cycle: int, x_value: int) -> int:
    cycle += 1
    if x_value <= cycle <= x_value + 2:
        image.append("#")
    else:
        image.append(".")

    cycle %= 40

    return cycle


with open("input", "r") as operations_input:
    operations: List[Tuple[str, int] | str] = [
        (op[0], int(op[1])) if len(op) == 2 else op[0]
        for op in map(lambda s: s.split(), filter(None, operations_input.read().split("\n")))
    ]
    cycle: int = 0
    x_value: int = 1
    image: List[str] | str = []
    for op in operations:
        if op[0] == "addx":
            cycle = put_pixel(image, cycle, x_value)
            cycle = put_pixel(image, cycle, x_value)
            x_value += op[1]

        else:
            cycle = put_pixel(image, cycle, x_value)

    image = "".join(image)
    pprint([image[i:i+40] for i in range(0, len(image), 40)])
