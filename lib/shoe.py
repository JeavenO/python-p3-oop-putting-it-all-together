class Shoe:
    def __init__(self, brand, size, color="Unknown"):
        self.brand = brand
        self._size = None
        self.size = size  # Use setter for validation
        self.color = color
        self.condition = "Used"  # default condition

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value > 0:
            self._size = value
        else:
            # Must print exactly what the test expects
            print("size must be an integer")

    def cobble(self):
        # Set condition to "New" after repair
        self.condition = "New"
        # Print exactly what the test expects
        print("Your shoe is as good as new!")
