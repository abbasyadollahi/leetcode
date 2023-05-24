from collections import defaultdict


def solution(right: int, queries: list[int]) -> list[int]:
    color_count = defaultdict(int)
    unique_colors = 0
    unique_colors_history = []
    line = [0] * (right + 1)

    for coord, color in queries:
        if line[coord] != color:
            if line[coord] != 0:
                color_count[line[coord]] -= 1
                if color_count[line[coord]] == 0:
                    unique_colors -= 1

            color_count[color] += 1
            if color_count[color] == 1:
                unique_colors += 1

        line[coord] = color
        unique_colors_history.append(unique_colors)

    return unique_colors_history
