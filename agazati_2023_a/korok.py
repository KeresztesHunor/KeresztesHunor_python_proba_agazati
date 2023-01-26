def lista_feltolt(db: int) -> [int]:
    print("II:")
    lista: [int] = []
    for i in range(db):
        lista.append(beker_vizsgalattal())
    return lista


def beker_vizsgalattal() -> int:
    szam: int = szam_beker()
    while not (0 <= szam <= 120):
        print("\tHiba! Határon kívüli érték.")
        szam = szam_beker()
    return szam


def szam_beker() -> int:
    return int(input("\tAdj meg egy kort [0-120]: "))


def korok_kiir(lista: [int]):
    print("II/A, B, C:", end="\n\t")
    egyel_kevesebb: int = len(lista) - 1
    for i in range(egyel_kevesebb):
        print(lista[i], end=":")
    print(lista[egyel_kevesebb])


def elso_idos(lista: [int]) -> int:
    elso_idos_index: int = 0
    while lista[elso_idos_index] <= 70 and elso_idos_index < len(lista):
        elso_idos_index += 1
    return elso_idos_index


def konzolra_ir(elso_idos_index: int):
    print(f"II/D, E:\n\tElső idős ember korának helye a listában: {elso_idos_index + 1}")


def fajl_ir(elso_idos_index: int):
    f = open("oreg.txt", "w", encoding="utf8")
    f.write(f"II/F:\n\tElső idős ember korának helye a listában: {elso_idos_index + 1}")
    f.close()
