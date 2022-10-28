napis = "Dawno, Dawno temu za siódmą górą mieszkała Królewna Śnieżka"
print("Ile jest liter a: ", napis.count("a"))
print("Ile jest liter D: ", napis.count("D"))
print("Ile jest liter ó: ", napis.count("ó"))

tekst = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
print(tekst)
szukany_znak = input("Wpisz szukany tekst: ")
tekst_male=tekst.lower()
iilosc_wystapien = tekst_male.count(f"{szukany_znak}")
print(f""" Ilosc wystapien wyszukiwanego znaku "{szukany_znak}": 
                    {iilosc_wystapien} """)

zdanie = "Ala MA maleGo kota FelicjAna, z którym luBi spędzać CzAs"
duzy = 0
maly = 0

for z in zdanie:
   if z == "a":
       maly +=1
   elif z == "A":
       duzy +=1

print("Moje zdanie wzór:", zdanie)

print("Liczba - a - w tekście:", maly)
print("Liczba - A - w tekście:", duzy)


zdanie = "Annapurna jest Królową Gór"

ilosc_A = zdanie.count("A")
ilosc_a = zdanie.count("a")

print(f"Ilość dużych liter A w zdaniu: ",zdanie, "to:\n", ilosc_A)
print(f"Ilość małych liter a w zdaniu: ",zdanie, "to:\n", ilosc_A)

print(f"Ilość dużych liter A w zdaniu: ",zdanie, "to:\n", zdanie.count("A"))
print(f"Ilość małych liter a w zdaniu: ",zdanie, "to:\n", zdanie.count("a"))
