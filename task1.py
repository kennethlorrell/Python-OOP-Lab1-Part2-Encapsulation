class Rectangle:
    def __init__(self, width=1.0, length=1.0):
        self.length = width
        self.width = length

    def set_width(self, width):
        if 0 < width < 20 and type(width) is float: 
            self.width = width
        else:
            raise Exception('Invalid value')

    def set_length(self, length):
        if 0 < length < 20 and type(length) is float: 
            self.length = length
        else:
            raise Exception('Invalid value')

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_area(self):
        return self.length * self.width
    
    def get_perimeter(self):
        return self.length * 2 + self.width * 2

    def __str__(self):
        return 'Rectangle with length = {}, width = {}'.format(self.length, self.width)
