class Gomba:
    def __init__(self, sor: str):
        adatok: [str] = sor.split("@")
        self.nev: str = adatok[0]
        self.nemzettseg: str = adatok[1]
        self.evszak: str = adatok[2]
