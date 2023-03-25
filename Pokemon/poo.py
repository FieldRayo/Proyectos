class pokemonCreator():
    def __init__(self):
        self.pokemon = None
        self.name = None
        self.tipo = None
        self.secundario = None
        self.ataques = None
        self.vida = 0
        self.daño = 0
        self.resistencia = 0
        self.nivel = 1
        self.puntos = 10
pC = pokemonCreator()

        #ataques

electrico = {"Ataque basico": {"Daño": 3 + pC.daño, "Coldown": 1},
            "Tormenta electrica": {"Daño": 10 + pC.daño, "Coldown": 2},
            "Rafaga electrica": {"Daño": 6 + pC.daño, "Coldown": 1}}

planta = {"Ataque basico": {"Daño": 5 + pC.daño, "Coldown": 1},
        "Hiedra picuda": {"Daño": 8 + pC.daño, "Coldown": 2},
        "Picos afilados": {"Daño": 6 + pC.daño, "Coldown": 1}}

agua = {"Ataque basico": {"Daño": 2 + pC.daño, "Coldown": 1},
        "Tsunami": {"Daño": 11 + pC.daño, "Coldown": 2},
         "Tormenta": {"Daño": 5 + pC.daño, "Coldown": 1}}

fuego = {"Ataque basico": {"Daño": 3 + pC.daño, "Coldown": 1},
        "Fuego atormentante": {"Daño": 10 + pC.daño, "Coldown": 2},
        "Lava": {"Daño": 6 + pC.daño, "Coldown": 1}}

class pokemons():
    def __init__(self):
        #Pokemones
        self.pikachu = pokemonCreator()
        self.bulbasaur = pokemonCreator()
        self.squirtle = pokemonCreator()
        self.charmander = pokemonCreator()
        self.charizard = pokemonCreator()
        self.blastoise = pokemonCreator()
        self.kartana = pokemonCreator()

        #Establecer stats

        #Pikachu
        self.pikachu.pokemon = "Pikachu"
        self.pikachu.tipo = "Electrico"
        self.pikachu.ataques = electrico
        self.pikachu.vida = 10
        self.pikachu.daño = 15
        self.pikachu.resistencia = 5
        self.pikachu.secundario = None

        #Bulbasaur
        self.bulbasaur.pokemon = "Bulbasaur"
        self.bulbasaur.tipo = "Planta"
        self.bulbasaur.ataques = planta
        self.bulbasaur.vida = 7
        self.bulbasaur.daño = 14
        self.bulbasaur.resistencia = 11
        self.bulbasaur.secundario = "Veneno"

        #Squirtle
        self.squirtle.pokemon = "Squirtle"
        self.squirtle.tipo = "Agua"
        self.squirtle.ataques = agua
        self.squirtle.vida = 6
        self.squirtle.daño = 16
        self.squirtle.resistencia = 5
        self.pikachu.secundario = None

        #Charmander
        self.charmander.pokemon = "Charmander"
        self.charmander.tipo = "Fuego"
        self.charmander.ataques = fuego
        self.charmander.vida = 14
        self.charmander.daño = 12
        self.charmander.resistencia = 5
        self.pikachu.secundario = None

        #Charizard
        self.charizard.pokemon = "Charizard"
        self.charizard.tipo = "Fuego"
        self.charizard.ataques = fuego
        self.charizard.vida = 20
        self.charizard.daño = 20
        self.charizard.resistencia = 13
        self.charizard.secundario = "Volador"

        #Blastoise
        self.blastoise.pokemon = "Blastoise"
        self.blastoise.tipo = "Agua"
        self.blastoise.ataques = agua
        self.blastoise.vida = 15
        self.blastoise.daño = 15
        self.blastoise.resistencia = 7
        self.blastoise.secundario = None

        #Kartana
        self.kartana.pokemon = "Kartana"
        self.kartana.tipo = "Planta"
        self.kartana.ataques = planta
        self.kartana.vida = 8
        self.kartana.daño = 25
        self.kartana.resistencia = 8
        self.kartana.secundario = "Acero"










