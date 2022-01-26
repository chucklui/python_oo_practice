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
        Have a count attribute set to 0"""

        self.start = start
        self.next_num = start + 1

    def generate(self):
        """this function return a integer represent number of times
        this method has been called + start attribute value"""

        if self.start + 1 == self.next_num:
            return self.start
        else:
            self.next_num += 1
            return self.next_num - 1

    def reset(self):
        """this function reset the count back to zero"""

        self.next_num = self.start + 1
