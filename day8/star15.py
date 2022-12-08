from typing import Final

with open("input", "r") as trees:
    trees_rows = list(filter(None, trees.read().split("\n")))
    outside_visible: Final[int] = 2 * len(trees_rows[0]) + 2 * len(trees_rows) - 4
    interior_visible: int = 0
    for r in range(1, len(trees_rows) - 1):
        for t in range(1, len(trees_rows[r]) - 1):
            for i in range(r):
                if trees_rows[r][t] <= trees_rows[i][t]:
                    break
                if i == r - 1:
                    interior_visible += 1
            else:
                continue

            for i in range(r + 1, len(trees_rows)):
                if trees_rows[r][t] <= trees_rows[i][t]:
                    break
                if i == len(trees_rows) - 1:
                    interior_visible += 1
            else:
                continue

            for i in range(t):
                if trees_rows[r][t] <= trees_rows[r][i]:
                    break
                if i == t - 1:
                    interior_visible += 1
            else:
                continue

            for i in range(t + 1, len(trees_rows[r])):
                if trees_rows[r][t] <= trees_rows[r][i]:
                    break
                if i == len(trees_rows[r]) - 1:
                    interior_visible += 1
            else:
                continue

    print(outside_visible + interior_visible)
