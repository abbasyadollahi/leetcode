class Solution:
    def latestBushGroup(self, a: list[int], k: int, m: int) -> int:
        a_len = len(a)
        days = [1] * a_len

        for day, i in enumerate(a[-1:k*m-a_len-1:-1]):
            days[i-1] = 0

            k_count = 0
            m_count = 0

            for rose in days:
                if rose == 1:
                    k_count += 1
                else:
                    if k_count >= k:
                        m_count += 1
                    k_count = 0

            if k_count >= k:
                m_count += 1

            if m_count >= m:
                return a_len - day - 1

        return -1


sol = Solution()
print(sol.latestBushGroup([1,4,3,2,5], 1, 3))
print(sol.latestBushGroup([1,2,7,6,4,3,5], 2, 2))
print(sol.latestBushGroup([1,2,3,5,6,7,4], 3, 2))
