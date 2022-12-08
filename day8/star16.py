from typing import List
from math import prod

with open("input", "r") as trees:
    trees_rows = list(filter(None, trees.read().split("\n")))
    best_scenic_score: int = 0
    for r in range(1, len(trees_rows) - 1):
        for t in range(1, len(trees_rows[r]) - 1):
            scenic_score: List[int] | int = []
            nonblocking_trees: int = 0
            for i in reversed(range(r)):
                nonblocking_trees += 1
                if trees_rows[r][t] <= trees_rows[i][t]:
                    break

            scenic_score.append(nonblocking_trees)

            nonblocking_trees = 0
            for i in range(r + 1, len(trees_rows)):
                nonblocking_trees += 1
                if trees_rows[r][t] <= trees_rows[i][t]:
                    break

            scenic_score.append(nonblocking_trees)

            nonblocking_trees = 0
            for i in reversed(range(t)):
                nonblocking_trees += 1
                if trees_rows[r][t] <= trees_rows[r][i]:
                    break

            scenic_score.append(nonblocking_trees)

            nonblocking_trees = 0
            for i in range(t + 1, len(trees_rows[r])):
                nonblocking_trees += 1
                if trees_rows[r][t] <= trees_rows[r][i]:
                    break

            scenic_score.append(nonblocking_trees)

            best_scenic_score = max(best_scenic_score, prod(scenic_score))

    print(best_scenic_score)
