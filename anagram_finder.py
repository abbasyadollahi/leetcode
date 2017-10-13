from itertools import chain

class Solution(object):
	def anagramFinder(self, words, anagram):
	    """
        :type words: string
        :type anagram: string
        """
        ana_len = len(anagram)
		words_len = len(words)
		double_char = []
		good = False

		for idx, char in enumerate(anagram):
			if anagram.count(char) > 1:
				double_char.append([char, anagram.count(char)])

		for i, c in enumerate(words):
			if i == words_len - ana_len - 1:
				break

			str_list = words[i:i+ana_len]

			if not str_list.strip(anagram):
				for char, count in double_char:
					if str_list.count(char) == count:
						good = True
					else:
						good = False
						break

				if good:
					print("Found one: {}".format(str_list))

