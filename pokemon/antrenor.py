class antrenor:
    def __init__(self, nume, pokemoni):
        self.nume = nume
        self.pokemoni = pokemoni

    def alege_pokemon(self):
        print(self.nume," Alegeti pokemonul dorit:\n")
        for i in range (len(self.pokemoni)):
            print(f'{i+1}. {self.pokemoni[i].nume}\n')
        choice = input("Alegere: ")
        return self.pokemoni[int(choice) - 1]

    def are_pokemoni_vii(self):    
        if self.pokemoni:
            return True
        return False

    def test():
        pass