class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        # if not len(words):
        #     return ''

        # order = []
        # for pair in zip(words,words[1:]):
        #     for x, y in zip(*pair):
        #         if x != y:
        #             order.append(x+y)
        #             break

        # letters = set(''.join(words))
        # dicts = []

        # while order:
        #         free_letter = letters - set(list(zip(*order))[1])
        #         if not free_letter:
        #             return ''
        #         dicts += free_letter
        #         order = filter(free_letter.isdisjoint, order)
        #         letters -= free_letter

        # return ''.join(dicts + list(letters))

        from collections import defaultdict
        pre = defaultdict(set)
        suc = defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        chars = set(''.join(words))
        charToProcess = chars - set(pre)
        order = ''
        while charToProcess:
            ch = charToProcess.pop()
            order += ch
            for b in suc[ch]:
                pre[b].discard(ch)
                if not pre[b]:
                    charToProcess.add(b)
        return order * (set(order) == chars)

sol = Solution()
print(sol.alienOrder([
  'wrt',
  'wrf',
  'er',
  'ett',
  'rftt'
]))
