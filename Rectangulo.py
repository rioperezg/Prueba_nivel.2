import Punto
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
        
        