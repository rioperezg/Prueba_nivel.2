from Punto import Punto 
from Rectangulo import Rectangulo

def iniciar():
    print("===================================")
    print("===================================")
    print("[1] Crear Puntos                   ")
    print("[2] Consultar Cuadrante            ")
    print("[3] Crear Vectores                 ")
    print("[4] Consultar distancia            ")
    print("[5] Crear Rectangulos              ")
    print("[6] Consultar base del Rectangulo  ")
    print("[7] Consultar Altura del Rectangulo")
    print("[8] Consultar Area del Rectangulo  ")
    print("===================================")
    opcion = input(">")
    if opcion == "1":
       print("Creando Punto...\n")
       x = input("Introduzca la coordenada x de su punto:")
       y = input("Introduzca la coordenada y de su punto:")
       P = Punto(x, y)
       print ("Punto creado")
       return P.__str__()
    elif opcion == "2":
       print("Consultando Cuadrante...\n")
       x = input("Introduzca la coordenada x de su punto:")
       y = input("Introduzca la coordenada y de su punto:")
       P = Punto(x, y)
       return P.cuadrante()
    elif opcion == "3":
       print("Creando vectores...\n")
       x1 = input("Introduzca la coordenada x de su punto:")
       y1 = input("Introduzca la coordenada y de su punto:")
       P = Punto(x1, y1)
       x2 = input("Introduzca la coordenada x del otro punto:")
       y2 = input("Introduzca la coordenada y del otro punto:")
       Q = Punto(x2,y2)
       return Punto.vector(self = P, other = Q)
    elif opcion == "4":        
       print("Consultando distancia...\n")
       x1 = input("Introduzca la coordenada x de su punto:")
       y1 = input("Introduzca la coordenada y de su punto:")
       P = Punto(x1, y1)
       x2 = input("Introduzca la coordenada x del otro punto:")
       y2 = input("Introduzca la coordenada y del otro punto:")
       Q = Punto(x2,y2)
       return Punto.distancia(self = P, other = Q)
    elif opcion == "5":
       print("Creando Rectangulo...\n")
       x1 = input("Introduzca la coordenada x de su punto:")
       y1 = input("Introduzca la coordenada y de su punto:")
       P = Punto(x1, y1)
       x2 = input("Introduzca la coordenada x del otro punto:")
       y2 = input("Introduzca la coordenada y del otro punto:")
       Q = Punto(x2,y2)
       rect = Rectangulo(P_inicial= P, P_final= Q)
       print("Rectangulo creado")
       return rect.__str__()
    elif opcion == "6":
       print("Consultando base del rectangulo...\n")
       x1 = input("Introduzca la coordenada x de su punto:")
       y1 = input("Introduzca la coordenada y de su punto:")
       P = Punto(x1, y1)
       x2 = input("Introduzca la coordenada x del otro punto:")
       y2 = input("Introduzca la coordenada y del otro punto:")
       Q = Punto(x2,y2)
       rect = Rectangulo(P_inicial= P, P_final= Q)
       return rect.base()
    elif opcion == "7":
       print("Consultando Altura del rectangulo...\n")
       x1 = input("Introduzca la coordenada x de su punto:")
       y1 = input("Introduzca la coordenada y de su punto:")
       P = Punto(x1, y1)
       x2 = input("Introduzca la coordenada x del otro punto:")
       y2 = input("Introduzca la coordenada y del otro punto:")
       Q = Punto(x2,y2)
       rect = Rectangulo(P_inicial= P, P_final= Q)
       return rect.altura()
    elif opcion == "8":   
       print("Consultando Area del rectangulo...\n")
       x1 = input("Introduzca la coordenada x de su punto:")
       y1 = input("Introduzca la coordenada y de su punto:")
       P = Punto(x1, y1)
       x2 = input("Introduzca la coordenada x del otro punto:")
       y2 = input("Introduzca la coordenada y del otro punto:")
       Q = Punto(x2,y2)
       rect = Rectangulo(P_inicial= P, P_final= Q)
       return rect.base()



