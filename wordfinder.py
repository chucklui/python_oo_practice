class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, location):
        self.location = location
        self.words = []
    
    def random(self):
        print

    def extract_data(self):
        words_file = open(self.location, 'r')
        for word in words_file:
            self.words.append(word)
            

