import random


def szam_general() -> int:
    szam: int = random.randint(1, 50)
    print("I/A:\n\tA generált szám:", szam)
    return szam


def kiiras(szam: int):
    print("I/B:")
    if szam % 3 == 0:
        if szam % 5 == 0:
            print("\tA szám hárommal és öttel is osztható.")
        else:
            print("\tA szám hárommal osztható.")
    elif szam % 5 == 0:
        print("\tA szám öttel osztható.")
    else:
        print("\tA szám nem osztható hárommal és öttel sem.")
