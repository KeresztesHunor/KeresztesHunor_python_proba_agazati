import szam
import korok
import gombak


# I

szam.kiiras(szam.szam_general())
print()


# II


lista: [int] = korok.lista_feltolt(5)
korok.korok_kiir(lista)
elso_idos_index: int = korok.elso_idos(lista)
korok.konzolra_ir(elso_idos_index)
korok.fajl_ir(elso_idos_index)
print()


# III


gombak.beolvasas()
gombak.gombak_szama()
gombak.papsapka()
gombak.tinoru()
