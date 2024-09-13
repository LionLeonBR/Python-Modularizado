# importar as models e controlers
# é uma importação relativa então devemos usar o seguinte:

import sys
from pathlib import Path # normaliza o uso dos caminhos para diferentes sistemas operacionais, widows src/nome_pasta/1.py, linus src\nome_pasta\1.py, normaliza as barras
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root)) # adiciona na lista path o caminho

from controler.pessoa import PessoaController
from models.pessoa import Pessoa

while True:
    decisao = int(input("1 - salvar, 2 - listar: "))

    if decisao == 1:
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        idade = input("Idade: ")
        cpf = input("CPF: ")

        p1 = Pessoa(nome=nome,sobrenome=sobrenome,idade=idade,cpf=cpf)

        PessoaController.salvar_pessoar(p1)
    elif decisao == 2:
        print(PessoaController.listar_pessoas())
    else:
        break