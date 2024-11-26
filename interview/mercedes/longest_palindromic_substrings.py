def longest_palindromic_substrings(s: str) -> set[str]:
    def expand(l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]

    longest = ""
    substrings = set()
    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)

        if len(odd) > len(longest) or len(even) > len(longest):
            substrings.clear()
            longest = max(odd, even, key=len)

        if len(odd) == len(longest):
            substrings.add(odd)
        if len(even) == len(longest):
            substrings.add(even)

    return substrings


assert longest_palindromic_substrings("deabbaceffeg") == {"abba", "effe"}
assert longest_palindromic_substrings("deabbac") == {"abba"}
assert longest_palindromic_substrings("deabac") == {"aba"}
assert longest_palindromic_substrings("abcdefg") == {"a", "b", "c", "d", "e", "f", "g"}
