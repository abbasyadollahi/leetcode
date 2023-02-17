import math


def main() -> None:
    x = "my   home on 222 street !@#is! beautiful! how-is-yours bruv"
    y = split_into_words(x)
    z = split_into_table(y, 3)
    list(map(print, z))


def split_into_words(s: str) -> list[str]:
    n = len(s)
    i = j = 0
    words = []
    while j < n:
        if s[j].isalnum():
            j += 1
        else:
            if i != j:
                words.append(s[i:j])

            i = j + 1
            while i < n and not s[i].isalnum():
                i += 1
            j = i

    if j == n:
        words.append(s[i:j])

    return words


def split_into_table(words: list[str], n: int) -> list[str]:
    """
    Equation
    --------
    Num words   = w
    Num cols    = n
    Num rows    = m = ceil(w / n)
    Remainder   = r = w % n
    table[i][j] = words[i + j*n + min(j, r)]
    """
    w = len(words)
    m = math.ceil(w / n)
    r = w % n
    table = [[None] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            index = i + (j * n) + min(j, r)
            if index < w:
                table[i][j] = words[index]
    return table


main()
