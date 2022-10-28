# from piatek import login
#
# if __name__ == '__main__':
#     haslo= input("Podaj haslo..")
#
#     if not login.wazne_haslo(haslo):
#         print("Hasło jest niepoprawne")
#     else:
#         print(" OK, hasło jest poprawne")

from piatek import klasa1 as k1

dom1 = k1.Dom()
print(dom1)
# print(dom1.metraz)
# dom1.okresl_metraz()
# print(dom1.metraz)
dom1.okresl_kolor()

# dom2 = k1.Dom()
# print(dom2)
# dom2.okresl_kolor()
# print("Dom2 ma kolor:", dom2.kolor)

dom3 = k1.Dom2(100, "czerwony", 3)
print(dom3.metraz)
print(dom3.ilosc_okien)
print(dom3.kolor)
dom3.zmien_okna()
print(dom3.ilosc_okien)

