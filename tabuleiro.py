from typing import List

from casa import Casa


class Tabuleiro:
    matrix: List[List[Casa]]
    __letras = [char for char in 'abcdefgh']

    def __init__(self) -> None:
        self.matrix = self.criar_tabuleiro()

    def criar_tabuleiro(self) -> List[List[Casa]]:
        tabuleiro = []
        for numero in range(8, 0, -1):
            linha = []
            for letra in self.__letras:
                linha.append(Casa(f'{letra}{numero}'))
            tabuleiro.append(linha)
        return tabuleiro

    def print(self) -> None:
        [print(' '.join([f'[{casa.nome}]' for casa in linha])) for linha in self.matrix]

    def trazer_casa(self, comando: str) -> Casa:
        try:
            letra = comando[0]
            numero = comando[1]

            letra_id = self.__letras.index(letra)
            numero_id = int(numero)

            return self.matrix[8 - numero_id][letra_id]
        except Exception:
            Exception('comando inválido')


if __name__ == '__main__':
    Tabuleiro().print()
