from pokemon import pokemon
from antrenor import antrenor
from batalie import batalie


if True:
    Charmander = pokemon("Charmender", "Foc", 50, 10)
    #Charmander.testare()
    Bulbasaur = pokemon("Bulbasaur", "Pamant", 60, 8)
    #Bulbasaur.testare()
    Squirtle = pokemon("Squirtle", "Apa", 40, 14)
    #Squirtle.testare()

    Torchic = pokemon("Torchic", "Foc", 55, 12)
    Piplup = pokemon("Piplup", "Apa", 45, 13)
    Snivy = pokemon("Snivy", "Pamant", 65, 7)

    Gigel = antrenor("Gigel", [Bulbasaur, Charmander, Squirtle])
    Vasile = antrenor("Vasile", [Torchic, Piplup, Snivy])
    #print(Gigel.pokemoni)
    #print(Vasile.pokemoni)
    Lupta = batalie()
    Lupta.lupta(Gigel, Vasile)
