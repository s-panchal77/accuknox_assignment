class Rectangle:
    """
    A simple Python class representing a Rectangle.
    This is NOT a Django model, just a pure Python class.
    """
    
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        
    def __iter__(self):
        """
        Makes the Rectangle class iterable.
        When we loop over a Rectangle instance, it will yield
        the length dictionary first, and then the width dictionary.
        """
        yield {'length': self.length}
        yield {'width': self.width}
