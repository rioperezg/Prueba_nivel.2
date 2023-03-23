class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if x == None and y == None:
            self.x = 0
            self.y = 0
    def __str__(self):
        return "Punto:({},{})".format(self.x, self.y)        