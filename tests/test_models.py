import sys
sys.path.append(".")
from src.models import pessoa

def test_concatenacao_nome_sobrenome():
    p1 = pessoa.Pessoa('Caio', 'Sampaio', 22, '0001')
    assert p1.nome_completo() == 'Caio Sampaio' # assert usado no pytest