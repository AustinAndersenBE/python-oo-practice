"""Python serial number generator."""

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


    def __init__ (self, start: int):
        """
        Initialize the SerialGenerator with a start number.

        Parameters:
            start (int): The starting number for the serial numbers.
        """
        self.start = start
        self.current_value = start

    def generate(self) -> int:
        """
        Generate the next serial number.
        """
        serial_number = self.current_value
        self.current_value += 1
        return serial_number
    
    def reset(self):
        """
        Reset the serial number to the original start number.
        """ 
        self.current_value = self.start
