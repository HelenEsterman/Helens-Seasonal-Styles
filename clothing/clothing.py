# creating clothing class to be inherited by individual items of clothing
class Clothing:
    def __init__(self, name, color, size, description):
        self.name = name
        self.color = color
        self.size = size
        self.description = description

    # adding method for when object is printed it shows the name instead of a convoluted object
    def __str__(self):
        return f"{self.name}"
