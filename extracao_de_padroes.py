### implementação com expressão regular pra identificar e extrair os dados 




import re
import os
import json
from lib.regex_patterns import regex

def realizar_extracao_academicas(pasta_assets, arquivo_json_saida):
    if not os.path.exists(pasta_assets):
        print(f"Erro: A pasta '{pasta_assets}' não foi encontrada.")
        return

    dados_extraidos = []
    
    #lê os arquivos da pasta assets ignorando arquivos ocultos
    arquivos = [f for f in os.listdir(pasta_assets) if os.path.isfile(os.path.join(pasta_assets, f)) and not f.startswith('.')]

    print("======================================================")
    print ("---Extrator de padrões regex---")
    print("======================================================")

    for nome_arquivo in arquivos:
        caminho_completo = os.path.join(pasta_assets, nome_arquivo)
        print(f" Processando o arquivo de entrada: {nome_arquivo}")

        linhas = leitura_e_inspecao.ler_arquivo(caminho_completo)

        # Varre linha por linha do arquivo (ignora o cabeçalho se for CSV)
        for num_linha, linha in enumerate(linhas, start=1):
            if num_linha == 1 and nome_arquivo.endswith('.csv'):
                continue # Pula o cabeçalho id;nome;email

            for tipo_dado, expressao in regex.items():
                achados = re.findall(expressao, linha)
                
                for valor in achados:
                    if isinstance(valor, tuple):
                        valor = valor[0]
                    
                    valor_limpo = valor.strip()
                    if not valor_limpo:
                        continue
                    
                    # Guarda os dados conforme a especificação do item d)
                    ocorrencia = {
                        "tipo": tipo_dado,
                        "valor_extraido": valor_limpo,
                        "arquivo_origem": nome_arquivo,
                        "linha": num_linha,
                        "classificacao": None #okamoto preenche
                    }
                    dados_extraidos.append(ocorrencia)


# falta expressoes_regulares
import leitura_e_inspecao
import re

def extrair_valores(caminho: str, expressoes_regulares: dict) -> list[tuple[str, str, str]]:
    lista = []
    
    arquivo_origem = caminho.replace("assets/", "")
    arquivo = leitura_e_inspecao.ler_arquivo(caminho)[1][:10]
    
    for chave in expressoes_regulares.keys():
        tipo = chave
        
        for linha in arquivo:
            expressao_regular = expressoes_regulares[tipo]
            matches = re.findall(expressao_regular, linha)
            
            if matches:
                for valor in matches:
                    lista.append((tipo, valor, arquivo_origem))
                    
    return lista

