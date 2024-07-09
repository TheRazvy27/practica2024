class pokemon:
    def __init__(self, nume, tip, viata, putere_atac):
        #print("initializare")
        self.nume = nume
        self.tip = tip
        self.viata = viata
        self.putere_atac = putere_atac

    def ataca(self, inamic):
        if (self.tip == "Apa" and inamic.tip == "Foc"):
            inamic.viata -= 2 * self.putere_atac
            return inamic.viata
        if (self.tip == "Foc" and inamic.tip == "Pamant"):
            inamic.viata -= 2 * self.putere_atac       
            return inamic.viata     
        if (self.tip == "Pamant" and inamic.tip == "Apa"):
            inamic.viata -= 2 * self.putere_atac
            return inamic.viata
        inamic.viata -= self.putere_atac
        return inamic.viata

    def este_viu(self):
        if (self.viata <= 0):
            return False
        else:
            return True

    def testare(self):
        print(self.nume, " ", self.tip, " ", self.viata, " ", self.putere_atac)


#class TelecomAcademy:
#  def  __init__(self, course_name):
#    print("Se executa metoda init")
#    self.course_name = course_name
#
#  def print_course_name(self):
#    print(self.course_name)#
#
#python = TelecomAcademy("Python")
#python.print_course_name()#
#
#java = TelecomAcademy("Java")
#java.print_course_name()