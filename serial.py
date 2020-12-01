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
        """ create instance and initiate current count"""
        self.start = start
        self.current_count = start - 1

    def generate(self):
        """ increment current count """
        self.current_count += 1
        return self.current_count

    def reset(self):
        """ reset current count"""
        self.current_count = self.start - 1
