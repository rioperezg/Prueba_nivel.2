import Punto
from Rectangulo import Rectangulo
class Rectangulo:
    def __init__(self, P_inicial, P_final): 
        if P_inicial and P_final == None:
            P_inicial = Punto(None, None)
            P_final = Punto(None, None)
        else:
            P_inicial = Punto()
            P_final = Punto()
            self.P_inicial = P_inicial
            self.P_final = P_final
    def __str__(self):
        return "Rectangulo formado por -- {} y -- {}".format(self.P_inicial.__str__(), self.P_final.__str__())
    def base(self):        
        comp_x_ini = self.P_inicial.x
        comp_x_fin = self.P_final.x
        print("La base del rectangulo forma por los puntos:({},{}) y ({},{})".format(self.P_inicial.x, self.P_inicial.y, self.P_final.x, self.P_final.y)) 
        return abs(comp_x_ini - comp_x_fin)
    def altura(self):
        comp_y_ini = self.P_inicial.y
        comp_y_fin = self.P_final.y
        print("La Altura del rectangulo forma por los puntos:({},{}) y ({},{})".format(self.P_inicial.x, self.P_inicial.y, self.P_final.x, self.P_final.y)) 
        return abs(comp_y_ini - comp_y_fin)
    def Area(self):
        print("Area del rectangulo:")
        return Rectangulo.base(self)*Rectangulo.altura(self)