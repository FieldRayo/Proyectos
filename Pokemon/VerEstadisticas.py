from poo import *

def verEstadisticas(x):
    pk = pokemons()
    if x == "kartana":
        print(
        f"Stats de kartana:\n"
        f"Nivel = {pk.kartana.nivel}"
        f"Tipo = {pk.kartana.tipo}"
        f"Daño = {pk.kartana.daño}"
        f"Vida = {pk.kartana.vida}"
        f"Resistencia = {pk.kartana.resistencia}"
        )