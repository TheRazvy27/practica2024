class batalie:
    def lupta(self, antrenor1, antrenor2):
        pokemon1 = antrenor1.alege_pokemon()
        pokemon2 = antrenor2.alege_pokemon()
        while True:
            print(pokemon1.nume, " vs ",pokemon2.nume)
            print ("Pokemon1: ", pokemon1.nume, " ", pokemon1.viata)
            print ("Pokemon2: ", pokemon2.nume, " ", pokemon2.viata)          
            pokemon1.ataca(pokemon2)
            print ("Pokemon1: ", pokemon1.nume, " ", pokemon1.viata)
            print ("Pokemon2: ", pokemon2.nume, " ", pokemon2.viata)
            if not pokemon2.este_viu():
                print (pokemon2.nume, " A murit!")
                for i in range(len(antrenor2.pokemoni)):
                    if not antrenor2.pokemoni[i - 1].este_viu():
                        antrenor2.pokemoni.pop(i - 1)
                if not antrenor2.are_pokemoni_vii():
                    print(antrenor2.nume, " Nu mai are pokemoni! Game over!")
                    break
                pokemon2 = antrenor2.alege_pokemon()                   
            pokemon2.ataca(pokemon1)
            print ("Pokemon1: ", pokemon1.nume, " ", pokemon1.viata)
            print ("Pokemon2: ", pokemon2.nume, " ", pokemon2.viata)
            if not pokemon1.este_viu():
                print (pokemon1.nume, " A murit!")
                for i in range(len(antrenor1.pokemoni)):
                    if not antrenor1.pokemoni[i - 1].este_viu():
                        antrenor1.pokemoni.pop(i - 1)
                if not antrenor1.are_pokemoni_vii():
                    print(antrenor1.nume, " Nu mai are pokemoni! Game over!")
                    break
                pokemon1 = antrenor1.alege_pokemon()   
                     

    
    def test():
        pass