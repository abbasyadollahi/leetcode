import re


def add_underscores(words: str, line_char_limit: int) -> list[str]:
    def space_out(line: list[str], line_length: int) -> str:
        exact, extra = divmod(line_char_limit - line_length, len(line) - 1)

        joiner = "_" * exact
        if len(line) == 1:
            return joiner + line[0] + joiner + "_" * extra
        else:
            return joiner.join(line) + "_" * extra

    tokens = []
    for word in "-".join(re.split(r"\s*-\s*", words)).split():
        hyphen_separated_words = word.split("-")
        for i, hyphen_separated_word in enumerate(hyphen_separated_words[:-1]):
            hyphen_separated_words[i] = hyphen_separated_word + "-"
        tokens.extend(hyphen_separated_words)

    lines = []

    line = []
    line_length = 0

    for i, token in enumerate(tokens):
        if line_length + len(line) + len(token) > line_char_limit:
            lines.append(space_out(line, line_length))

            line = [token]
            line_length = len(token)
        else:
            if "-" in tokens[i - 1]:
                line[-1] += token
            else:
                line.append(token)

            line_length += len(token)

    if line:
        lines.append(space_out(line, line_length))

    return lines


add_underscores("auto-complete is my    go  -   to  ", 8)
add_underscores("auto-complete is my    go  -   to - l ", 8)
add_underscores("auto-complete is my    go  -   to - l ", 14)
