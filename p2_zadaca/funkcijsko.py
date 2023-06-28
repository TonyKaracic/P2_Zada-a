# Definicija funkcije koja ispisuje "Pozdrav {ime}!"
def pozdrav(ime):
    return f"Pozdrav {ime}!"

# Definicija lambda izraza koji ispisuje "Dobrodošao {ime}!"
dobrodosao = lambda ime: f"Dobrodošao {ime}!"

# Definicija funkcije koja poziva funkciju za ispis dobrodošlice
def pozovi_funkciju(func, ime):
    return func(ime)

# Poziv treće funkcije s prvom definiranom funkcijom
rezultat = pozovi_funkciju(pozdrav, "Antonio ")
print(rezultat)

# Poziv treće funkcije s drugom definiranom funkcijom (lambda izraz)
rezultat = pozovi_funkciju(dobrodosao, "Antonio ")
print(rezultat)
