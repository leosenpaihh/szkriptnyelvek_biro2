def hogolyo_csata(korok: list):
    statisztikak = {}

    for kor in korok:
        for jatekos, adatok in kor.items():
            if jatekos not in statisztikak:
                statisztikak[jatekos] = {
                    'eldobott_hogolyok': 0,
                    'talalt': 0,
                    'fejtalalat': 0
                }
            statisztikak[jatekos]['eldobott_hogolyok'] += adatok.get('eldobott_hogolyok', 0)
            statisztikak[jatekos]['talalt'] += adatok.get('talalt', 0)
            statisztikak[jatekos]['fejtalalat'] += adatok.get('fejtalalat', 0)

    return statisztikak


def hogolyo_pontossag(statisztikak):
    for jatekos, adatok in statisztikak.items():
        eldobott = adatok['eldobott_hogolyok']
        talalt = adatok['talalt']

        if eldobott > 0:
            adatok['pontossag'] = talalt / eldobott
        else:
            adatok['pontossag'] = 0

    return statisztikak


def hogolyo_piros_lap(statisztikak):
    piros_lap = []

    for jatekos, adatok in statisztikak.items():
        eldobott = adatok['eldobott_hogolyok']
        talalt = adatok['talalt']

        if eldobott > 0 and talalt > 0:
            fejtalalat_arany = adatok['fejtalalat'] / talalt
            if adatok['pontossag'] >= 0.7 and fejtalalat_arany >= 0.5:
                piros_lap.append(jatekos)

    return piros_lap
