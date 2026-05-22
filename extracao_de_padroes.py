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

        try:
            with open(caminho_completo, 'r', encoding='utf-8') as f:
                linhas = f.readlines()
        except Exception as e:
            print(f" Erro ao ler o arquivo {nome_arquivo}: {e}")
            continue

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

    # Salva os dados extraídos em um arquivo JSON
    try:
        with open(arquivo_json_saida, 'w', encoding='utf-8') as f_out:
            json.dump(dados_extraidos, f_out, indent=4, ensure_ascii=False)
        print("======================================================")
        print(f"Sucesso. Total de elementos extraídos: {len(dados_extraidos)}")
        print(f"Arquivo gerado para integração: {arquivo_json_saida}")
        print("======================================================")
    except Exception as e:
        print(f" Erro ao salvar o arquivo JSON: {e}")

if __name__ == "__main__":
    PASTA_INPUT = "assets"
    ARQUIVO_INTEGRACAO = "dados_extraidos.json"
    
    realizar_extracao_academicas(PASTA_INPUT, ARQUIVO_INTEGRACAO)