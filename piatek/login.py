def wazne_haslo(haslo):  # Ustalenie wartości początkowych.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digits = False
    if len(haslo) >= 7:  # Sprawdzenie długości hasła.
        correct_length = True
    for ch in haslo:
        if ch.isupper():  # Sprawdzenie, czy jest duża litera.
            has_uppercase = True
        if ch.islower():  # Sprawdzenie, czy jest mała litera.
            has_lowercase = True
        if ch.isdigit():  # Sprawdzenie, czy jest cyfra.
            has_digits = True
        # Ustalenie, czy wszystkie wymagania zostały spełnione.
    if correct_length and has_uppercase and has_lowercase and has_digits:
        jest_wazne = True
    else:
        jest_wazne = False
    return jest_wazne
