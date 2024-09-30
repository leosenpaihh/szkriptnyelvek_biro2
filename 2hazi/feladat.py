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