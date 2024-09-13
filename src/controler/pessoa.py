import sys
from typing import List
from pathlib import Path # normaliza o uso dos caminhos para diferentes sistemas operacionais, widows src/nome_pasta/1.py, linus src\nome_pasta\1.py, normaliza as barras

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root)) # adiciona na lista path o caminho

from models.pessoa import Pessoa


class PessoaController:
    pessoa = []

    @classmethod
    def salvar_pessoar(cls, pessoa: Pessoa) -> None:
        cls.pessoa.append(pessoa)
    
    @classmethod
    def listar_pessoas(cls) -> List[Pessoa]: # Lista de dados da instancia pessoa
        return cls.pessoa