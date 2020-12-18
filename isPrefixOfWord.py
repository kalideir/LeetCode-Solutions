class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str):
        len_searchWord = len(searchWord)
        words = sentence.split(' ')
        for j, word in enumerate(words):
            for i in range(0, len(word) + 1):
                if word[i: len_searchWord] == searchWord:
                    return j + 1 # return the place of word in the sentence (starts from 1)
        return -1
