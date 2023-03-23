class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if x == None and y == None:
            self.x = 0
            self.y = 0
    def __str__(self):
        return "Punto:({},{})".format(self.x, self.y)   
    def cuadrante(self):
        if self.x > 0:
            if self.y > 0:
                return "El punto pertenece al primer cuadrante"
            elif self.y < 0:
                return "El punto pertenece al cuarto cuadrante"
            else:
                return "El punto se encuentra sobre el eje x"
        elif self.x < 0:
            if self.y > 0:
                return "El punto pertenece al segundo cuadrante"
            elif self.y < 0:
                return "El punto pertenece al tercer cuadrante"
            else:
                return "El punto se encuentra sobre el eje x"
        else:
            return "El punto se encuentra sobre el eje y"       