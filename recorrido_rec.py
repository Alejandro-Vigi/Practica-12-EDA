import turtle
import argparse

def recorrido(tortuga, espacio, huellas):
    if huellas > 0:
        tortuga.stamp()
        espacio = espacio + 3
        tortuga.forward(espacio)
        tortuga.right(24)
        recorrido(tortuga, espacio, huellas-1)
        
ap = argparse.ArgumentParser()
ap.add_argument("--huellas", required=True, help="número de huellas")
args = vars(ap.parse_args())

huellas = int(args["huellas"])
espacio = 15
recorrido(turtle, huellas, espacio)