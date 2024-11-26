import string


def solve(s: str) -> str:
    index = 1
    reset = False
    reset_index = 0
    characters = list(s)
    while index < len(characters):
        if reset:
            characters[index] = string.ascii_lowercase[reset_index % 2]
            reset_index += 1
        elif characters[index - 1] >= characters[index]:
            reset = True
            while characters[index] == "z":
                if index == 0:
                    return "-1"
                index -= 1

            characters[index] = chr(ord(characters[index]) + 1)
        index += 1

    return "".join(characters)
