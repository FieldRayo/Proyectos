from poo import *
from VerEstadisticas import *


def elejirstats():

    resistencia = int(input("Resistencia > "))
    if pokemon.puntos - resistencia > 0:
        pokemon.resistencia += resistencia
        pokemon.puntos -= resistencia
    else:
        pokemon.resistencia += pokemon.puntos if resistencia >= pokemon.puntos else pokemon.puntos - resistencia
        return None
    print(f"Te quedan {pokemon.puntos} puntos")
    daño = int(input("Daño > "))
    if pokemon.puntos - daño > 0:
        pokemon.daño += daño
        pokemon.puntos -= daño
    else:
        pokemon.daño += pokemon.puntos if daño >= pokemon.puntos else pokemon.puntos - daño
        return None
    print(f"Te quedan {pokemon.puntos} puntos")
    vida = int(input("Vida > "))
    if pokemon.puntos - vida > 0:
        pokemon.vida += vida
        pokemon.puntos -= vida
    else:
        pokemon.vida += pokemon.puntos if vida >= pokemon.puntos else pokemon.puntos - vida
        return None
    print(f"Te quedan {pokemon.puntos} puntos")




def pelear():
    eleccion = input(
        "Con quien quieres pelear? \n"
        "1. Pikachu\n"
        "2. charizard\n"
        "3. kartana\n"
        ">>> "
    )
    if eleccion == "1":
        eleccion = pokemons().pikachu
    if eleccion == "2":
        eleccion = pokemons().charizard
    if eleccion == "3":
        eleccion = pokemons().kartana
    print(f"Tu oponente es {eleccion}!")

pokemon = pokemonCreator()
pokemon.pokemon = input(
    "Elije el pokemon \n"
    "1. Pikachu\n"
    "2. Charmander\n"
    "3. Squirtle\n"
    ">>> "

)

if pokemon.pokemon == "1":
    pokemon = pokemons().pikachu
if pokemon.pokemon == "2":
    pokemon = pokemons().charmander
if pokemon.pokemon == "3":
    pokemon = pokemons().squirtle

pokemon.name = input("Ingrese nombre de su pokemon: ")
print("Tienes 10 puntos, utilizalos sabiamente:")

elejirstats()

print(
    f"Las estadisticas de tu {pokemon.pokemon}('{pokemon.name}') de tipo {pokemon.tipo} son:\n"
    f"Daño: {pokemon.daño}, \n"
    f"Resistencia: {pokemon.resistencia}, \n"
    f"Vida: {pokemon.vida}. \n"
    f"Nivel: {pokemon.nivel}\n"
    f"Puntos: {pokemon.puntos}\n"
    f"\nAtaques:\n{pokemon.ataques}"
)

pelear()