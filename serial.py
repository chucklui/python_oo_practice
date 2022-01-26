from tracemalloc import start


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        """this function takes in a start value and set it to the attribute.
        Have a count attribute set to 0"""

        self.start = start
        self.count = 0
        

    def generate(self):
        """this function return a integer represent number of times
        this method has been called + start attribute value"""

        self.count += 1
        generate = self.start + self.count - 1
        return generate

    def reset(self):
        """this function reset the count back to zero"""

        self.count = 0
