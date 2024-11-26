def avoidMonsters(
    m: int,
    n: int,
    start: tuple[int, int],
    end: tuple[int, int],
    monsters: list[tuple[int, int]],
) -> int:
    grid = [
        [min(distance(i, j, monster_i, monster_j) for monster_i, monster_j in monsters) for j in range(n)]
        for i in range(m)
    ]

    return max(traverse(grid, *start, end, float("inf"), set()))


def traverse(
    grid: list[list[int]],
    i: int,
    j: int,
    end: tuple[int, int],
    minimum: int,
    visited: set[tuple[int, int]],
) -> list[int]:
    if (i, j) in visited or i not in range(len(grid)) or j not in range(len(grid[0])):
        return []

    visited.add((i, j))

    if (i, j) == end:
        return [min(minimum, grid[i][j])]

    options = []
    if i - 1 >= 0 and (i - 1, j) not in visited:
        options.append((i - 1, j))
    if i + 1 < len(grid) and (i + 1, j) not in visited:
        options.append((i + 1, j))
    if j - 1 >= 0 and (i, j - 1) not in visited:
        options.append((i, j - 1))
    if j + 1 < len(grid[0]) and (i, j + 1) not in visited:
        options.append((i, j + 1))

    distances = []
    maximum = max((grid[ii][jj] for ii, jj in options), default=None)
    for ii, jj in options:
        if grid[ii][jj] == maximum:
            distances.extend(traverse(grid, ii, jj, end, min(minimum, maximum), visited))
            visited.remove((ii, jj))

    return distances


def distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x2 - x1) + abs(y2 - y1)


print(
    avoidMonsters(
        5,
        5,
        (0, 0),
        (3, 3),
        [
            (0, 3),
            (1, 4),
        ],
    )
)

print(
    avoidMonsters(
        5,
        5,
        (0, 0),
        (4, 4),
        [
            (2, 3),
            (2, 4),
            (3, 2),
            (4, 2),
        ],
    )
)
