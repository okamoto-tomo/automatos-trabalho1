'''
b) Extração de padrões com expressões regulares. 
Implemente expressões regulares para identificar e extrair, no mínimo, os seguintes padrões: 
e-mails, telefones, CPFs, datas, horários, datas e horários combinados, URLs, valores 
monetários em reais, nomes próprios (definir critérios e justificar). Para cada tipo de 
padrão, o sistema deve: aplicar a expressão regular aos arquivos; extrair todas as 
ocorrências encontradas; indicar em qual arquivo ocorreram.
'''

import re

def extrair_valores(arquivo: tuple[str, list[str]], expressoes_regulares: dict[str, str]) -> list[tuple[str, str, str]]:
    '''
    Extrai valores de cada linha do arquivo utilizando expressões regulares.
    
    params:
        arquivo (tuple[str, list[str]]): Tupla contendo o caminho e o conteúdo do arquivo.
        expressoes_regulares (dict[str, str]): Dicionário de pares `tipo: expressão regular`.
    returns: 
        lista_extracao (list[tuple[str, str, str]]): Lista de tuplas contendo o tipo, 
        a string extraída e o arquivo de origem.
    '''
    
    lista_extracao = []
    
    origem = arquivo[0]
    conteudo = arquivo[1]
    
    for tipo, expressao_regular in expressoes_regulares.items():
        for linha in conteudo:
            matches = re.findall(expressao_regular, linha)
            
            if matches:
                for valor in matches:
                    lista_extracao.append((tipo, valor, origem))
                    
    return lista_extracao

