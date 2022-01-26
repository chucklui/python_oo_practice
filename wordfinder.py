import random
import os


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, location):
        '''Takes an input location for a file of words, then runs extract_data
        method to extract the words into self.words'''

        self.location = location
        self.words = []

        self.extract_data()
        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"<WordFinder location = {self.location}, words = {self.words}"

    def random(self):
        '''Returns a random word from the list of words'''

        return random.choice(self.words)

    def extract_data(self):
        '''Extracts the words from file at self.location and saves them to
        self.words. Returns nothing'''

        print(f"In extract_data, location = {self.location}")
        words_file = open(self.location, "r")

        for word in words_file:
            print(f"word = {word}")
            self.words.append(word.strip())

        words_file.close()
