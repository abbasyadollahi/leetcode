class Solution:
    def textQueries(self, sentences, queries):
        """
        :type sentences: String
        :type queries: String
        """

        all_words = []
        for sentence in sentences:
            all_words.append(set(sentence.split(' ')))

        for query in queries:
            found = False
            for line, sentence in enumerate(all_words):
                if all(word in sentence for word in query.split(' ')):
                    found = True
                    print(line, end=' ')
            print('' if found else -1)
