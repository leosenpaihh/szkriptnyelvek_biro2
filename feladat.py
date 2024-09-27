# Nev: Lakatos Leonardó Demeter
# Neptun: HME82K
# h: h373985

def szekem(sorSzam: int):
    sor = sorSzam//14+1 #sor meghatarozas
    oldal = "bal"
    maradek = sorSzam % 14
    szek = 7 - maradek + 1 #szek meghataorzas


    if maradek == 0:
        sor -= 1
        szek -= 1

    elif maradek <= 7:
        oldal = "jobb"

    else:
        szek = maradek - 7

    return f"{sor}. sor, {oldal} {szek}. szek"

print(szekem(15))