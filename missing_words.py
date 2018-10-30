class Solution:
    def missingWords(self, s, t):
        """
        :type s: String
        :type t: String
        :rtype: List[String]
        """

        s = s.split(' ')
        t = t.split(' ')
        missing = []

        t_idx = 0
        t_len = len(t)
        for s_idx, word in enumerate(s):
            if t_idx == t_len:
                return missing + s[s_idx:]
            if word == t[t_idx]:
                t_idx += 1
            else:
                missing.append(word)

        return missing

sol = Solution()
print(sol.missingWords('I am using hackerrank to improve programming', 'am hackerrank to improve'))
