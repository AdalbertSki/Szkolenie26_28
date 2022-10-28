plik = open('baza.txt', "r")  # r- tylko do odczytu, w utworzenie/zapis, a pozwala dopisywać dane do pliku
try:
    for linia in plik:
        print(linia.strip())  # strip obcina zbędne elementy puste pola
finally:
    plik.close()