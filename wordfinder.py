from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        """ define the word list and print number of words read """
        self.path = path
        self.word_list = self.get_word_list()
        self.words_read()

    def get_word_list(self):
        """ return a list of words from the doc in the path"""
        word_doc = open(self.path, "r")
        return word_doc.read().split("\n")

    def random(self):
        """ return a random word from the list"""
        return choice(self.word_list)

    def words_read(self):
        """ print number of words read """
        print(f"{len(self.word_list)} words read")
