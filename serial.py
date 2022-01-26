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

    def __init__(self, start):
        """this function takes in a start value and set it to the attribute.
        Have a next number attribute set to start value"""

        self.start = start
        self.next_num = start

    def generate(self):
        """this function return current serial number"""

        self.next_num += 1
        return self.next_num - 1

    def reset(self):
        """this function reset the next number back to start"""
        
        self.next_num = self.start