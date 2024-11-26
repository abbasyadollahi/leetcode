"""
Given a list of strings represented as below, sort by name first then by roman numeral.

Input: ['Louis IX', 'Louis VIII', 'Charles II']
Output: ['Charles II', 'Louis VIII', 'Louis IX']
"""


def roman_to_number(roman: str) -> int:
    value = {"I": 1, "V": 5, "X": 10}

    number = 0
    for i, letter in enumerate(roman):
        if i < len(roman) - 1 and value[letter] < value[roman[i + 1]]:
            number -= value[letter]
        else:
            number += value[letter]

    return number


def sort_king(king: str) -> tuple[str, int]:
    name, roman = king.split()
    return (name, roman_to_number(roman))


def sort_kings(kings: list[str]) -> list[str]:
    return sorted(kings, key=sort_king)


assert sort_kings(["Louis IX", "Louis VIII", "Charles II"]) == [
    "Charles II",
    "Louis VIII",
    "Louis IX",
]
