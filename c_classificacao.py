'''
c) Classificação entre cadeias válidas e inválidas. 
Os arquivos contêm dados válidos e inválidos. O sistema deve ser capaz de 
classificá-los com base em critérios estruturais definidos por expressões regulares. 
Deve-se, no mínimo, classificar: e-mails válidos e inválidos; telefones válidos e 
inválidos; CPFs bem formatados e mal formatados; URLs válidas e inválidas; registros 
inconsistentes no arquivo CSV. Obs.: Não é necessário validar regras semânticas 
(por exemplo, dígitos verificadores de CPF), exceto se o grupo desejar implementar 
como diferencial.
'''
import re

def classificar_valores(entradas: list[tuple[str, str, str]], expressoes_regulares: dict[str, str]) -> list[tuple[str, str, str, bool]]:
    '''
    Classifica os valores em strings válidas e inválidas de acordo com expressões regulares de classificação.
    
    params:
        entradas (list[tuple[str, str, str]]): Lista de entradas com campos `tipo, valor, origem`.
        expressoes_regulares (dict[str, str]): Dicionário de expressões regulares de classificação.
    returns:
        lista_classificacao (list[tuple[str, str, str, bool]]): Lista de entradas com campos `tipo, valor, origem, validade`.
    '''
    
    lista_classificacao = []
    
    for entrada in entradas:
        tipo, valor, origem = entrada[0], entrada[1], entrada[2]
        
        if tipo not in ["email", "telefone", "cpf", "url"]:
            continue
        
        lista_classificacao.append((tipo, 
                                    valor, 
                                    origem, 
                                    bool(re.fullmatch(expressoes_regulares[tipo], valor)),
                                    ))
        
    return lista_classificacao


def validar_csv():
        
        