class Ksiazka:
    def __init__(self, tytul, autor, rok):
        self.tytul = str(tytul)
        self.autor = str(autor)
        self.rok = int(rok)

ilosc_ksiazek=int(input())
lista_ksiazek=[]
lista_egzemplarzy=[]

for i in range(ilosc_ksiazek):
    info_ksiazka = eval(input())
    tytul = info_ksiazka[0]
    autor = info_ksiazka[1]
    rok = info_ksiazka[2]
    ksiazka = Ksiazka(tytul, autor, rok)
    lista_ksiazek.append(ksiazka)

tytul = []
ilosc = []
info = []
i = 0

for ksiazka in lista_ksiazek:
    tytul.append(ksiazka.tytul)

for n in tytul:
    ilosc.append(tytul.count(n))

for ksiazka in lista_ksiazek:
    info.append(ksiazka.tytul + ksiazka.autor + str(ilosc[i]))
    i += 1
    info = set(info)
    info = sorted(info)

for info_egzemplarze in info:
    print(info_egzemplarze)
