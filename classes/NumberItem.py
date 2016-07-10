class NumberItem:
    def __init__(self, x, y, z):
        self.coord = (x, y, z)

    def __repr__(self):
        return "Point(%s, %s, %s)" % self.coord