# plik = open('baza.txt', "r")  # r- tylko do odczytu, w utworzenie/zapis, a pozwala dopisywać dane do pliku
# try:
#   for linia in plik:
#    print(linia.strip())  # strip obcina zbędne elementy puste pola
# finally:
#   plik.close()

# try:
#     plik = open('baza444.txt', "r")
#     for linia in plik:
#         print(linia.strip())
#     plik.close()
# except FileNotFoundError:
#     print("Zła nazwa pliku, spróbuj ponownie...")
# finally:
#     for i in range(5):
#         print(i + 1 * 2)

lista = ["Tomek", "Michał", "Asia"]

# with open("baza.txt", encoding='utf-8') as p:
#     for linia in p:
#         print(linia.strip())
#
with open("baza.txt", "a", encoding="utf-8") as p:
    # p.write("Witaj w świecie Pythona 5 !\n")
    for i in lista:
        p.write(str(i) + "\n")
