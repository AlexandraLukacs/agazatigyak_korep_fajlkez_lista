import epuletek

epuletek_lista=epuletek.fajlbeolvasas()
print("")
hossza=epuletek.epuletek_szama(epuletek_lista)
print("III/A, B:")
print(f"\tAz épületek száma: {hossza}")
magasepuletekszama=epuletek.magas_epuletek_szama(epuletek_lista)
print("III/C:")
print(f"\tAz 555 lábnál magasabb épületek száma: {magasepuletekszama}.")
legoregebb_index=epuletek.legoregebb(epuletek_lista)
print("III/D:")
print(f"\tA legöregebb épület országa: {epuletek_lista[legoregebb_index].orszag}.")
print("")
legtobbem=epuletek.legtobb_em(epuletek_lista)
print(f"\tA legtöbb emelettel rendelkező épület neve és városa: {epuletek_lista[legtobbem].nev, epuletek_lista[legtobbem].varos}.")
