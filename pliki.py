# plik = open('baza.txt', "r")  # r- tylko do odczytu, w utworzenie/zapis, a pozwala dopisywać dane do pliku
# try:
#   for linia in plik:
#    print(linia.strip())  # strip obcina zbędne elementy puste pola
# finally:
#   plik.close()

try:
    plik = open('baza444.txt', "r")
    for linia in plik:
        print(linia.strip())
    plik.close()
except FileNotFoundError:
    print("Zła nazwa pliku, spróbuj ponownie...")
finally:
    for i in range(5):
        print(i + 1 * 2)

with open('baza.txt') as p:
    for linia in p:
        print(linia.strip())
