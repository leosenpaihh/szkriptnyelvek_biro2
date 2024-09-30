def nyertes_korok(urmacskak,szuperegerek: list):

    if len(urmacskak) != len(szuperegerek):
        return -1
    if urmacskak == [] or szuperegerek == []:
        return -1

    nyertes_pontok = 0
    for pontok in range(len(urmacskak)):
        if urmacskak[pontok] > szuperegerek[pontok]:
            nyertes_pontok += 1

    return nyertes_pontok

#Tesztelés
#print(nyertes_korok(urmacskak=[30, 50, 10, 80, 100, 40],szuperegerek=[60, 20, 10, 20, 30, 20]))