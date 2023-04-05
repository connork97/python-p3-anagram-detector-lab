# your code goes here!

class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, list):
        matched_words = []
        word_letters = [letter for letter in self.word]
        word_letters.sort()
        for word in list:
            list_word_letters = [letter for letter in word]
            list_word_letters.sort()
            if(word_letters == list_word_letters):
                matched_words.append(word)
            else:
                print("Word does not match")
        return matched_words
