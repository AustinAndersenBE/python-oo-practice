import random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """
    A class to find random words from a file.
    

    >>> wf = WordFinder("words.txt")
    235886 words read
    >>> type(wf.random()) is str # it should return a string
    True
    """

    def __init__ (self, file_path: str):
        """
        Initialize the WordFinder with file path.

        Parameters:
            file_path (str): The path to the file with the words.
        """
        self.file_path = file_path
        self.words = self.load_words()
        print(f"{len(self.words)} words read")

    def load_words(self) -> list:
        """
        Loads words from the file and stores them in a list

        Returns: a list of words from the file

        """
        with open(self.file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
        
    def random(self) -> str:
        """
        Returns a random word from the list of words.
        """
        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """
    This is a subclass of WordFinder that filters out comments and blank lines

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def load_words(self) -> list:
        """swf's version of load_words which also filters out comments and blank lines"""
        all_words = super().load_words()

        return [word for word in all_words if word and not word.startswith("#")]

swf = SpecialWordFinder("complex.txt")
print(type(swf.random()) is str)  # This should print True


