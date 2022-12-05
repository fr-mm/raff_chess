from dataclasses import dataclass

from peca import Peca


@dataclass
class Casa:
    nome: str
    conteudo: Peca or None = None

    def to_str(self) -> str:
        if self.conteudo:
            return self.conteudo.char
        else:
            return ' '
