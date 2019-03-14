
class Barrier:
    x, y = 60, 60
    size_x, size_y = 10, 20

    def __init__(self, x, y, size_x, size_y):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

    def get_bounds(self):
        return [self.x, self.y, self.x + self.size_x, self.y + self.size_y]
