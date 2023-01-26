from Gomba import Gomba


lista: [Gomba] = []


def beolvasas():
    f = open("gombak_jav.txt", "r", encoding="utf8")
    sorok: [str] = f.readlines()
    for i in range(1, len(sorok)):
        lista.append(Gomba(sorok[i]))
    f.close()


def gombak_szama():
    print("III/A, B:\n\tA gombák száma:", len(lista))


def papsapka():
    elso_papsapka_index: int = 0
    while lista[elso_papsapka_index].nemzettseg.find("papsapkagombák") != -1 and elso_papsapka_index < len(lista):
        print(lista[elso_papsapka_index].nemzettseg)
        elso_papsapka_index += 1
    print("III/C:\n\tAz első papsapkagomba neve:", lista[elso_papsapka_index].nev)


def tinoru():
    db: int = 0
    for i in range(len(lista)):
        if lista[i].nemzettseg == "tinóru":
            db += 1
    print("III/D:\n\tA tinóru gombák száma:", db)
