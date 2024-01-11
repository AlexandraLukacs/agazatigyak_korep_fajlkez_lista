from Epulet import Epulet
def fajlbeolvasas():
    epuletek_lista=[] # objektumok
    f=open("epulet.txt", "r", encoding="utf-8")
    f.readline()
    fajl_lista=f.readlines()
    f.close()
    # print(fajl_lista[0]) fájlnak az első sora a fejléc nélkül
    for i in range(0, len(fajl_lista), 1):
        aktsor=fajl_lista[i].replace(",", ".").strip().split("$")
        epuletem=Epulet(aktsor[0], aktsor[1], aktsor[2], float(aktsor[3]), int(aktsor[4]), int(aktsor[5]))
        print(epuletem.nev, epuletem.varos, epuletem.orszag, epuletem.magassag, epuletem.em_szam, epuletem.epult)
        epuletek_lista.append(epuletem)
    return epuletek_lista

def epuletek_szama(lista):
    return len(lista)

def magas_epuletek_szama(lista):
    db: int= 0
    for i in range(0, len(lista), 1):
        if lista[i].magassag > (555/3.280839895):
            db += 1
    return db

def legoregebb(lista):
    max_index = 0
    for i in range(0, len(lista), 1):
        # összhasonlítom az aktuális elemet és az eddigi maximumot
        if lista[i].epult <= lista[max_index].epult:
            max_index = i
    return max_index

"""A legtöbb emelettel rendelkező épület neve és városa"""
def legtobb_em(lista):
    max_index = 0
    for i in range(0, len(lista), 1):
        if lista[i].em_szam > lista[max_index].em_szam:
            max_index = i
    return max_index