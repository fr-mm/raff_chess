from dataclasses import dataclass


@dataclass
class Peca:
    char: str

    @classmethod
    def peao(cls):
        return cls("p")

    @classmethod
    def torre(cls):
        return cls("R")

    @classmethod
    def cavalo(cls):
        return cls("N")

    @classmethod
    def bispo(cls):
        return cls("B")

    @classmethod
    def rainha(cls):
        return cls("Q")

    @classmethod
    def rei(cls):
        return cls("K")
