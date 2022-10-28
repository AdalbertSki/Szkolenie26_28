from piatek import login

if __name__ == '__main__':
    haslo= input("Podaj haslo..")

    if not login.wazne_haslo(haslo):
        print("Hasło jest niepoprawne")
    else:
        print(" OK, hasło jest poprawne")
