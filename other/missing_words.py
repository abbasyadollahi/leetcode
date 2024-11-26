class Solution:
    def missingWords(self, s: str, t: str) -> list[str]:
        s = s.split(" ")
        t = t.split(" ")
        missing = []

        t_index = 0
        for s_index, word in enumerate(s):
            if t_index == len(t):
                return missing + s[s_index:]
            if word == t[t_index]:
                t_index += 1
            else:
                missing.append(word)

        return missing


sol = Solution()
assert sol.missingWords("I am using hackerrank to improve programming", "am hackerrank to improve") == [
    "I",
    "using",
    "programming",
]
