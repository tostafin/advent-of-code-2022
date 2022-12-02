from typing import List


def get_result_points(result: List[str]) -> int:
    match result:
        case ["A", "X"]:
            return 3 + 0
        case ["A", "Y"]:
            return 1 + 3
        case ["A", "Z"]:
            return 2 + 6

        case ["B", "X"]:
            return 1 + 0
        case ["B", "Y"]:
            return 2 + 3
        case ["B", "Z"]:
            return 3 + 6

        case ["C", "X"]:
            return 2 + 0
        case ["C", "Y"]:
            return 3 + 3
        case ["C", "Z"]:
            return 1 + 6

    raise ValueError(f"Wrong list values: {result}.")


with open("input", "r") as rps_scores:
    print(sum(
        map(lambda r: get_result_points(r), filter(None, map(lambda s: s.split(), rps_scores.read().split("\n"))))
    ))
