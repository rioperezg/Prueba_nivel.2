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
       x = input("Introduzca la coordenada x de su punto:")
       y = input("Introduzca la coordenada y de su punto:")
       P = Punto(x, y)
       return P.vector()
    elif opcion == "4":        

    elif opcion == "5":

    elif opcion == "6":

    elif opcion == "7":




