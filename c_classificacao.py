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
        tipo, valor, origem = entrada[:3]
        
        if tipo not in ["email", "telefone", "cpf", "url"]:
            continue
        
        lista_classificacao.append((tipo, 
                                    valor, 
                                    origem, 
                                    bool(re.fullmatch(expressoes_regulares[tipo], valor)),
                                    ))
        
    return lista_classificacao


def validar_csv(arquivo: tuple[str, list[str]], expressoes_regulares: dict[str, str]) -> tuple[int, list[tuple[str, bool]], bool]:
    '''
    Valida os registros e os campos de um arquivo CSV, verificando:
        1. Se o campo é válido;
        2. Se o registro é válido (ou seja, se todos os campos de um registro são válidos).
    
    params:
        arquivo (tuple[str, list[str]]): Tupla que contém o caminho e o conteúdo do CSV.
        expressoes_regulares (dict[str, str]): Dicionário que contém os pares `tipo: regex`.
        
    returns:
        lista_csv (tuple[int, list[tuple[str, bool]], bool]): Lista de tuplas as quais contém:
            1. Id: Identificador do registro.
            2. matches: Lista de duplas `valor, validade`.
            3. validade: Bool que monitora se o registro válido ou inválido.
            4. caminho: Arquivo de origem.
    '''
    
    lista_csv = []
    
    caminho = arquivo[0]        
    conteudo = arquivo[1]
    
    campos = ["nome", "email", "telefone", "cpf", "data_e_horario", "dinheiro"]

    for linha in conteudo:
        Id, *valores = linha.strip().split(";")[:7]
        Id = int(Id)
        matches = [(valor, bool(re.fullmatch(expressoes_regulares[campo], valor))) for campo, valor in zip(campos, valores)]
        validade = all(match for _, match in matches)
        
        lista_csv.append((Id, matches, validade, caminho))

    return lista_csv