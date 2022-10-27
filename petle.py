czy_znasz_python = False  # ctrl-alt-l porządkuje kod robi spacje
if czy_znasz_python:  # ":" robi wcięcie 4 spacje
    print("Brawo!")
else:
    print("Musisz_sie_uczyc_dalej")

print("Ja jestem poza warunkiem")

# < > <= >= != ==

zarobki = 1500
if zarobki < 10000:
    podatek = 0.0
elif zarobki < 3000:
    podatek = 0.2
elif zarobki < 100000:
    podatek = 0.35
else:
    podatek = 0.40

print(f"zapłacisz {zarobki * podatek} zł")

zarobki = int(input("Proszę, wprowadź swój dochód: "))  # zmiana na int do wprowadzenia cyfr
# < > <= >= != ==

if zarobki < 10000:
    podatek = 0.0
elif zarobki < 30000:
    podatek = 0.2
elif zarobki < 100000:
    podatek = 0.35
else:
    podatek = 0.40

print(f"zapłacisz {zarobki * podatek} zł")


