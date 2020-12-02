from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    ignore = []

    def __init__(self, path):
        """ define the word list and print number of words read """
        self.path = path
        self.word_list = self.get_word_list()
        self.read_words()

    def __repr__(self):
        return f"<WordFinder path={self.path}>"

    # TO DO: change this from .read() to .readlines() to save memory space
    def get_word_list(self):
        """ return a list of words from the doc in the path"""
        word_doc = open(self.path, "r")
        return word_doc.read().split("\n")

    def filter_word_list(self):
        return None

    def random(self):
        """ return a random word from the list"""
        return choice(self.word_list)

    def read_words(self):
        """ print number of words read """
        print(f"{len(self.word_list)} words read")


class SpecialWordFinder(WordFinder):
    """ WordFinder that filters word list """
    ignore = ['\n', '#']
    # def __init__(self, path):
    #     """ get parent class (WordFinder),
    #     call it's init, call filter word list function """
    #     super().__init__(path)
    #     self.filter_word_list()


    def filter_word_list(self):
        """ Filter word list by removing empty strings and words that start 
        with # """
        self.word_list = [ word for word in self.word_list if 
        not word.startswith("#") 
        and word]
        
        