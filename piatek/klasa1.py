class Dom:
    '''
    To jest klasa DOM, która sprawdza działanie OOP w Pytonie
    '''
    metraz = 0
    kolor = ""
    ilosc_okien = 0

    # def okresl_metraz(self):
    #     wybor = int(input("Podaj metraż "))
    #     self.metraz = wybor
    #     print("Metraż wynosi: ", self.metraz)
    #
    # def okresl_kolor(self):
    #     wybor = input("Podaj kolor ")
    #     self.kolor = wybor
    #     print("Kolor wynosi: ", self.kolor)
    #
    # def okresl_okna(self):
    #     wybor = int(input("Podaj ilość okien "))
    #     self.ilosc_okien = wybor
    #     print("Ilość okien wynosi: ", self.ilosc_okien)


class Dom2:
    '''
    To jest klasa DOM2, która sprawdza działanie
    OOP w Pythonie...
    '''
    def __init__(self, metraz, kolor, ilosc_okien):
        self.metraz = metraz
        self.kolor = kolor
        self.ilosc_okien = ilosc_okien
    def zmien_metraz(self):
        wybor = int(input("Podaj metraż "))
        self.metraz = wybor
        print("Metraż wynosi: ", self.metraz)

    def zmien_kolor(self):
        wybor = input("Podaj kolor ")
        self.kolor = wybor
        print("Kolor wynosi: ", self.kolor)

    def zmien_okna(self):
        wybor = int(input("Podaj ilość okien "))
        self.ilosc_okien = wybor
        print("Ilość okien wynosi: ", self.ilosc_okien)
