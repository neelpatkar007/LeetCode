class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s1word = s1.split(" ")
        s2word = s2.split(" ")

        comb = s1word + s2word
        wordcount = {}

        for word in comb:
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1

        uncommonwords = [word for word in wordcount if wordcount[word] == 1]
        return uncommonwords